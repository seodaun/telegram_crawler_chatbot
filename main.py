import telegram
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import logging
from command import *
from actions import *
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    menu_action = MenuAction()
    while True:
        bot = telegram.Bot(token = TOKEN)
        updater = Updater(TOKEN) # 봇의 업데이트 상황을 가져옴
        updater.dispatcher.add_handler(CommandHandler('start', start_command)) #handler를 추가하는 함수
        updater.dispatcher.add_handler(CallbackQueryHandler(menu_action.title_meun_action))
        updater.start_polling(poll_interval=0.0,
                          timeout=10,
                          clean=False,
                          bootstrap_retries=0)
        updater.idle() # updater가 종료되지 않고 계속 실행되어 있도록 하는 함수
    print("종료 되었습니다.")