import requests
import bs4
import re
import pandas as pd
url = 'https://steamcommunity.com/app/215080/reviews/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

regex = re.compile('apphub_CardContentAuthorName')

ds = pd.DataFrame(columns=['title', 'hours', 'content' ,  'author'])
for x in range(1, 99):
    offset = (x*10) - 10

    payload = {
    'userreviewsoffset': offset,
    'p': x,
    'workshopitemspage': x,
    'readytouseitemspage': x,
    'mtxitemspage': x,
    'itemspage': x,
    'screenshotspage': x,
    'videospage': x,
    'artpage': x,
    'allguidepage': x,
    'webguidepage': x,
    'integratedguidepage': x,
    'discussionspage': x,
    'numperpage': '10',
    'browsefilter': 'toprated',
    'browsefilter': 'toprated',
    'l': 'english',
    'appHubSubSection': '10',
    'filterLanguage': 'default',
    'searchText': '',
    'forceanon': '1'}



    response = requests.get(url, headers=headers, params=payload)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('div',{'class':'apphub_Card modalContentLink interactable'})
    for card in cards:
        title = card.find('div',{'class':'title'}).text
        hours = card.find('div',{'class':'hours'}).text
        content = card.find('div',{'class':'apphub_CardTextContent'}).text.strip()
        author = card.find('div',{'class':regex}).text
        List= [title, hours, content, author]
        ds.append(List)
        