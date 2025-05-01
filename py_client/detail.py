import requests

endpoint = 'http://localhost:8000/api/product/2/'

get_respond = requests.get(endpoint)
# print(get_respond.headers)
print(get_respond.json())