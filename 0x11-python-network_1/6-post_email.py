#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the URL.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
