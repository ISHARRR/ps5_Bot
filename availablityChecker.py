from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from sys import platform

import time
import emailAlert


print('Running...')

url = "https://www.amazon.co.uk/dp/B08H97NYGP/ref=twister_B08J4RCVXW?_encoding=UTF8&psc=1"
ID = "availability"
company = "AMAZON"
unavailableMessage = "Currently unavailable."

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
if platform == "linux" or platform == "linux2":
    driver = webdriver.Chrome(options=chrome_options)
elif platform == "darwin":
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get(url)

while True:
    el = driver.find_element_by_id(ID)
    str1=el.text
    if(str1.find(unavailableMessage)!=-1):
        pass
    else:
        emailAlert.email("PS5 AVAILABLE AT " + company)
    driver.refresh()
    time.sleep(randint(30,60))
