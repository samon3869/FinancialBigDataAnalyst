# crud_ops.py
import sqlite3

# ---------- Read  ----------

def fetch_concepts(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    sql = """
        SELECT *
        FROM concepts
        ORDER BY concept_id
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    return rows