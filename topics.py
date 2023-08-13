from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from main import logging,get_driver,scrool
import time

TOPICS = ["$ETH","$BTC","$DOGE","NFT","$DEFI"]

driver = get_driver()
logging()



def specific_topic():
    time.sleep(3)
    driver.get("https://twitter.com/i/topics/1301229157511168001?s=12")



specific_topic()
time.sleep(3)


while True:
    scrool()
    time.sleep(2)