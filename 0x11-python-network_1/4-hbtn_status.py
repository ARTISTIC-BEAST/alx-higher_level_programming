#!/usr/bin/python3
""" 4. What's my status? #1 """

from requests import get

if __name__ == "__main__":
    r = get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
