import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


#Begin Chrome Driver Connection
service = Service("/Documents/WebDev/geckodriver")
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://tweetdeck.twitter.com")
time.sleep(5)

USER_NAME = "bigslattunchai1"
PASSWORD = "Guibsjks5768"

USE = "ethetheth000"
PASS = "naptaj-9hocdy-Tyrcaw"


PERSON = "XCOPYART"



def logging():

    log_in_click = driver.find_element(By.CSS_SELECTOR,".r-1kb76zh > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
    log_in_click.click()
    time.sleep(10)

    log_in = driver.find_element(By.CSS_SELECTOR, '.r-30o5oe')
    log_in.send_keys(USE)
    time.sleep(2)

    next_button = driver.find_element(By.CSS_SELECTOR,'div.css-18t94o4:nth-child(6) > div:nth-child(1)')
    next_button.click()
    time.sleep(3)

    password_in = driver.find_element(By.CSS_SELECTOR, '.r-homxoj')
    time.sleep(3)
    password_in.send_keys(PASS)
    time.sleep(2)
    password_in.send_keys(Keys.ENTER)
    time.sleep(100)



def scrolll_1():

    sidebar = driver.find_element(By.CSS_SELECTOR,
                                  "div.r-cpa5s6:nth-child(1) > section:nth-child(1)")
    driver.execute_script("arguments[0].scrollTop += 500;", sidebar)
    #sidebar_height = sidebar.size["height"]
    #driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
    time.sleep(5)


def scrolll_2():
    sidebar = driver.find_element(By.CSS_SELECTOR,
                                  "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-5swwoo.r-13qz1uu.r-417010 > main > div > div > div > div:nth-child(2)")
    driver.execute_script("arguments[0].scrollTop += 500;", sidebar)
    # sidebar_height = sidebar.size["height"]
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
    time.sleep(5)


def scrolll_3():
    sidebar = driver.find_element(By.CSS_SELECTOR,
                                  "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-5swwoo.r-13qz1uu.r-417010 > main > div > div > div > div:nth-child(3)")
    driver.execute_script("arguments[0].scrollTop += 500;", sidebar)
    # sidebar_height = sidebar.size["height"]
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sidebar)
    time.sleep(5)

logging()

while True:

    scrolll_1()
    #scrolll_2()
    #scrolll_3()
    time.sleep(30)