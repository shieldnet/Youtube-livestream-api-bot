#!/usr/bin/env python

from time import sleep
from datetime import datetime
import sys
import pickle
import re
import random
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
file_name = datetime.now().strftime("%Y%m%d-%H-%M-%S.txt")


# Save custom commands to file
def save_custom_commands():
    f = open("custom_commands.dat", "wb")
    pickle.dump(custom_commands, f)
    f.close()


# Load custom commands from file
def load_custom_commands():
    try:
        f = open("custom_commands.dat", "rb")
        obj = pickle.load(f)
        f.close()
        return obj
    except:
        return dict()

custom_commands = load_custom_commands()

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
        auth = msg.author.is_chat_owner or msg.author.is_chat_moderator

        if msg.message_text.strip() == '!업타임':
            uptime(chatid)

        elif msg.message_text.split()[0] == '!앵무새' and len(msg.message_text.split()) >= 2:
            contents = re.split('(\\s+)', msg.message_text)
            real_msg_pos = contents.index('!앵무새') + 1
            chat_obj.send_message("DDOKDDOK " + ''.join(contents[real_msg_pos:]).strip(), chatid)
            msg.delete()

        elif msg.message_text.split()[0] == '!주사위':
            try:
                if len(msg.message_text.split()) < 2:
                    sides = 6
                else:
                    sides = int(msg.message_text.split()[1])
            except:
                sides = 6
            result = random.SystemRandom().randint(1, max(1, sides))

            special_kor = [2, 4, 5, 9]
            chat_obj.send_message('주사위에서 %d%s 나왔습니다!' % (result, ['이', '가'][1 if result % 10 in special_kor else 0]), chatid)

        elif msg.message_text.split()[0] == '!추가' and len(msg.message_text.split()) >= 3 and auth:
            key = msg.message_text.split()[1]
            if key not in custom_commands:
                contents = ' '.join(msg.message_text.split()[2:])
                custom_commands[key] = contents
                save_custom_commands()
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 추가되었습니다.', chatid)
            else:
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 이미 존재합니다.', chatid)

        elif msg.message_text.split()[0] == '!수정' and len(msg.message_text.split()) >= 3 and auth:
            key = msg.message_text.split()[1]
            if key in custom_commands:
                contents = ' '.join(msg.message_text.split()[2:])
                custom_commands[key] = contents
                save_custom_commands()
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 수정되었습니다.', chatid)
            else:
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 존재하지 않습니다.', chatid)

        elif msg.message_text.split()[0] == '!삭제' and len(msg.message_text.split()) == 2 and auth:
            key = msg.message_text.split()[1]
            if key in custom_commands:
                custom_commands.pop(key)
                save_custom_commands()
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 삭제되었습니다.', chatid)
            else:
                chat_obj.send_message('"' + key + '" 커스텀 명령어가 존재하지 않습니다.', chatid)

        elif msg.message_text.strip() in custom_commands:
            chat_obj.send_message(custom_commands[msg.message_text.strip()], chatid)

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

