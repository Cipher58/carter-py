import datetime
from Janex import *

URLS = {
    "say": "https://api.carterlabs.ai/api/chat"
}

def convert_to_string(variable_name, value):
    try:
        return str(value)
    except:
        raise TypeError(f"{variable_name} must be convertible to a string, received {type(value)}")

def iso_now():
    return datetime.datetime.now().isoformat()

def tokenize(value):
    words = tokenize(value)
    return words

def request_template(api_key, text, user_id, uiname):
    headers = {
        "API-Key": api_key
    }
    data = {
        "query": text,
        "user": user_id,
        "agent_name": uiname
    }
    return headers, data
