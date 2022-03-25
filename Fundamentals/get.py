import requests
import urllib3

urllib3.disable_warnings()
page_num = {"page":2}
resp = requests.get("https://reqres.in/api/users", params=page_num, verify=False)
print(resp)