import requests

payload = {
    "name": "Jagdish",
    "job": "Test Lead"
}

resp = requests.post("https://reqres.in/api/users", payload)
json_resp = resp.json()
print(json_resp)
assert json_resp["name"] == payload["name"]
assert json_resp["createdAt"] is not None
assert json_resp["id"] is not None