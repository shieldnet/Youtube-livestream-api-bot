#!/usr/bin/env python

from time import sleep
import sys
from youtubechat import YoutubeLiveChat, get_live_chat_id_for_broadcast_id, get_live_chat_id_for_stream_now

argv = sys.argv

if len(argv) is not 2:
    print("Use like bot.py <broadcast_id>")
    exit(-1)

broadcast_id = str(argv[1])

print(broadcast_id)

livechat_id = get_live_chat_id_for_broadcast_id(broadcast_id,"oauth_creds")
print(livechat_id)

chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])


def respond(msgs, chatid):
    for msg in msgs:
        print(msg)
        if msg.message_text[0] is '!':
            chat_obj.send_message("BOT: " +msg.message_text, chatid)
            msg.delete()

try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()
