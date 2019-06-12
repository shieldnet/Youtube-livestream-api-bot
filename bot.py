#!/usr/bin/env python

from time import sleep
import sys
from youtubechat import YoutubeLiveChat, get_live_chat_id_for_broadcast_id, get_live_chat_id_for_stream_now
from youtubechat import get_broadcast_start_time
argv = sys.argv

if len(argv) is not 2:
    print("Use like bot.py <broadcast_id>")
    exit(0)

broadcast_id = str(argv[1])

print(broadcast_id)

livechat_id = get_live_chat_id_for_broadcast_id(broadcast_id,"oauth_creds")
print(livechat_id)

chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])


# Command
def uptime(chatid):
    response = '방송이 시작된 지, '+get_broadcast_start_time(broadcast_id,"oauth_creds") + '이 지났습니다.';
    chat_obj.send_message(response, chatid)


#Parsing Commands
def respond(msgs, chatid):
    for msg in msgs:
        print(msg)
        if msg.message_text.find('!업타임') != -1:
            uptime(chatid)
        elif msg.message_text.find('!앵무새') != -1:
            chat_obj.send_message("DDOKDDOK "+msg.message_text[4:], chatid)
            msg.delete()
        else:
            print(msg)



# Enroll Bot to thread
try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()

