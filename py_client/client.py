import requests

endpoint = 'http://localhost:8000/api/?this=isTime'

get_respond = requests.post(endpoint, params={'key':'values'}, json={'content':'reply'})
# print(get_respond.headers)
print(get_respond.json())