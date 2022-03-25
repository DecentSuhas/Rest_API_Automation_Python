import json
import requests
import urllib3
urllib3.disable_warnings()


def delete_a_user():
    req = requests.delete("https://reqres.in/api/users/2", verify=False)
    print(req.status_code)
    assert req.status_code==204, "User deletion failed"

delete_a_user()