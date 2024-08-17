import requests
from bs4 import BeautifulSoup

domain = 'http://www.google.com/search?q='
search = 'Top companies in manufacturing sector in Asia'
response = requests.get(domain+search)
soup = BeautifulSoup(response.content, 'html.parser')

elm = [x['href'][x['href'].find('https'):] for x in soup.select('a') if '/url?q=' in x['href']]

for e in elm:
    print('Main URL',e)
    response = requests.get(e)
    soup = BeautifulSoup(response.content, 'html.parser')

    url = [x['href'] for x in soup.select('a') if x.has_attr('href') and 'https' in x['href']]
    print('Sub URL', url)

