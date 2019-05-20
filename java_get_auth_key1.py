#!/usr/bin/env python
import webbrowser

import httplib2
from oauth2client import client
from oauth2client.file import Storage

if not hasattr(__builtins__,'raw_input'):
    # Python 3
    raw_input = input

flow = client.flow_from_clientsecrets(
    'client_secrets.json',
    scope=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')
auth_uri = flow.step1_get_authorize_url()
webbrowser.open(auth_uri)
