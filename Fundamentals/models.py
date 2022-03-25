import requests
import json
import urllib3

urllib3.disable_warnings()
resp = requests.get("https://reqres.in/api/users?page=2", verify=False)
json_response = resp.json()
assert json_response['page'] == 2, "incorrect data recieved"
print(json_response['page'])
assert json_response['total_pages'] == 2, "incorrect data recieved"
print(json_response['total_pages'])
email = json_response['data'][0]['email']
assert email == "michael.lawson@reqres.in", "incorrect email"
assert email.endswith("@reqres.in"), "Incorrect domain"