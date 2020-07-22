import requests
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver
import time


chromedriver = 'D:\\SD_python\\django\\django-project\\project\\chromedriver\\chromedriver.exe'

with sqlite3.connect('./matchdb.sqlite3') as con:
    cur = con.cursor()
    cur.execute("select * from matches")
    infos = cur.fetchall()

# print(infos)
codes = []
for i in infos:
    code = i[3]
    codes.append(code)

base_url = 'https://www.premierleague.com/match/'

driver = webdriver.Chrome(chromedriver)
all_matches = []
for code in codes[1:3]:

    url = base_url + code
    time.sleep(1)
    driver.get(url)

    # match_date = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]').text
    # referee = driver.find_element_by_class_name('referee').text
    
    # home_club = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
    # away_club = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text
    
    # time.sleep(1)
    # lineUp = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[1]/div/div/ul/li[2]')
    # lineUp.click()
    
    # home_formation = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/header/div/strong').text
    # away_formation = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/header/div/strong').text


    # # home line up
    # home_Goalkeeper = []
    # home_Goalkeeper.append(driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/div/ul[1]/li/a/div[2]/span[1]').text)

    # home_Defenders = []
    # defenders = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/div/ul[2]')
    # for de in defenders:
    #     defender = de.text
    #     defender = defender.split('\n')
    #     home_Defenders.append(defender)
    
    # home_Midfielders = []
    # mid = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/div/ul[3]')
    # for m in mid:
    #     midfielder = m.text
    #     midfielder = midfielder.split('\n')
    #     home_Midfielders.append(midfielder)
    
    # home_Forward = []
    # foward = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/div/ul[4]/li')
    # for st in foward:
    #     striker = st.text
    #     striker = striker.split('\n')
    #     home_Forward.append(striker)
    
    # home_Substitutes = []
    # sub = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[1]/div/div/ul[5]/li')
    # for su in sub:
    #     subp = su.text
    #     subp = subp.split('\n')        
    #     home_Substitutes.append(subp)


    # # away line up
    # away_Goalkeeper = []
    # away_Goalkeeper.append(driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/div/ul[1]/li/a/div[2]/span[1]').text)

    # away_Defenders = []
    # defenders = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/div/ul[2]')
    # for de in defenders:
    #     defender = de.text
    #     defender = defender.split('\n')
    #     away_Defenders.append(defender)

    # away_Midfielders = []
    # mid = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/div/ul[3]')
    # for m in mid:
    #     midfielder = m.text
    #     midfielder = midfielder.split('\n')
    #     away_Midfielders.append(midfielder)
    
    # away_Forward = []
    # foward = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/div/ul[4]/li')
    # for st in foward:
    #     striker = st.text
    #     striker = striker.split('\n')
    #     away_Forward.append(striker)
    
    # away_Substitutes = []
    # sub = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[2]/div/div/div[3]/div/div/ul[5]/li')
    # for su in sub:
    #     subp = su.text
    #     subp = subp.split('\n')        
    #     away_Substitutes.append(subp)

    # HOME = [match_date, referee, home_club, home_formation, home_Goalkeeper, home_Defenders, home_Midfielders, home_Forward, home_Substitutes]
    # AWAY = [match_date, referee, away_club, away_formation, away_Goalkeeper, away_Defenders, away_Midfielders, away_Forward, away_Substitutes]
    time.sleep(1)
    stat_tab = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[1]/div/div/ul/li[3]')
    stat_tab.click()

    home_stat = []
    away_stat = []


    time.sleep(1)
    
    homePossession = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]')
    for i in homePossession:
        home_stat.append(i.text)

    awayPossession = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[3]')
    for j in awayPossession:
        away_stat.append(i.text)

    homeShotOnTarget = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[2]/td[1]')
    for shot in homeShotOnTarget:
        home_stat.append(shot)



    

#     match = [HOME, AWAY]
#     all_matches.append(match)

# for i in all_matches:
#     print(i)


    

    





# with sqlite3.connect('./matchdb.sqlite3') as con:
#     cur = con.cursor()
#     home = ""
#     away = ""
#     competition = ""
#     match_id = ""
#     stadium = ""

#     for link in links:
#         home = link.get_attribute("data-home")
#         away = link.get_attribute("data-away")
#         competition = link.get_attribute("data-competition")
#         match_id = link.get_attribute("data-comp-match-item")
#         stadium = link.get_attribute("data-venue").strip("<strong>")
#         stadium = stadium.strip("</strong>")
#         stadium = stadium.replace("<strong>", "")


#         cur.execute("INSERT INTO "+ table +" (home, away, competition, match_id, stadium) VALUES (?,?,?,?,?)", (home, away, competition, match_id, stadium))
#     con.commit()

