import json
import requests
import urllib3

'''
CRUD
 C: Create
 R: Read
 U: Update
 D: Delete

PUT: Update/Replace
PATCH: Update/Modify

'''
urllib3.disable_warnings()


def upload_via_dict_1():
    payload = {
        "name": "John",
        "job": "President"
    }
    create = requests.post("https://reqres.in/api/users", data=payload, verify=False)
    print(create)
    print(create.json())


def upload_via_dict_2():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "Passed"
    }
    create = requests.post("https://reqres.in/api/register", data=payload, verify=False)
    print(create)
    print(create.json())


def upload_via_json():
    user = open("users.json", "r").read()
    req = requests.post("https://reqres.in/api/users", data=json.loads(user), verify=False)
    print(req)
    print(req.json())
    print(req.headers.get("Content-Type"))  # Like this you can get any particular value


upload_via_dict_2()
