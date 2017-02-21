import requests
import json
header_list = {"content-type": "application/json", "connection": "keep-alive", "origin": "https://staging.crunchboards.com", "accept": "application/json"}
email = "release_tester@mailinator.com"
password = "Password1!"
credentials = {"email": email, "password": password}
r = requests.post('https://api-staging.crunchboards.com/login/', data=json.dumps(credentials), headers=header_list)
print(r)
token = r.json()['id']
print(token)
