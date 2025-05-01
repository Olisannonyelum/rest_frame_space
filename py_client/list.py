import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/auth/'
# password = getpass()

auth_respond = requests.post(endpoint, json={'username':'olisa', 'password':'olisa12345'})
 
print(auth_respond.json())

if auth_respond.status_code == 200:
    token = auth_respond.json().get('token')
    headers ={
        'Authorization':f'Token {token}'
    }   
    endpoint = 'http://localhost:8000/api/product/'


    get_respond = requests.get(endpoint, headers=headers)
    # print(get_respond.headers) 
    print(get_respond.json())

 