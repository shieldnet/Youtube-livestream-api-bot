#!/usr/bin/env python

from time import sleep
from datetime import datetime
import sys
from youtubechat import YoutubeLiveChat, get_live_chat_id_for_broadcast_id, get_live_chat_id_for_stream_now
from youtubechat import get_broadcast_elapsed_time
argv = sys.argv


laugh_global = 0

if len(argv) is not 2:
    print("Use like bot.py <broadcast_id>")
    exit(0)

broadcast_id = str(argv[1])

print(broadcast_id)

livechat_id = get_live_chat_id_for_broadcast_id(broadcast_id,"oauth_creds")
print(livechat_id)

chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])
file_name = datetime.now().strftime("%Y%m%d-%H:%M:%S.txt")

# Logging Function
def log_chat(msg_obj):
    error_to_catch = getattr(__builtins__,'FileNotFoundError', IOError)
    try:
        f=open(file_name,'a')
    except error_to_catch:
        f=open(file_name,'w')

    _author = msg_obj.author.display_name
    _displayed_msg = msg_obj.display_message
    _published_time = str(msg_obj.published_at.strftime("%Y%m%d-%H-%M-%S"))
    f.write('['+_published_time+'] ' + _author +' : ' +_displayed_msg+'\n')
    f.close()


# Command
def uptime(chatid):
    response = '방송이 시작된 지, '+get_broadcast_elapsed_time(broadcast_id,"oauth_creds") + '이 지났습니다.'
    chat_obj.send_message(response, chatid)

def laugh(chatid):
    response = "으악ㅋㅋㅋ똑똑이도 웃겨ㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
    chat_obj.send_message(response, chatid)


#Parsing Commands
def respond(msgs, chatid):
    global laugh_global

    for msg in msgs:
        print(msg)
        log_chat(msg)
        if msg.message_text.find('!업타임') != -1:
            uptime(chatid)

        elif msg.message_text.find('!앵무새') != -1:
            chat_obj.send_message("DDOKDDOK "+msg.message_text[4:], chatid)
            msg.delete()

        elif msg.message_text.find('ㅋㅋㅋ') != -1:
            laugh_global = laugh_global+1
            if laugh_global%5==0:
                laugh(chatid)
        else:
            True
            #Nothing



# Enroll Bot to thread
try:
    chat_obj.start()
    chat_obj.subscribe_chat_message(respond)
    chat_obj.join()

finally:
    chat_obj.stop()

