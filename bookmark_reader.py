import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from main import logging,get_driver,scrool

BOOKMARKS = []

def get_bookmark():

    time.sleep(5)
    Posts = driver.find_elements(By.CSS_SELECTOR, "article")

    for post in Posts:
        print(post.text)



driver = get_driver()
logging()
time.sleep(3)
driver.get("https://twitter.com/i/bookmarks")

while True:
    get_bookmark()
    scrool()