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


def fetch_types(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    sql = """
        SELECT *
        FROM types
        ORDER BY type_id
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    return rows


def fetch_problems(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    sql = """
        SELECT *
        FROM problems
        ORDER BY problem_id
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    return rows

# ---------- Create ----------

def add_concept(
    conn: sqlite3.Connection,
    name: str,
    level: int,
    parent_id: Optional[int] = None,
    note_path: Optional[str] = None,
) -> int:
    sql = """
        INSERT INTO concepts (name, level, parent_id, note_path)
        VALUES (?, ?, ?, ?)
    """

    cur = conn.cursor()
    last_id = cur.execute(sql, (name, level, parent_id, note_path)).lastrowid
    conn.commit()
    return last_id


def add_type(
    conn: sqlite3.Connection,
    name: str,
    concept_id: int,
    note_path: Optional[str] = None,
) -> int:
    sql = """
        INSERT INTO types (name, concept_id, note_path)
        VALUES (?, ?, ?)
    """

    cur = conn.cursor()
    last_id = cur.execute(sql, (name, concept_id, note_path)).lastrowid
    conn.commit()
    return last_id


def add_problem(
    conn: sqlite3.Connection,
    year: int,
    number: int,
    type_id: int,
    note_path: Optional[str] = None,
) -> int:
    sql = """
        INSERT INTO problems (year, number, type_id, note_path)
        VALUES (?, ?, ?, ?)
    """

    cur = conn.cursor()
    last_id = cur.execute(sql, (year, number, type_id, note_path)).lastrowid
    conn.commit()
    return last_id

# ---------- Update ----------
def update_concept(
    conn: sqlite3.Connection,
    concept_id: int,
    name: str,
    level: int,
    parent_id: Optional[int],
    note_path: Optional[str],
) -> None:
    sql = """
        UPDATE concepts
        SET name = ?, level = ?, parent_id = ?, note_path = ?
        WHERE concept_id = ?
    """

    cur = conn.cursor()
    cur.execute(sql, (name, level, parent_id, note_path, concept_id))
    conn.commit()


def update_type(
    conn: sqlite3.Connection,
    type_id: int,
    name: str,
    concept_id: int,
    note_path: Optional[str],
) -> None:
    sql = """
        UPDATE types
        SET name = ?, concept_id = ?, note_path = ?
        WHERE type_id = ?
    """

    cur = conn.cursor()
    cur.execute(sql, (name, concept_id, note_path, type_id))
    conn.commit()


def update_problem(
    conn: sqlite3.Connection,
    problem_id: int,
    year: int,
    number: int,
    type_id: int,
    note_path: Optional[str],
) -> None:
    sql = """
        UPDATE problems
        SET year = ?, number = ?, type_id = ?, note_path = ?
        WHERE problem_id = ?
    """

    cur = conn.cursor()
    cur.execute(sql, (year, number, type_id, note_path, problem_id))
    conn.commit()

# ---------- Delete ----------
def delete_concept(conn: sqlite3.Connection, concept_id: int) -> None:
    sql = "DELETE FROM concepts WHERE concept_id = ?"

    cur = conn.cursor()
    cur.execute(sql, (concept_id,))
    conn.commit()


def delete_type(conn: sqlite3.Connection, type_id: int) -> None:
    sql = "DELETE FROM types WHERE type_id = ?"

    cur = conn.cursor()
    cur.execute(sql, (type_id,))
    conn.commit()


def delete_problem(conn: sqlite3.Connection, problem_id: int) -> None:
    sql = "DELETE FROM problems WHERE problem_id = ?"

    cur = conn.cursor()
    cur.execute(sql, (problem_id,))
    conn.commit()
