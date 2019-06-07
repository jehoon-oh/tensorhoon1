from bs4 import BeautifulSoup
import requests

class Wiki:
    def __init__(self, url):
        base_url = url
        con = requests.get(base_url)
        soup = BeautifulSoup(con.content, 'html.parser')
        #print(soup)
        infoTable = soup.find('table', {'class' : 'wikitable sortable'})
        result = []
        for a in infoTable.find_all('tr'):
            infolist = []
            for b in a.find_all('td'):
                info = b.get_text()
                infolist.append(info)
            result.append(infolist)
        print(result)