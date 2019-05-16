#!/usr/bin/env python
import webbrowser

from oauth2client import client
from oauth2client.file import Storage
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google_auth_oauthlib.flow import InstalledAppFlow

# 나중에, 이거 크레덴셜이 자꾸 없다고 하니까 로컬서버에서 연 다음 다른 방법으로
# 크레덴셜 오브젝트를 가져오는 방향으로 구현해보자

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secrets.json"

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
#scopes=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'])
flow = InstalledAppFlow.from_client_secrets_file(
    client_secrets_file,
    scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

request = youtube.liveBroadcasts().list(
    part="snippet",
    id="BRHNUf8gTQE")

response = request.execute()
print(response)

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