from time import sleep        
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get('https://www.crunchbase.com/organization/wetpaint?utm_source=odm_C7D54DA4E16142F4A5BE76114AE527E0.csv&utm_medium=export&utm_campaign=dataset')
driver.set_window_position(0, 0)
driver.set_window_size(100000, 200000)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5) 

soup = BeautifulSoup(driver.page_source)
funding_rounds = soup.find_all("div", class_="funding_rounds")
for div in funding_rounds:
    if div.div["class"] not in 'card-header':
        for ul in div.ul:
            print(ul.li.div.h4.span.contents)
