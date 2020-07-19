import requests
import json

response = requests.get('http://localhost:5000/api/orders/')
print(response.json())


#response = requests.post('http://localhost:5000/api/orders/')
#print(response.reason)

payload = {
    'name': 'Book 2',
    'price': 10000
}

response = requests.post('http://localhost:5000/api/orders/', json=payload)
print(response.reason)

response = requests.get('http://localhost:5000/api/orders/')
print(response.json())

response = requests.post('http://localhost:5000/api/orders/', json={'name': 'dssd'})
print(response.reason)
