import requests

reply = input('what instance will you like to delete from the database: ')
try:
    repy = int(reply)
except:
    print('it look like you enter the wrong input ')
    reply = None

endpoint = f'http://localhost:8000/api/product/{reply}/delete/'

get_respond = requests.delete(endpoint)
# print(get_respond.headers)
print(get_respond.status_code, get_respond.status_code ==204 )