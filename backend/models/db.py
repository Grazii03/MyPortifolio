import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_conn():
    return psycopg2.connect(
        os.environ["DATABASE_URL"],
        cursor_factory=RealDictCursor
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Postgres table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS skills (
      id BIGSERIAL PRIMARY KEY,
      tipo TEXT NOT NULL,     -- hard | soft
      texto TEXT NOT NULL,
      ordem INT NOT NULL
    );
    """)

    # seed só se vazio
    cur.execute("SELECT COUNT(*) AS n FROM skills;")
    n = cur.fetchone()["n"]

    if n == 0:
        cur.executemany(
            "INSERT INTO skills (tipo, texto, ordem) VALUES (%s, %s, %s);",
            [
                ("hard", "Processamento de sinais EMG", 1),
                ("hard", "Análise Biomecânica do Movimento Humano", 2),
                ("hard", "MATLAB - Intermediário\nPython - Intermediário", 3),
                ("soft", "Pensamento Analítico", 1),
                ("soft", "Trabalho em equipe", 2),
                ("soft", "Formulação Estratégica de Soluções", 3),
            ],
        )

    conn.commit()
    cur.close()
    conn.close()