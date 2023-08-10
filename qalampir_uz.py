from bs4 import BeautifulSoup
import requests

class Qalampir_uz:
    def __init__(self):
        pass
        

    def text(url):
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        title = soup.find('div', class_ = 'title').h1.text
        news_type  = soup.find('div', class_ = 'content-main-hero-info content-main-hero-info-top').p.text
        content_div = list(soup.find_all('div', class_ = 'col-12'))[4]
        p_txt = ' '.join([p.text for p in content_div.find_all('p')])
        date_div = soup.find('div', 'content-main-hero-info content-main-hero-info-top')
        date_publish = date_div.find('p', class_ = 'right').text.split('visibility')[0]
        try: 
            li_txt = ' '.join([li.text for li in content_div.find_all('li')])
        except: 
            pass
        img_source = soup.find('div', class_ = 'source_post').img['src']
    
        return news_type  + " . " +  p_txt + li_txt + img_source +' ' +  date_publish
        
    

obj = Qalampir_uz.text('https://qalampir.uz/uz/news/k-irgizistonda-davlat-tilida-efir-yuritmagan-telekanallar-zharimaga-tortildi-87929')
print(obj)

