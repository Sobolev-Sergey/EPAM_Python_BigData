import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock, patch

from users_api import add_admin, get_admins


class TestUsersAPI(unittest.TestCase):

    @patch('users_api.requests')
    def test_get_admins(self, mock_requests):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = [
            {'name': 'alice', 'email': 'alice@mail.com', 'is_admin': False},
            {'name': 'bob', 'email': 'bob@mail.com', 'is_admin': False},
            {'name': 'admin', 'email': 'admin@mail.com', 'is_admin': True},
            {'name': 'carrol', 'email': 'carrol@mail.com', 'is_admin': True}
        ]
        mock_requests.get.return_value = response_mock

        self.assertEqual(len(get_admins()), 2)

    def test_not_found_error(self):
        with patch('users_api.requests') as mock_requests:
            response_mock = Mock()
            response_mock.status_code = 404
            mock_requests.get.return_value = response_mock

            self.assertIsNone(get_admins())

    def test_timeout_error(self):
        from users_api import requests
        with patch.object(requests, 'post', side_effect=Timeout):
            with self.assertRaises(Timeout):
                add_admin('Daniel', 'daniel@mail.com')


if __name__ == '__main__':
    unittest.main()
