#!/usr/bin/env python

from time import sleep

from youtubechat import YoutubeLiveChat, custom_get_live_chat_id_for_stream_now

#!/usr/bin/env python
import webbrowser

import httplib2
from oauth2client import client
from oauth2client.file import Storage

from google_auth_oauthlib.flow import InstalledAppFlow

flow2 = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'])

if not hasattr(__builtins__,'raw_input'):
    # Python 3
    raw_input = input

credential = flow2.run_local_server(host='localhost',
    port=8080, 
    authorization_prompt_message='Please visit this URL: {url}', 
    success_message='The auth flow is complete; you may close this window.',
    open_browser=True)

livechat_id = custom_get_live_chat_id_for_stream_now(credential)
print(livechat_id)
exit(0)

chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])


def respond(msgs, chatid):
    for msg in msgs:
        print(msg)
        msg.delete()
        chat_obj.send_message("RESPONSE!", chatid)


try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()
