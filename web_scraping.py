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

        while True:
            #Gets all the waves scores on the page as list.
            self.waves =  self.driver.find_elements_by_xpath('//*[@class="score"]')


            #Gets the number of surfers and heats on the round, such as the avg surfers per heat (must be 2 or 3)
            self.number_of_surfers = int(len(self.waves)/18)

            #As the final round only has 1 heat, the find_element_by_class_name gets a 'WebDriver' element and not a list
            try:
                self.number_of_heats = len(self.driver.find_element_by_class_name('new-heat-hd-name'))
            except:
                self.number_of_heats = 1
                
            self.surfers_per_heat = int(self.number_of_surfers / self.number_of_heats)

            #there's a count to deduct 1 stage and gets the round name for each round.
            self.count = 0
            #Gets the stats for each heat
            self.heat_data = []
            for g in range(0, self.number_of_heats):
                #Gets the round's name
                self.round = self.driver.find_elements_by_xpath('//*[@class="carousel-item-title-wrap"]')[len(self.driver.find_elements_by_xpath('//*[@class="carousel-item-title-wrap"]')) - (self.count + 1)].text
                self.count += 1
                #Page stats
                #Event stats
                self.event_turn = self.driver.find_element_by_class_name('event-meta-tour-info').text.split()[2][1:]
                self.event_period = self.driver.find_element_by_class_name('event-schedule__date-range').text
                self.event_name = self.driver.find_element_by_class_name('event-title').text.split('\n')[0]
                self.event_local = re.split(r'(\d+)', self.driver.find_element_by_class_name('event-meta-tour-info').text)[2]
                self.avg_wave_score = re.split(r'(\d+\.\d+)',self.driver.find_element_by_class_name('new-heat-hd-status').text)[1]
                
                #Heat's id for the database
                self.heat_id = f'heat{g + 1}' + self.round + self.event_turn + self.event_period[len(self.event_period):len(self.event_period)-4]
                

                #Surfer stats
                
                self.surfer1 = self.driver.find_elements_by_xpath('//*[@class="athlete-name"]')[g*2].text
                self.surfer1_nat = self.driver.find_elements_by_xpath('//*[@class="athlete-country-flag"]')[g*2].get_attribute('title')
                
                self.surfer1_best_w1 = self.waves[g*18+(1-1)].text
                self.surfer1_best_w2 = self.waves[g*18+(2-1)].text
                self.surfer1_total = self.waves[g*18+(3-1)].text
                self.surfer1_w01 = self.waves[g*18+(4-1)].text
                self.surfer1_w02 = self.waves[g*18+(5-1)].text
                self.surfer1_w03 = self.waves[g*18+(6-1)].text
                self.surfer1_w04 = self.waves[g*18+(7-1)].text
                self.surfer1_w05 = self.waves[g*18+(8-1)].text
                self.surfer1_w06 = self.waves[g*18+(9-1)].text
                self.surfer1_w07 = self.waves[g*18+(10-1)].text
                self.surfer1_w08 = self.waves[g*18+(11-1)].text
                self.surfer1_w09 = self.waves[g*18+(12-1)].text
                self.surfer1_w10 = self.waves[g*18+(13-1)].text
                self.surfer1_w11 = self.waves[g*18+(14-1)].text
                self.surfer1_w12 = self.waves[g*18+(15-1)].text
                self.surfer1_w13 = self.waves[g*18+(16-1)].text
                self.surfer1_w14 = self.waves[g*18+(17-1)].text
                self.surfer1_w15 = self.waves[g*18+(18-1)].text

                #Surfer 2 stats
                self.surfer2 = self.driver.find_elements_by_xpath('//*[@class="athlete-name"]')[g*2+1].text
                self.surfer2_nat = self.driver.find_elements_by_xpath('//*[@class="athlete-country-flag"]')[g*2+1].get_attribute('title')

                self.surfer2_best_w1 = self.waves[g*18+(19-1)].text
                self.surfer2_best_w2 = self.waves[g*18+(20-1)].text
                self.surfer2_total = self.waves[g*18+(21-1)].text
                self.surfer2_w01 = self.waves[g*18+(22-1)].text
                self.surfer2_w02 = self.waves[g*18+(23-1)].text
                self.surfer2_w03 = self.waves[g*18+(24-1)].text
                self.surfer2_w04 = self.waves[g*18+(25-1)].text
                self.surfer2_w05 = self.waves[g*18+(26-1)].text
                self.surfer2_w06 = self.waves[g*18+(27-1)].text
                self.surfer2_w07 = self.waves[g*18+(28-1)].text
                self.surfer2_w08 = self.waves[g*18+(29-1)].text
                self.surfer2_w09 = self.waves[g*18+(30-1)].text
                self.surfer2_w10 = self.waves[g*18+(31-1)].text
                self.surfer2_w11 = self.waves[g*18+(32-1)].text
                self.surfer2_w12 = self.waves[g*18+(33-1)].text
                self.surfer2_w13 = self.waves[g*18+(34-1)].text
                self.surfer2_w14 = self.waves[g*18+(35-1)].text
                self.surfer2_w15 = self.waves[g*18+(36-1)].text  
                
                #Inputing all variables into the heat_data list
                self.heat_data.append(self.heat_id)
                self.heat_data.append(self.event_name)
                self.heat_data.append(self.event_local)
                self.heat_data.append(self.event_turn)
                self.heat_data.append(self.event_period)
                self.heat_data.append(self.avg_wave_score)
                self.heat_data.append(self.surfer1)
                self.heat_data.append(self.surfer1_nat)
                self.heat_data.append(self.surfer1_best_w1)
                self.heat_data.append(self.surfer1_best_w2)
                self.heat_data.append(self.surfer1_total)
                self.heat_data.append(self.surfer1_w01)
                self.heat_data.append(self.surfer1_w02)
                self.heat_data.append(self.surfer1_w03)
                self.heat_data.append(self.surfer1_w04)
                self.heat_data.append(self.surfer1_w05)
                self.heat_data.append(self.surfer1_w06)
                self.heat_data.append(self.surfer1_w07)
                self.heat_data.append(self.surfer1_w08)
                self.heat_data.append(self.surfer1_w09)
                self.heat_data.append(self.surfer1_w10)
                self.heat_data.append(self.surfer1_w11)
                self.heat_data.append(self.surfer1_w12)
                self.heat_data.append(self.surfer1_w13)
                self.heat_data.append(self.surfer1_w14)
                self.heat_data.append(self.surfer1_w15)
                self.heat_data.append(self.surfer2)
                self.heat_data.append(self.surfer2_nat)
                self.heat_data.append(self.surfer2_best_w1)
                self.heat_data.append(self.surfer2_best_w2)
                self.heat_data.append(self.surfer2_total)
                self.heat_data.append(self.surfer2_w01)
                self.heat_data.append(self.surfer2_w02)
                self.heat_data.append(self.surfer2_w03)
                self.heat_data.append(self.surfer2_w04)
                self.heat_data.append(self.surfer2_w05)
                self.heat_data.append(self.surfer2_w06)
                self.heat_data.append(self.surfer2_w07)
                self.heat_data.append(self.surfer2_w08)
                self.heat_data.append(self.surfer2_w09)
                self.heat_data.append(self.surfer2_w10)
                self.heat_data.append(self.surfer2_w11)
                self.heat_data.append(self.surfer2_w12)
                self.heat_data.append(self.surfer2_w13)
                self.heat_data.append(self.surfer2_w14)
                self.heat_data.append(self.surfer2_w15)
                print(self.heat_data)
            
            #self.driver.get(self.driver.find_element_by_xpath('//*[@class="previous"]').get_attribute('href'))
            








