import requests
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
import time


conn = sqlite3.connect('./matchdb.sqlite3')
table = 'matches'

x = 1
while x:
    try:
        query = 'CREATE TABLE '+ table +' (home TEXT, away TEXT, competition TEXT, match_id TEXT, stadium TEXT)'
        conn.execute(query)
        conn.commit()
        x = 0
    except:
        del_query = 'DROP TABLE ' + table
        conn.execute(del_query)
        conn.commit()


conn.close()

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
links = driver.find_elements_by_class_name('matchFixtureContainer')
dates = driver.find_elements_by_class_name('fixtures__matches-list')

with sqlite3.connect('matchdb.sqlite3') as con:
    cur = con.cursor()
    home = ""
    away = ""
    competition = ""
    match_id = ""
    stadium = ""

    for link in links:
        home = link.get_attribute("data-home")
        away = link.get_attribute("data-away")
        competition = link.get_attribute("data-competition")
        match_id = link.get_attribute("data-comp-match-item")
        stadium = link.get_attribute("data-venue").strip("<strong>")
        stadium = stadium.strip("</strong>")
        stadium = stadium.replace("<strong>", "")


        cur.execute("INSERT INTO "+ table +" (home, away, competition, match_id, stadium) VALUES (?,?,?,?,?)", (home, away, competition, match_id, stadium))
    con.commit()

