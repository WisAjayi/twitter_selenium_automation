import random
from random import choice, randint, shuffle
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


USER_NAME = "your_username"
PASSWORD = "your_Password"
SEARCH = "search_name"
Follower_List = []



service = Service("/Documents/WebDev/geckodriver")
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://www.twitter.com")
time.sleep(5)



def logging():

    log_in_click = driver.find_element(By.CSS_SELECTOR,"div.r-1ydw1k6:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
    log_in_click.click()
    time.sleep(5)

    log_in = driver.find_element(By.CSS_SELECTOR, 'div label div div div input')
    log_in.send_keys(USER_NAME)
    time.sleep(2)

    next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    next_button.click()
    time.sleep(3)

    password_in = driver.find_element(By.CSS_SELECTOR, '[name=password]')
    time.sleep(3)
    password_in.send_keys(PASSWORD)
    time.sleep(2)
    password_in.send_keys(Keys.ENTER)
    time.sleep(3)

    #Skip_Notification = driver.find_element(By.CSS_SELECTOR,"div.r-1ets6dv:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
    #Skip_Notification.click()
    #time.sleep(3)



def search():
    Search_Bar = driver.find_element(By.CSS_SELECTOR, '.r-30o5oe')
    Search_Bar.send_keys(SEARCH)
    time.sleep(3)
    Artist_Click = driver.find_element(By.CSS_SELECTOR,"#typeaheadDropdown-1 > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
    Artist_Click.click()
    time.sleep(5)



def scrool():
    driver.execute_script("window.scrollBy(0, 500)")


def get_driver():
    return driver


logging()
