import requests
import urllib3
urllib3.disable_warnings()


def basicAuth_validUser():
    req = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'), verify=False)
    print(req.status_code)

def basicAuth_invalidUser():
    req = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('pass','Terrain'), verify=False)
    print(req.status_code)

basicAuth_invalidUser()