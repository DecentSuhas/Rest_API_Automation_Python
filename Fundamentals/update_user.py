import json
import requests
import urllib3
urllib3.disable_warnings()

#If the record exists then it will update/replace
#If the record does not exists then it will create

# PUT - For put you need to give all the properties/resources
# PATCH - For patch you can specify only specific property

def update_record_PUT():
    payload = {
        "name": "John",
        "job": "Clerk"
    }
    update = requests.put("https://reqres.in/api/users/2", data=payload, verify=False)
    print(update)
    print(update.json())

def update_record_PATCH():
    payload = {
        "name": "Dinesha"
    }
    update = requests.put("https://reqres.in/api/users/2", data=payload, verify=False)
    print(update)
    print(update.json())

update_record_PATCH()