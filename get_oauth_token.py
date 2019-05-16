#!/usr/bin/env python
import webbrowser

import httplib2
from oauth2client import client
from oauth2client.file import Storage

from google_auth_oauthlib.flow import InstalledAppFlow

# 나중에, 이거 크레덴셜이 자꾸 없다고 하니까 로컬서버에서 연 다음 다른 방법으로
# 크레덴셜 오브젝트를 가져오는 방향으로 구현해보자

flow2 = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'])

if not hasattr(__builtins__,'raw_input'):
    # Python 3
    raw_input = input

credentials = flow2.run_local_server(host='localhost',
    port=8080, 
    authorization_prompt_message='Please visit this URL: {url}', 
    success_message='The auth flow is complete; you may close this window.',
    open_browser=True)

print(credentials)
 

"""
storage = Storage("oauth_creds")
storage.put(credentials)
"""

"""
flow = client.flow_from_clientsecrets(
    'client_secrets.json',
    scope=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'],
    redirect_uri='http://localhost:8080/oauth2callback')
    # 'urn:ietf:wg:oauth:2.0:oob'])

auth_uri = flow2.step1_get_authorize_url()
webbrowser.open(auth_uri)
auth_code = raw_input("auth code: ")

credentials = flow2.step2_exchange(auth_code)

# http_auth = credentials.authorize(httplib2.Http())
"""