""" It includes basic referral api response"""
import json
from behave import step # pylint: disable=no-name-in-module
import requests
import urllib3
from Referral.utilities import config

urllib3.disable_warnings()

get_access_token = ""
prefetchContent = {}


@step("User is logged in")
def fetch_accessToken(context):
    """
    This method returns the access token generated in the string format
    :return: access_token
    """
    login_url = config.BASE_URL + config.TOKEN_URL
    req = requests.post(login_url, verify=False)
    json_response = req.json()
    access_token = json_response.get("access_token")
    # return access_token
    global get_access_token
    get_access_token = access_token


def read_json():
    json_file = open("../data/data_for_referral.json", "r").read()
    json_content = json.loads(json_file)
    data = json_content['data']['labels']


def getPrefetchContent(context):
    """
    This method hits the prefetch api and returns the response in dictionary format.
    :return: prefetch_content_resp
    """
    prefetch_api = config.BASE_URL + config.V6_URL
    # cwd = os.getcwd()
    # files = os.listdir(cwd)
    # print("Files in %r: %s" % (cwd, files))
    payload = open("Referral/data/data_for_referral.json", "r").read()
    token = "Bearer " + get_access_token
    header_value = {'Content-type': 'application/json',
                    'Accept': 'application/json', 'Authorization': token}
    req = requests.post(prefetch_api, json=json.loads(payload),
                        headers=header_value, verify=False)
    # If you try data=json.loads(payload) then you will get Invalid json error. So use "json=json.loads(payload)"
    prefetch_content_resp = req.json()  # returns a dict
    # response_to_json = json.dumps(response)  # returns a json
    return prefetch_content_resp


@step("I hit the prefetch api and get the response")
def prefetch_content_response(context):
    """
    It captures the prefetch content
    :param context:
    :return:
    """
    global prefetchContent
    prefetchContent.update(getPrefetchContent(context))


def clear_prefetch_resp_dict(context):
    """
    It clears the dictionary
    :param context:
    :return:
    """
    prefetchContent.clear()
