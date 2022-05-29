import requests

p="page=2"
response = requests.get("https://reqres.in/api/users",p)
#response = requests.get("https://reqres.in/api/users")

assert response.status_code == 200, "Status code does not match"

# print(response.text) #content response in unicode
# print(response.content) #content response in bytes
# print(response.json()) #content response in json format
# print(response.headers)
# print(response.headers["Date"])
# print(response.cookies)

json_res = response.json()
print("Current page : {current}".format(current=json_res["page"]))
assert json_res["page"] == 2, "Incorrect current page"

print("Records per page : {rec}".format(rec=json_res["per_page"]))
assert json_res["per_page"] == 6, "Incorrect per page record count"

print("Total pages : {total}".format(total=json_res["total"]))
assert json_res["total"] == 12, "Incorrect total pages"

print("Current page: {total_pg}".format(total_pg=json_res["total_pages"]))
assert json_res["total_pages"] == 2, "Incorrect total pages"

print("Complete data :\n {data}".format(data=json_res["data"]))
print("Data of 1 record:\n {first_rec}".format(first_rec=json_res["data"][0]))
print("email of 1st person: {email}".format(email=json_res["data"][0]["email"]))
assert (json_res["data"][0]["email"]).endswith("reqres.in"), "Incorrect mail"
