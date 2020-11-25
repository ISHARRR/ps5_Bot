from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from random import randint

import time

WebsiteURL = "https://www.amazon.co.uk/dp/B08H97NYGP/ref=twister_B08J4RCVXW?_encoding=UTF8&psc=1"
WebsiteURL = "https://www.amazon.co.uk/Lead-Snowkids-Compatible-Support-Ethernet-Function-Grey-HDMI-cable/dp/B07GYS426K/ref=sr_1_4?dchild=1&keywords=hdmi&qid=1606341255&sr=8-4"

ID = "availability"
unavailableMessage = "Currently unavailable."

email = '******@gmail.com'
password = '*******'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument('--user-data-dir=/Users/ishar/Library/Application Support/Google/Chrome/Profile 3')

driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get(WebsiteURL)

def amazonLogin(email, password):
    try:
        account = driver.find_element_by_id("nav-link-accountList").click()
        emailText = driver.find_element_by_id("ap_email")
        emailText.send_keys(email)
        emailText.send_keys(Keys.ENTER)
        passwordText = driver.find_element_by_id("ap_password")
        passwordText.send_keys(password)
        passwordText.send_keys(Keys.ENTER)
    except NoSuchElementException:
        driver.get(WebsiteURL)

amazonLogin(email, password)
while True:
    wait(driver, 10).until(EC.presence_of_element_located((By.ID, ID)))
    el = driver.find_element_by_id(ID)
    str1=el.text
    if(str1.find(unavailableMessage)!=-1):
        print('unavailable')
        driver.refresh()
    else:
        buy = driver.find_element_by_id("buy-now-button").click()
        try:
            confirmBuy = driver.find_element_by_id("submitOrderButtonId").click()
        except NoSuchElementException:
            try:
                passwordText = driver.find_element_by_id("ap_password")
                passwordText.send_keys(password)
                passwordText.send_keys(Keys.ENTER)
                wait(driver, 10).until(EC.presence_of_element_located((By.ID, "turbo-checkout-iframe")))
                iframe = driver.find_element_by_id("turbo-checkout-iframe")
                driver.switch_to.frame(iframe)
                turboCheckout = driver.find_element_by_id("turbo-checkout-pyo-button").click()
                print("Purchase Completed")
            except NoSuchElementException:
                wait(driver, 10).until(EC.presence_of_element_located((By.ID, "turbo-checkout-iframe")))
                iframe = driver.find_element_by_id("turbo-checkout-iframe")
                driver.switch_to.frame(iframe)
                turboCheckout = driver.find_element_by_id("turbo-checkout-pyo-button").click()
                print("Purchase Completed")
        break
