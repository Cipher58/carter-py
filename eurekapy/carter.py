import requests
import json
import time
from .utils import convert_to_string, URLS, tokenize, request_template


def carterRequest(url, data, headers):
    try:
        response = requests.post(
            url, data=json.dumps(data), headers=headers)
        carter_data = response.json()
        return {"carter_data": carter_data, "status_code": response.status_code, "status_message": response.reason, "ok": response.ok, "url": response.url}
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        return None


class Eureka:
    def __init__(self, api_key, uiname):
        self.api_key = api_key
        self.history = []

    def say(self, text, user_id):
        user_id = str(user_id)
        text = str(text)

        BASE_URL = "https://api.eureka-ai.dev"
        headers, data = request_template(self.api_key, text, user_id, self.uiname)
        response = requests.post(f"{BASE_URL}/chat", json=data, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return {"error": "Error occurred during chat request"}
