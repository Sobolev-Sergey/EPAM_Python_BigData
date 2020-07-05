import sqlite3


def count_admins(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM users WHERE is_admin = true;')
    admins = int(cur.fetchone()[0])
    conn.close()

    return admins
