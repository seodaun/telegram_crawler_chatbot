from telegram import ForceReply
from keyboard import *
from crawling import *
def naver_menu(bot,update):
    rank = ''
    sw = []
    query = update.callback_query
    if query.data == 'naver_search_word':
        sw = naver_search_word()
    if query.data == 'naver_webtoon_top':
        sw = naver_webtoon_top10()
    if len(sw) != 0:
        for i in range(0,10):
            rank += str(i+1)+'. '+sw[i] +'\n'
        bot.send_message(message_id = query.message.message_id,
                        chat_id = query.message.chat_id,
                        text = rank,reply_markup=start_menu_keyboard())
def melon_menu(bot,update):
    rank = ''
    sw = []
    query = update.callback_query
    if query.data == 'melon_top_10':
        sw = melon_top_10()
    if query.data == 'melon_new_song':
        sw = melon_new()
    if len(sw) != 0:
        for i in range(0,len(sw)):
            rank += str(i+1)+'. '+sw[i] +'\n'
        bot.send_message(message_id = query.message.message_id,
                        chat_id = query.message.chat_id,
                        text = rank,reply_markup=start_menu_keyboard())