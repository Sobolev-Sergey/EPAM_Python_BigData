import os
import tempfile
import sqlite3
import pytest

from users_api import count_admins


@pytest.fixture(scope='module')
def db_connection():
    db, db_path = tempfile.mkstemp()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('CREATE TABLE users (username text, email text, is_admin bool);')

    test_users = [
        ('alice', 'alice@mail.com', False),
        ('bob', 'bob@mail.com', False),
        ('admin', 'admin@mail.com', True),
        ('carrol', 'carrol@mail.com', True)
    ]
    cur.executemany('INSERT INTO users VALUES (?, ?, ?);', test_users)
    conn.commit()
    conn.close()

    yield db_path

    os.close(db)
    os.unlink(db_path)


def test_count_admins(db_connection):
    assert count_admins(db_connection) == 2
