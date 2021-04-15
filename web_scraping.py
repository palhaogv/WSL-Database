import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import pandas as pd
from httplib2 import Http
from selenium import webdriver
import time
from random import randint, random
import pandas as pd

class Web_scraping:
    def __init__(self):
        '''Initialize the application'''
        self.driver = webdriver.Edge('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe')

    def games_link(self):
        '''Create a list with all season event's link and then create another list with all event's link'''
        #Creating list with the all season's link
        self.season_pages_list = []
        for y in range(2008, 2022):
            #Creating the seasons links as str and adding it to a list
            self.season_link = 'https://www.worldsurfleague.com/events/' + str(y) + '/mct?all=1'
            self.season_pages_list.append(self.season_link)

        #Creating a list with the all event's link from each season
        self.events_link_list = []
        for link in self.season_pages_list:
            self.driver.get(link)
            #Getting all the events links as selenium format
            self.event_links = self.driver.find_elements_by_xpath('//a[@class="event-schedule-details__event-name"]')
            #Finding the class status completed is needed once it's possible to stop the process on it.
            self.event_status = self.driver.find_elements_by_xpath('//span[@class="event-status event-status--completed"]')

            #Creating event's link list
            for i in range(0, len(self.event_status)):
                #Getting the links for each event as a str format
                self.link_attribute = self.event_links[i].get_attribute('href')
                self.events_link_list.append(self.link_attribute)
                
        with open('events.txt', 'w') as f:
            for item in self.events_link_list:
                f.write("%s\n" % item)
        
        print('FINISHED')
    
    #Getting data inside which event
    def event_stats(self):
        #TXT file with all events link to list
        self.events_link = [line[0] for line in pd.read_fwf('events.txt', header=None).values.tolist()]

        
        

        for link in self.events_link:
            self.driver.get(link)

            #Page stats
            #Event stats
            self.event_name = self.driver.find_elements_by_xpath('//a[@class="event-title"]')[0].text
            self.event_local = self.driver.find_elements_by_xpath('//a[@class="event-meta-tour-info"]')[0].text
            self.event_turn = self.driver.find_elements_by_xpath('//a[@class="event-meta-tour-info"]')[1].text
            self.event_end_date = self.driver.find_elements_by_xpath('//a[@class="local-time"]')[0].text
            self.heat_name = self.driver.find_elements_by_xpath('//a[@class="carousel-item-title"]')[0].text + self.driver.find_elements_by_xpath('//a[@class="new-heat-hd-name"]')[0].text
            self.avg_wave_score = self.driver.find_elements_by_xpath('//a[@class="new-heat-hd-status"]')[0].text
            #Surfer 1 stats
            self.surfer1 = self.driver.find_elements_by_xpath('//a[@class="athlete-name"]')[0].text
            self.surfer1_nat = self.driver.find_elements_by_xpath('//a[@class="athlete-country-flag"]')[0].text
            self.surfer1_best_w1 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_best_w2 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_total = self.driver.find_elements_by_xpath('//a[@class="wave wave-total"]')[0].text
            self.surfer1_w01 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w02 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w03 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w04 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w05 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w06 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w07 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w08 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w09 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w10 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w11 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w12 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w13 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w14 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            self.surfer1_w15 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
            #Surfer 2 stats
            self.surfer2 = ''
            self.surfer21_nat = ''
            self.surfer2_best_w1 = ''
            self.surfer2_best_w2 = ''
            self.surfer2_total = ''
            self.surfer2_w01 = ''
            self.surfer2_w02 = ''
            self.surfer2_w03 = ''
            self.surfer2_w04 = ''
            self.surfer2_w05 = ''
            self.surfer2_w06 = ''
            self.surfer2_w07 = ''
            self.surfer2_w08 = ''
            self.surfer2_w09 = ''
            self.surfer2_w10 = ''
            self.surfer2_w11 = ''
            self.surfer2_w12 = ''
            self.surfer2_w13 = ''
            self.surfer2_w14 = ''
            self.surfer2_w15 = ''





