import requests
import re
import datetime
from pymongo import MongoClient
import pymongo
from selenium import webdriver
import time


chromedriver = 'D:\\SD_python\\django\\django-project\\project\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

searchurl = 'https://www.premierleague.com/results'
time.sleep(1)

driver.get(searchurl)
time.sleep(1)
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")        

while True:
    # Scroll down to bottom                                                     
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)                                             
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);") 
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height           
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height, new_height)

    if new_height == last_height:                                               
        break

    last_height = new_height


# match_date = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[1]/div[3]/section/time[263]/strong')
match_results = driver.find_elements_by_class_name('fixtures__matches-list')



client = MongoClient('localhost', 27017)

db = client.EPL
collection = db.match_results

for match in match_results:
    date = match.get_attribute('data-competition-matches-list')
    links = match.find_elements_by_class_name('matchFixtureContainer')

    for link in links:
        home = link.get_attribute("data-home")
        away = link.get_attribute("data-away")
        competition = link.get_attribute("data-competition")
        match_id = link.get_attribute("data-comp-match-item")
        stadium = link.get_attribute("data-venue").strip("<strong>")
        stadium = stadium.strip("</strong>")
        stadium = stadium.replace("<strong>", "")
        
    match = {
        'Match_id' : match_id,
        'Date': date,
        'Home' : home,
        'Away' : away,
        'Competition' : competition,
        'Stadium' : stadium
    }

    game_id = collection.insert_one(match)


all_match = collection.find()

for i in all_match:
    print(i)
