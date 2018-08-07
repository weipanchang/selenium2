#!/usr/bin/env python

#import MySQLdb
import requests, urllib3, sys
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
import time

def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

class PingShow_test(unittest.TestCase):
     def setUp(self):
          self.url =  "http://99.43.90.10/login_page"
          # create a new Firefox session
          self.driver = webdriver.Firefox()
          self.driver.implicitly_wait(30)
  #        self.driver.maximize_window()
          # navigate to the application home page
          self.driver.get(self.url)
 
     def test_log_on(self):
         # get the search textbox
         
          elm_lists = self.driver.find_elements_by_tag_name("a")
          for elm in elm_lists:
#              print elm.get_attribute('href'), elm.text
               if elm.get_attribute('href') == "http://99.43.90.10/login_page/login.php":
                    elm.click()
                    self.url = elm.get_attribute('href')
#                    print self.url
                    time.sleep(5.5)
                    break
#          self.driver.get(self.url)
          self.assertIn('Login', self.driver.title)
#          time.sleep(5.5)
#         self.driver.get(self.url)
          username = self.driver.find_element_by_id("username")
          password = self.driver.find_element_by_id("password")
          username.send_keys("tester")
          password.send_keys("tester")
          # login_attempt = self.driver.find_element_by_xpath("//*[@type='submit']")
          # login_attempt.submit()
          login_attempt = self.driver.find_element_by_name("Submit")
          login_attempt.submit()
          time.sleep(5.5)
          elm_lists = self.driver.find_elements_by_tag_name("a")
          for elm in elm_lists:
#               print elm.get_attribute('href'), elm.text
               if elm.get_attribute('href') == "http://99.43.90.10/login_page/Airecenter_member.php":
                    elm.click()
                    self.url = elm.get_attribute('href')
#                    print self.url
                    time.sleep(5.5)
                    break
          
#          print self.driver.current_url
          self.assertIn('AireTcenter Member Data Check', self.driver.title)
          for model in ['acmdtv', 'acmq106','acmq109', \
                        'acwebrtcax92', 'acwebrtccycle', 'acsm8s94','acsm8sac', \
                        'acme1gd','acm2006']:
               uuid = self.driver.find_element_by_name("uuid")
               uuid.send_keys(model)
               submit = self.driver.find_element_by_xpath("//input[@value='Submit']")
               submit.submit()
               time.sleep(10.5)
               source = self.driver.page_source
               soup = BeautifulSoup(source, "html.parser")
     #          soup = soup_maker(self.url)
               rows_total = soup.find("table", border=1).find("tbody").find_all("tr")
               row =[k for k in rows_total if (k.has_attr('style') == False)]
               # if model == 'acmdtv54e4bddc7361':
               #      for k in rows:
               #           print k
               print 'Total rows for ' + model + ' = ' + str(len(row) - 1)
          # for row in rows:
          #      cells = row.find_all("td")
          #      rn = cells[0].get_text()
     def tearDown(self):
          # close the browser window
          self.driver.quit()
          
if __name__ == '__main__':
    unittest.main()          