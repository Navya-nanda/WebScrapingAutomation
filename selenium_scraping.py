from selenium import webdriver
import numpy as np
import time


driver = webdriver.Chrome()
domain = 'http://www.google.com/search?q='
search = 'Top companies in manufacturing sector in Asia'
driver.get(domain+search)
time.sleep(5)

elm = [x.get_attribute('href') for x in driver.find_elements_by_tag_name('a') if x.get_attribute('href') is not None]

for e in elm:
    print('Main URL',e)
    driver.get(e)
    time.sleep(5)
    url = np.unique([x.get_attribute('href') for x in driver.find_elements_by_tag_name('a') if x.get_attribute('href') is not None and x.get_attribute('href').startswith('https')]).tolist()
    print('Sub URL',url)

driver.quit()
