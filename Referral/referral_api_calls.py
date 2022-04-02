import base64
import json

import requests
import urllib3
from Referral import config
from behave import step

urllib3.disable_warnings()


@step("User is logged in")
def fetchAccessToken():
    """
    This method returns the access token generated in the string format
    :return: access_token
    """
    login_url = config.BASE_URL + config.TOKEN_URL
    req = requests.post(login_url, verify=False)
    json_response = req.json()
    access_token = json_response.get("access_token")
    return access_token


def read_json():
    json_file = open("data_for_referral.json", "r").read()
    json_content = json.loads(json_file)
    data = json_content['data']['labels']


def get_prefetch_content():
    """
    This method hits the prefetch api and returns the response in dictionary format.
    :return: prefetch_content_resp
    """
    prefetch_api = config.BASE_URL + config.V6_URL
    payload = open("data_for_referral.json", "r").read()
    token = "Bearer " + str(fetchAccessToken())
    header_value = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': token}
    req = requests.post(prefetch_api, json=json.loads(payload), headers=header_value, verify=False)
    # If you try data=json.loads(payload) then you will get Invalid json error. So use "json=json.loads(payload)"
    prefetch_content_resp = req.json()  # returns a dict
    # response_to_json = json.dumps(response)  # returns a json
    return prefetch_content_resp


@given(": User is logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given : User is logged in')