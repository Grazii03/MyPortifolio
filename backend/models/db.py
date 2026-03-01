import sqlite3

DB_PATH = "backend/portfolio.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS skills(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      tipo TEXT NOT NULL,     -- hard | soft
      texto TEXT NOT NULL,
      ordem INTEGER NOT NULL
    );
    """)

    # seed só se vazio
    n = cur.execute("SELECT COUNT(*) as n FROM skills;").fetchone()["n"]
    if n == 0:
        cur.executemany(
            "INSERT INTO skills (tipo, texto, ordem) VALUES (?, ?, ?);",
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
    conn.close()