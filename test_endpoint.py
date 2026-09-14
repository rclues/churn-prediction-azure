from dotenv import load_dotenv
import os
load_dotenv()
import requests
import json

url = os.getenv("AZURE_ENDPOINT_URL")
api_key = os.getenv("AZURE_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "data": [[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 29.85, 29.85, 1, 0, 0, 0, 0, 1, 0]]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print("Status code:", response.status_code)
print("Response:", response.text)