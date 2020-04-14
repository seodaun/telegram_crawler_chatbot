from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_menu_keyboard():
    keyboard = [[InlineKeyboardButton("멜론", callback_data='melon')],
                [InlineKeyboardButton("네이버", callback_data='naver')],
                 [InlineKeyboardButton('종료', callback_data='exit')]]
    return InlineKeyboardMarkup(keyboard)
def melon_keyboard():
    keyboard = [[InlineKeyboardButton("top 10", callback_data='melon_top_10')],
                [InlineKeyboardButton("최신곡", callback_data='melon_new_song')],
                [InlineKeyboardButton('종료', callback_data='exit')]]
    return InlineKeyboardMarkup(keyboard)
def naver_keyboard():
    keyboard = [[InlineKeyboardButton("실시간 급상승 검색어", callback_data='naver_search_word')],
                [InlineKeyboardButton("네이버 웹툰 인기 급상승 만화", callback_data='naver_webtoon_top')],
                [InlineKeyboardButton('종료', callback_data='exit')]]
    return InlineKeyboardMarkup(keyboard)
