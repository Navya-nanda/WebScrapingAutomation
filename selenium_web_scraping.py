from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
domain = 'http://www.google.com/search?q='
search = 'Top companies in manufacturing sector in Asia'
driver.get(domain+search)
time.sleep(5)

DOM = driver.page_source
soup = BeautifulSoup(DOM,'html.parser')

elm = [x['href'] for x in soup.select('a') if x.has_attr('href') and x['href'].startswith('https')]

for e in elm:
    print('Main URL', e)
    driver.get(e)
    time.sleep(5)
    DOM = driver.page_source
    soup = BeautifulSoup(DOM, 'html.parser')
    url = [x['href'] for x in soup.select('a') if x.has_attr('href') and 'https' in x['href']]
    print('Sub URL', url)

driver.quit()


