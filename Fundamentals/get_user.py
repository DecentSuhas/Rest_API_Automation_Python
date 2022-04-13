import logging
import requests
import json

''' Making unverified HTTPS requests is strongly discouraged, however, 
if you understand the risks and wish to disable these warnings, you can use disable_warnings()'''
import urllib3

urllib3.disable_warnings()

logging.captureWarnings(True)
resp = requests.get("https://reqres.in/api/users?page=2", verify=False)
# print(type(resp))
# print(resp)
# print(dir(resp))

code = resp.status_code
assert code == 200, "Code doesn\'t match"
content = resp.content
# print(content)  # this prints in byte
text = resp.text
# print(text)  # This prints in unicode (plain strings)
jsons = resp.json()
# print(jsons)

headers = resp.headers
# print(type(headers))

cookies = resp.cookies
print(cookies)

encodin = resp.encoding
print(encodin)

urls = resp.url
print(urls)
