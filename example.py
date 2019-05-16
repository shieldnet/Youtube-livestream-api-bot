#!/usr/bin/env python

from time import sleep

from youtubechat import YoutubeLiveChat, get_live_chat_id_for_broadcast_id,get_live_chat_id_for_stream_now

broadcast_id = 'BRHNUf8gTQE'

livechat_id = get_live_chat_id_for_broadcast_id(broadcast_id,"oauth_creds")
print(livechat_id)
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
