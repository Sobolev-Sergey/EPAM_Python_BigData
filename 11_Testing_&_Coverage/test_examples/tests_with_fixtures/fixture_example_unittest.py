import os
import tempfile
import unittest
import sqlite3

from users_api import count_admins


class TestUsersAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._db, cls._db_path = tempfile.mkstemp()
        conn = sqlite3.connect(cls._db_path)
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

    @classmethod
    def tearDownClass(cls):
        os.close(cls._db)
        os.unlink(cls._db_path)

    def test_count_admins(self):
        self.assertEqual(count_admins(TestUsersAPI._db_path), 3)


if __name__ == '__main__':
    unittest.main()
