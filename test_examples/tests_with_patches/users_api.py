import requests


def get_admins():
    r = requests.get('http://localhost/users/')

    if r.status_code == 200:
        users_json = r.json()
        return list(filter(lambda u: u['is_admin'], users_json))
    return None


def add_admin(name, email):
    payload = {
        'name': name,
        'email': email,
        'is_admin': True
    }

    r = requests.post('http://localhost/users/', payload)

    return r.status_code
