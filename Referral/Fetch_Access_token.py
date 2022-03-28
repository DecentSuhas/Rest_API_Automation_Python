import base64
import json

import requests
import urllib3

urllib3.disable_warnings()

baseUrl = "https://philips.extole.io"
api_token = "/api/v5/token"
api_v6_zones = "/api/v6/zones"


def fetchAccessToken():
    login_url = "https://philips.extole.io/api/v5/token"
    req = requests.post(login_url, verify=False)
    json_response = req.json()
    access_token = json_response.get("access_token")
    return access_token


def read_json():
    json_file = open("data_for_referral.json", "r").read()
    json_content = json.loads(json_file)
    data = json_content['data']['labels']


def show_prefetch_content():
    prefetch_api = "https://philips.extole.io/api/v6/zones"
    payload = open("data_for_referral.json", "r").read()
    token = "Bearer " + str(fetchAccessToken())
    header_value = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
    req = requests.post(prefetch_api, json=json.loads(payload), headers=header_value, verify=False)
    # If you try data=json.loads(payload) then you will get Invalid json error. So use json
    test = req.json()
    print(type(test))

show_prefetch_content()
