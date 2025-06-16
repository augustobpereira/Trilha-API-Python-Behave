import requests

url = "https://api.restful-api.dev/objects"
data = {'id':1}
response = requests.get(url,data)
print(response.json())