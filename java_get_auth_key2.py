#!/usr/bin/env python
import webbrowser
import sys
import httplib2
from oauth2client import client
from oauth2client.file import Storage

if not hasattr(__builtins__,'raw_input'):
    # Python 3
    raw_input = input

if len(sys.argv) is not 2:
    print("Not Valid Parameter. Use it scipt.py <authcode>")
    exit(-1)

auth_code = sys.argv[1]
credentials = flow.step2_exchange(auth_code)
http_auth = credentials.authorize(httplib2.Http())
storage = Storage("oauth_creds")
storage.put(credentials)