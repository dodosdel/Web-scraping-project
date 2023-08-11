import requests
from bs4 import BeautifulSoup
from qalampir_uz import Qalampir_uz

# source = requests.get('https://qalampir.uz/uz/post/category-ajax?id=3&limit=10&offset=1').text

# soup = BeautifulSoup(source, 'lxml')

# news_link = soup.find('div', class_ = 'col-lg-4 col-md-6')
# p_txt = ' '.join([p.text for p in news_link.find_all('a')])
# print(news_link)


n = int(input("N ta maqola: "))
url = f'https://qalampir.uz/uz/post/category-ajax?id=3&limit={n}&offset=1'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div_elements = soup.find_all('div', class_='col-lg-4 col-md-6')

href_values = []
for div_element in div_elements:
    a_tags = div_element.find_all('a', href=True)
    for a_tag in a_tags:
        href_values.append('https://qalampir.uz' + a_tag['href'])


for i in range(n):
    scrape = Qalampir_uz.text(href_values[i])
    print('\n\n\n' + scrape)
