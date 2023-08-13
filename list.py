import time
import datetime
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import pyttsx3
from main import logging,get_driver,scrool


TWEET = {
    "Tweeter" : "",
    "Tweet":"",
    "Quoted":"",
    "Comments_Stat": 0,
    "Retweets_Stat": 0,
    "Like_Stat": 0,
    "Seen_Stat": 0
}

driver = get_driver()
logging()

All_List = driver.get("https://twitter.com/Tugrunn222/lists")
time.sleep(5)


Trugoy_List = driver.get("https://twitter.com/i/lists/1660934875439067136")
time.sleep(5)

def text_to_speech():
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

def All_Post():

    Posts = driver.find_elements(By.CSS_SELECTOR,"article")
    for post in Posts:
        print(post.text)
        #print(dir(post))
        print("\n \n \n")



def gettweeter():

    tweeter = driver.find_element(By.CSS_SELECTOR,"div.r-1jgb5lz:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
    print(tweeter.text)
    TWEET["Tweeter"] = tweeter.text

    tweet = driver.find_element(By.CSS_SELECTOR,"div.r-1jgb5lz:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)")
    print(tweet.text)
    TWEET["Tweet"] = tweet.text


    try:
        quote = driver.find_element(By.CSS_SELECTOR,"div.r-1jgb5lz:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
        print(quote.text)
        TWEET["Quoted"] = quote.text
    except TimeoutError:
        print("Did not quote a tweet")



    commentstat = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[1]")
    print(commentstat.text)
    TWEET["Comments_Stat"] = commentstat.text

    retweetstat = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[2]")
    print(retweetstat.text)
    TWEET["Retweets_Stat"] = retweetstat.text

    likestat = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[3]")
    print(likestat.text)
    TWEET["Like_Stat"] = likestat.text

    seenstat = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[4]")
    print(seenstat.text)
    TWEET["Seen_Stat"] = seenstat.text

    with open(f"Credentials/{Trugoy_List}.json", "a") as file:
        json.dump(TWEET, file, indent=4)



def scroll_list():

    tweeter_list = input('Please Input the list link')
    driver.get(tweeter_list)

    while True:
        gettweeter()
        scrool()


logging()

while True:
    scrool()
    time.sleep(3)
    gettweeter()