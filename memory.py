import sqlite3

def initialise_memory():
    connection = sqlite3.connect("continuum.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_memory(key, value):
    connection = sqlite3.connect("continuum.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO memories (key, value) VALUES (?, ?)",
        (key, value)
    )

    connection.commit()
    connection.close()

    print(f'Memory saved: {key} = {value}')

def get_memory(key):
    connection = sqlite3.connect('continuum.db')
    cursor = connection.cursor()

    cursor.execute('SELECT value FROM memories WHERE key = ?', (key,)
    )
    result = cursor.fetchone()
    connection.close()

    if result:
        return result[0]

    return None