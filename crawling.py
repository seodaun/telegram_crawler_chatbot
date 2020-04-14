from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
from google_images_download import google_images_download

import ssl
def naver_search_word():
    sw = []
    web_url = "http://www.naver.com"
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        roll = soup.find("div",{'class':'ah_roll_area'})
        sw = roll.find("ul").find_all("li")
        sw = [i.find("a").find("span",{"class":"ah_k"}).text for i in sw]
        return sw
def naver_webtoon_top10():
    sw = []
    web_url = "https://comic.naver.com/index.nhn"
    with urllib.request.urlopen(web_url) as response:  # respose 에 값을 저장
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')  # 파싱해
        roll = soup.find('div', {'class': 'asideBox'})
        for tag in roll.select('#realTimeRankFavorite li a'):
            sw.append(tag['title'])
        return sw
def melon_top_10():
    sw=[]
    web_url = "https://www.melon.com/"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get("https://www.melon.com/", headers=header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
    roll = parse.find('div', {'class': 'wrap_chart_tab'}).find('div', {'class': 'list_wrap'})
    item = roll.find('ul')
    for i in item.select('.song a'):
        sw.append(i['title'])
    return sw

def melon_new():
    sw=[]
    web_url = "https://www.melon.com/"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get("https://www.melon.com/new/index.htm", headers=header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
    roll = parse.find('div', {'class': 'service_list_song'}).find('tbody')
    item = roll.find_all('div',{'class':'wrap_song_info'})
    sw = [i.find("a").text for i in item]
    return sw
