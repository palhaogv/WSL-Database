import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import pandas as pd
from httplib2 import Http
from selenium import webdriver
import time
from random import randint, random
import pandas as pd
import re

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

        
        

        #for link in self.events_link:
        self.driver.get(self.events_link[0])

        #Page stats
        #Event stats
        self.event_name = self.driver.find_element_by_class_name('event-title').text.split('\n')[0]
        self.event_local = re.split(r'(\d+)', self.driver.find_element_by_class_name('event-meta-tour-info').text)[2]
        self.event_turn = self.driver.find_element_by_class_name('event-meta-tour-info').text.split()[2][1:]
        self.event_period = self.driver.find_element_by_class_name('event-schedule__date-range').text
        self.heat_name = self.driver.find_elements_by_xpath('//*[@class="carousel-item-title-wrap"]')[len(self.driver.find_elements_by_xpath('//*[@class="carousel-item-title-wrap"]')) - 1].text + self.driver.find_element_by_class_name('new-heat-hd-name').text
        self.avg_wave_score = re.split(r'(\d+\.\d+)',self.driver.find_element_by_class_name('new-heat-hd-status').text)[1]
        print(f'The events name is: {self.event_name}')
        print(f'The local name is: {self.event_local}')
        print(f'The turn is: {self.event_turn}')
        print(f'The events period is: {self.event_period}')
        print(f'The events heat is: {self.heat_name}')
        print(f'The events avg score is: {self.avg_wave_score}')
        #Surfer 1 stats
        self.surfer1 = self.driver.find_elements_by_xpath('//*[@class="athlete-name"]')
        self.surfer1_nat = self.driver.find_elements_by_xpath('//*[@class="athlete-country-flag"]')
        for i in range(0, len(self.surfer1)): print(f'Surfer {i+1}: {self.surfer1[i].text}')
        for i in range(0, len(self.surfer1_nat)): print(f'Surfer {i+1} nationality: {self.surfer1_nat[i].get_attribute("title")}')
        
        '''self.surfer1_best_w1 = self.driver.find_elements_by_xpath('//a[@class="score"]')[0].text
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
        self.surfer2 = self.driver.find_elements_by_xpath('//a[@class="athlete-name"]')[1].text
        self.surfer2_nat = self.driver.find_elements_by_xpath('//a[@class="athlete-country-flag"]')[1].text
        self.surfer2_best_w1 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_best_w2 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_total = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w01 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w02 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w03 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w04 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w05 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w06 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w07 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w08 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w09 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w10 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w11 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w12 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w13 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w14 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text
        self.surfer2_w15 = self.driver.find_elements_by_xpath('//a[@class="score"]')[1].text        
        print(f'The turn name is: {self.event_turn}')
        print(f'The events end date is: {self.event_end_date}')
        print(f'The events heat name is: {self.heat_name}')
        print(f'The events avg score is: {self.avg_wave_score}')
        print(f'The events surfer 1 is: {self.surfer1}')
        print(f'The events surfer 1 nationality is: {self.surfer1_nat}')
        print(f'The events surfer 2 is: {self.surfer2}')
        print(f'The events surfer 2 nationality is: {self.surfer2_nat}')
        print(f'Score number{x}: {i} in the class store' for x, i in self.driver.find_elements_by_xpath('//a[@class="score"]'))'''





