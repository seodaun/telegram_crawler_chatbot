
from menu_content import *
class MenuAction:
    def __init__(self):
        self.keyboard = None
        self.button_tag = None
        self.query = None
        self.keyboard_dict = {"melon_key":melon_keyboard(),
                              "naver_key":naver_keyboard()}
    def title_meun_action(self,bot,update):
        self.query = update.callback_query
        if  self.query.data =='melon' or self.query.data =='naver':
            self.button_tag = self.query.data
            self.keyboard = self.keyboard_dict[self.button_tag+"_key"]
        if self.button_tag == 'google' or self.button_tag == 'melon' or self.button_tag == 'naver': #타이틀버튼 눌렀을 경우
            if self.button_tag == 'melon': melon_menu(bot, update)
            if self.button_tag == 'naver': naver_menu(bot, update)
            bot.edit_message_text(self.query.data, chat_id=self.query.message.chat_id,
                                  message_id=self.query.message.message_id,
                                  reply_markup=self.keyboard)
        if self.query.data == 'exit':
            bot.edit_message_text(chat_id=self.query.message.chat_id,
                                  message_id=self.query.message.message_id,
                                  text='종료 중..')
        return
