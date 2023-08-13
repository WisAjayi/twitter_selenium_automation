from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup
import requests

#Begin Chrome Driver Connection
service = Service("/Documents/WebDev/chromedriver")
service.start()
driver = webdriver.Remote(service.service_url)

#Twitter Login Info
driver.get("https://twitter.com/i/flow/login")
time.sleep(2)
user_name = "coin_ctrl"
password = "Mistermightycontroller"
comments = ["Dammyyy", "Lovelyyy", "Haha"]
random.shuffle(comments)

def login():
    log_in = driver.find_element(By.CSS_SELECTOR, 'div label div div div input')
    log_in.send_keys(user_name)
    time.sleep(2)
    next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    next_button.click()
    time.sleep(3)
    password_in = driver.find_element(By.CSS_SELECTOR, '[name=password]')
    time.sleep(3)
    password_in.send_keys(password)
    time.sleep(2)
    password_in.send_keys(Keys.ENTER)
    time.sleep(3)


def get_post():
    print("Enter Post URL")
    x = input()
    post = driver.get(x)
    time.sleep(3)

def comment_wreck():
    for comment in comments:
        comment_select = driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block')
        comment_select.click()
        time.sleep(2)
        comment_select.send_keys(comment)
        reply = driver.find_element(By.CSS_SELECTOR, "div.r-42olwf:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
        reply.click()
        time.sleep(10)

login()
get_post()



