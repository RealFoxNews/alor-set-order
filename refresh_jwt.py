import requests

url = "https://oauthdev.alor.ru/refresh"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)