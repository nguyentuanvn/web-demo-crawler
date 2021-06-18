from bs4 import BeautifulSoup
import requests
import re
from collections import Counter

class Article(): 
    def __init__(self, url):
        self.top_image = None
        self.title = None
        self.date = None
        self.author = None
        self.related = {}
        self.words_dict = {}
        self.craw(url)

    def craw(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            self.top_image = soup.find('img', attrs={'itemprop': 'contentUrl'})["data-src"]
            self.title = soup.find('h1', 'title-detail').text
            self.date = soup.find('span', 'date').text
            self.author = soup.find('p', attrs={'style': 'text-align:right;'}).text
            box_related = soup.find('ul', attrs={'data-campaign': 'Box-Related'})
            self.related = {obj['title']: obj['href'] for child in box_related.children for obj in child if obj.has_attr('href')}
            txt = "".join([paragraph.text for paragraph in soup.find_all('p', 'Normal')])
            txt = re.sub('[\s",;.]', ' ', txt)
            words = re.split("\s+", txt.strip())
            words = [word.upper() for word in words]
            self.words_dict = dict(Counter(words).most_common()[:5])
        except:
            pass