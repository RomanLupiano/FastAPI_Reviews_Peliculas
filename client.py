import requests

URL = 'http://127.0.0.1:8000/api/v1/reviews'

''' 
headers = {'accept': 'application/json'}

params = {
    'page': '2',
    'limit': '2'
}

response = requests.get(URL, headers=headers, params=params)

if response.status_code == 200:
    if response.headers.get('content-type') == 'application/json':
        for review in response.json():
            print(review)
      
'''
            
            
review = {
  "user_id": 1,
  "movie_id": 1,
  "review": "test desde el requests",
  "score": 1
}

response = requests.post(URL, json=review)

if response.status_code == 200:
    print(response.text)
else:
    print(response.content)


REVIEW_ID = 4
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.get(URL)
print(response.text)
    
    
    
data = {
  "review": "Excelente",
  "score": 5
}

response = requests.put(URL, json=data)
print(response.text)

response = requests.get(URL)
print(response.text)

response = requests.delete(URL)
print(response.text)