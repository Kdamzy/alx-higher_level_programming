#!/usr/bin/python3
"""
 script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
