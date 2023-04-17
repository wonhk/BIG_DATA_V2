import requests
from bs4 import BeautifulSoup

def melon_list():
    s_list = list()
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers = headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    chart = soup.select("table > tbody > tr")


    idx = 0
    for song in chart[:100]:
        idx += 1
        rank = song.select_one("div.wrap.t_center span.rank").text
        title = song.select_one("div.ellipsis.rank01 a").text
        artist = song.select_one(" div > div.ellipsis.rank02 > a").text
        print(f"{idx}위 {title} - {artist}")

    return s_list

