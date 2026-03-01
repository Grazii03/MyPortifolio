from backend.models.db import get_conn

def list_skills():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT texto FROM skills WHERE tipo=%s ORDER BY ordem;", ("hard",))
    hard = cur.fetchall()

    cur.execute("SELECT texto FROM skills WHERE tipo=%s ORDER BY ordem;", ("soft",))
    soft = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "hard": [r["texto"] for r in hard],  # RealDictCursor -> dict
        "soft": [r["texto"] for r in soft],
    }