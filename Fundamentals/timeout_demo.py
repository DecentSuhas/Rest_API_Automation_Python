import requests
import urllib3
urllib3.disable_warnings()


def timeoutDemo():
    req = requests.get("https://httpbin.org/delay/1", timeout=3, verify=False)
    print(req.status_code)

timeoutDemo()