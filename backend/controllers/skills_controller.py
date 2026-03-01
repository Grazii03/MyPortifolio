from backend.models.db import get_conn

def list_skills():
    conn = get_conn()
    hard = conn.execute("SELECT texto FROM skills WHERE tipo='hard' ORDER BY ordem;").fetchall()
    soft = conn.execute("SELECT texto FROM skills WHERE tipo='soft' ORDER BY ordem;").fetchall()
    conn.close()

    return {
        "hard": [r["texto"] for r in hard],
        "soft": [r["texto"] for r in soft],
    }