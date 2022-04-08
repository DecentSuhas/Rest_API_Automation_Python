import json

import requests
import urllib3
from Referral.Base_utilities import config
from behave import step

urllib3.disable_warnings()

getAccessToken = ""
prefetch_content = {}


@step("User is logged in")
def fetchAccessToken(context):
    """
    This method returns the access token generated in the string format
    :return: access_token
    """
    login_url = config.BASE_URL + config.TOKEN_URL
    req = requests.post(login_url, verify=False)
    json_response = req.json()
    access_token = json_response.get("access_token")
    # return access_token
    global getAccessToken
    getAccessToken = access_token


def read_json():
    json_file = open("../Data/data_for_referral.json", "r").read()
    json_content = json.loads(json_file)
    data = json_content['data']['labels']


def get_prefetch_content(context):
    """
    This method hits the prefetch api and returns the response in dictionary format.
    :return: prefetch_content_resp
    """
    prefetch_api = config.BASE_URL + config.V6_URL
    # cwd = os.getcwd()
    # files = os.listdir(cwd)
    # print("Files in %r: %s" % (cwd, files))
    payload = open("Referral/Data/data_for_referral.json", "r").read()
    token = "Bearer " + getAccessToken
    header_value = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
    req = requests.post(prefetch_api, json=json.loads(payload), headers=header_value, verify=False)
    # If you try data=json.loads(payload) then you will get Invalid json error. So use "json=json.loads(payload)"
    prefetch_content_resp = req.json()  # returns a dict
    # response_to_json = json.dumps(response)  # returns a json
    return prefetch_content_resp


@step("I hit the prefetch api and get the response")
def prefetch_content_response(context):
    global prefetch_content
    prefetch_content.update(get_prefetch_content(context))


def clear_prefetch_resp_dict(context):
    prefetch_content.clear()
