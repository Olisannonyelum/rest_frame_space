import requests

endpoint = 'http://localhost:8000/api/product/1/update/'

data = {
    'title':'this occoure due to update',
}

get_respond = requests.put(endpoint, json=data)
# print(get_respond.headers)
print(get_respond.json())