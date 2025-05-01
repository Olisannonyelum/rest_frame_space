import requests

title = input('title : ?')


token = '53f2703998412e5757580d39634e0b67078974b5'
headers ={
    'Authorization':f'Token {token}'
}  

endpoint = 'http://localhost:8000/api/product/'

data = {
    'title':title,
    'price':12.2,
    'email':'olisa@gmail.com'
}
get_respond = requests.post(endpoint, json=data, headers=headers)
# print(get_respond.headers)
print(get_respond.json())