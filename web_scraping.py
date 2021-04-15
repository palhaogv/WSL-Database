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









