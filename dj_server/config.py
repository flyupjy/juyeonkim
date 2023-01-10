import os

import requests


url = "https://api.doppler.com/v3/configs/config/secrets/download?project=juyeonkim&config=dev&format=json&include_dynamic_secrets=true&dynamic_secrets_ttl_sec=1800"

headers = {
    "accept": "application/json",
    "authorization": os.getenv("DOPPLER")
}

response = requests.get(url, headers=headers)

ENV = response.json()