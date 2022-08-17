import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


# 순위 body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 제목 body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수 body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    a = music.select_one('td.info')
    rank = music.select_one('td.number').text[0:2].strip()
    title = a.select_one('a.title.ellipsis').text.strip()
    # 19금 노래는 따로 찾아서 strip을 한번 더 해주고 다시 씌워주기
    if title.find('19금') != -1:
        title = title.replace('19금','').strip()
        title = '[19금] ' + title
    artist = a.select_one('a.artist.ellipsis').text
    print(rank, title, artist)