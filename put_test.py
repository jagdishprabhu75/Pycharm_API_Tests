import requests
import json

newdata = open("create_user.json", "r").read()
putdata = open("put_data.json").read()
json_resp=requests.put("https://reqres.in/api/users/2",json.loads(newdata))
print("Status code returned: {code}".format(code=json_resp.status_code))
print("Content before post request: \n {json_content}".format(json_content=json_resp.json()))

json_resp=requests.put("https://reqres.in/api/users/2",json.loads(putdata))
print("Status code returned after put request: {code}".format(code=json_resp.status_code))
print("Content after post request: \n {json_content}".format(json_content=json_resp.json()))