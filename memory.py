
import sqlite3

DB_NAME = "continuum.db"


def initialise_memory():
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL COLLATE NOCASE UNIQUE,
                value TEXT NOT NULL
            )
        """)


def save_memory(key, value):
    key = key.strip().casefold()
    value = value.strip()

    if not key or not value:
        raise ValueError("Memory key and value cannot be empty.")

    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            INSERT INTO memories (key, value)
            VALUES (?, ?)
            ON CONFLICT(key)
            DO UPDATE SET value = excluded.value
        """, (key, value))


def get_memory(key):
    key = key.strip().casefold()

    with sqlite3.connect(DB_NAME) as connection:
        result = connection.execute(
            "SELECT value FROM memories WHERE key = ?",
            (key,)
        ).fetchone()

    return result[0] if result else None


def delete_memory(key):
    key = key.strip().casefold()

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute(
            "DELETE FROM memories WHERE key = ?",
            (key,)
        )

        return cursor.rowcount > 0
