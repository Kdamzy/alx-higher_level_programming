#!/usr/bin/python3
"""Sends a POST request to a URL with a given email"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
   if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = urllib.parse.urlencode({'email': email})
        data = data.encode('utf-8')
        request = urllib.request.Request(url, data)

        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
