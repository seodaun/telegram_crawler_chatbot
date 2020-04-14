import json
import requests
TOKEN = '1198846529:AAGAYG7_Xxc9xe2ySMZt13EP-QNftQYn_4I'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
def check_id(bot, update): #아이디 확인
    try:
        id = update.message.chat.id
        print('Chat ID: ', id)
        return id
    except:
        id = update.channel_post.chat.id
        return id
def check_nickname(bot, update): #닉네임 확인
    try:
        nickname = update.message.from_user.first_name
        print('Chat NickName: ', nickname)
        return nickname
    except:
        nickname = update.channel_post.from_user.first_name
        return nickname


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    print('a')
    if offset:
        url += "&offset={}".format(offset)
        print('b')
    js = get_json_from_url(url)
    print(js)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)
def get_last_update_text(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)
def main():
    run = True
    last_update_id = None
    while run:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            num_updates = len(updates["result"])
            last_update = num_updates - 1
            text = updates["result"][last_update]["message"]["text"]
            run = False
            return text