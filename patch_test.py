import requests
import json


patch_data = open("patch_data.json","r").read()
json_resp=requests.patch("https://reqres.in/api/users/2",json.loads(patch_data))
print("Data after patching: {patch_data_a}".format(patch_data_a=json_resp.json()))
