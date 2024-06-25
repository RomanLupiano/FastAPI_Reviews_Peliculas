import requests

URL = 'http://127.0.0.1:8000/api/v1/users'

USER = {
    'username': 'string',
    'password': 'string'
}

response = requests.post(URL + '/login', json=USER)

if response.status_code == 200:
    print(response.text)
    print(response.cookies) #RequestCookieJar
    print(response.cookies.get_dict()) #dict
    
    response = requests.get(URL + '/reviews', cookies=response.cookies.get_dict())
    print(response.text)


