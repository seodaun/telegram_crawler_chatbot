from keyboard import *
from utill import *

def start_command(bot, update):
    id = check_id(bot, update)
    nickname = check_nickname(bot, update)
    bot.send_message(chat_id=id, text="안녕하세요 " + nickname +"! crawlingbot입니다!\n\n")
    update.message.reply_text('무엇을 하고 싶으신가요?', reply_markup=start_menu_keyboard())