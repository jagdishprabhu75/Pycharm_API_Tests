import requests
import json

mydata = open("create_user.json", "r").read()
resp = requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print("Status code returned: {code}".format(code=resp.status_code))
