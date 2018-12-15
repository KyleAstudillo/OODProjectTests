#!/usr/bin/python

import requests
import json

server_url = 'https://oodservercloudserver.azurewebsites.net/api/coffee'
okta_server = 'https://dev-********.oktapreview.com'
apikey = '*******' 
data = {}
username = '*****@yahoo.com'
password = '*******'

headers = {'Accept': 'application/json', 'Content-Type':'application/json', "Authorization": "SSWS ********"}
body = { "appName": "OODProject", "apikey": "{0}".format(apikey), "username": "{0}".format(username), "password": "{0}".format(password), "options": { "multiOptionalFactorEnroll": True, "warnBeforePasswordExpired": True }}

body['headers'] = headers
print(json.dumps(body))
r = requests.post(url='{0}/api/v1/authn'.format(okta_server), headers=headers, json=body)
print(r.json())
authtoken = 'e******wiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlpUNmMzWkpLQ1pxZHpQTDlfM0tUYXhNNmlKMmhEYXV2bGRLZEpjVU1RNm8iLCJpc3MiOiJodHRwczovL2Rldi00OTM2MDYub2t0YXByZXZpZXcuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTU0NDQ5NTkxNiwiZXhwIjoxNTQ0NDk5NTE2LCJjaWQiOiIwb2Fod2pxOWNnSHVWbld2SjBoNyIsInVpZCI6IjAwdWh4MndobTRySTRaSEdQMGg3Iiwic2NwIjpbIm9wZW5pZCIsImVtYWlsIl0sInN1YiI6Imt5bGUuYXN0dWRpbGxvQHlhaG9vLmNvbSJ9.JfMozE554wm-U4Woof8oU67MOO8ZTHRzczHNPxLvWl43b65_AT1tXhmXUJyVRxbrbZGJpcj3nQqwuJ_QiVJqk85lj_qTPcjpVJiPCFuy372-Vy_cluiCSedN5w0x-nMXDB0u2MDrZ95CyTlzsd10jqycyZFiqic79GIsD-QE0SsCWKdREOgvtqQBtp-RqAXNK-pE6RcSQbwe7rk2YR9vcZgL5IZ9SWjlZMZMcZPu5eQn12oyz5Ub1fyKy29XayqwPilCI_ni-_7yUOJ45NtYdIHMugPmpYpBeqO6kv0JUIfknOQtq-gorhJ1WXZOvtSdOUfqE058q-U-Oerh_302YA'
print(authtoken)

urlOptions  = "?id={0}&name={1}&imageLink1={2}&imageLink2={3}&userId={4}&coffeeId={5}".format(23, "TestAuth", "null", "null", 23, 23)
urlCustom = server_url + urlOptions
r = requests.post(url=urlCustom)
print(r.status_code, r.reason)


headers = {'Content-Type':'application/json', "Authorization": "Bearer {0}".format(authtoken)}
payload = {"id": 23, "name":"TestAuth", "imageLink1":"null", "imageLink2":"null", "userId": 23, "coffeeId": 23}
r = requests.post(url=urlCustom, headers=headers)
print(r.status_code, r.reason)


