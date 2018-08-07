#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
from bs4 import BeautifulSoup
#import unittest
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

import time
#from bs4 import BeautifulSoup as bs
#from selenium import webdriver

class get_historical_data():

    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
        print "Get stock history data: " + stock_name.upper()
        self.downloadPath = downloadPath
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.download.folderList", 2)
        self.profile.set_preference("browser.download.manager.showWhenStarting", False)
        self.profile.set_preference("browser.download.dir", downloadPath)
        self.profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        self.profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.profile.set_preference("browser.download.manager.focusWhenStarting", False)
        self.profile.set_preference("browser.download.manager.useWindow", False)
        self.profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        self.profile.set_preference("browser.download.manager.closeWhenDone", False)
        self.profile.set_preference("browser.cache.disk.enable", False)
        self.profile.set_preference("browser.cache.memory.enable", False)
        self.profile.set_preference("browser.cache.offline.enable", False)
        self.profile.set_preference("network.http.use-cache", False)
        self.desiredCapabilities = DesiredCapabilities.FIREFOX.copy()
        self.desiredCapabilities['firefox_profile'] = self.profile.encoded
        driver = webdriver.Firefox(capabilities=self.desiredCapabilities)
        driver.set_page_load_timeout(60)    
        #url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
        url = "https://www.nasdaq.com"

        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
#        driver.maximize_window()
        time.sleep(1)
#        //*[@id="search-button"]
        stock_elm = driver.find_element_by_xpath("//*[@id='stock-search-text']")
        stock_elm.send_keys(stock_name.upper())
        time.sleep(90)    # get_stock_data = get_historical_data("adbe",  downloadPath)

        try:
# #                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
            button_elm = driver.find_element_by_xpath("//*[@id='cookieConsentOK']")
#             button_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button")
            print "click at x button"
            button_elm.click()
            time.sleep(10)
# #           break
        except:
            pass

        stock_elm.send_keys(Keys.RETURN)
#        stock_search_elm = driver.find_element_by_xpath("//*[@id='search-button']")
        time.sleep(20)
        print "Processing " + self.stock_name.upper() +" stock history data"

        driver.maximize_window()


#        elm = driver.find_element_by_xpath("//span[contains(text(), 'Historical Data')]")
#        elm = elm = driver.find_element_by_xpath ("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/section/div/ul/li[9]/a/span[text()='Historical Data']")

        elm = driver.find_element_by_xpath ("//*[@id='historical_quoteslink']")
        
        print "click at Historical Data Button"
        try:
            elm.click()
        except TimeoutException:
            pass

        time.sleep(5)

        driver.find_element_by_xpath("//select[@name='ddlTimeFrame']/option[@value='8y']").click()
        # input_elm = input_elm_lists[4]
        # print "click at input button"
        # input_elm.click()
        time.sleep(20)
        # body = driver.find_element_by_css_selector('body')
        # body.send_keys(Keys.PAGE_DOWN)
        tableDiv =  driver.find_element_by_xpath("//*[@id='historicalContainer']")
        tableRows =  tableDiv.find_elements_by_tag_name("tr")
        print len(tableRows)
#        print len(tableRows)
        for tableRow in tableRows[2:]:
            row = tuple(tableRow.text.split())
            print ('"%s",%s,%s,%s,%s,"%s"' % row)

#//*[@id="lnkDownLoad"]
        # a_elm = driver.find_element_by_xpath("//*[@id='lnkDownLoad']")
        # print "click at download link"
        # url1 = a_elm.get_attribute('href')
        # print url1
        # a_elm.click()
#        driver.get("url1")
        # url1 =  driver.current_url
        # page = requests.get(url1).text
        # soup = BeautifulSoup(page, 'lxml')
        # tableDiv = soup.find_all('div', id="historicalContainer")
        # tableRows = tableDiv[0].findAll('tr')
        # print len(tableRows)
        # for tableRow in tableRows[2:]:
        #     row = tuple(tableRow.getText().split())
        #     print ('"%s",%s,%s,%s,%s,"%s"' % row)
        # 
        print len(tableRows)
        time.sleep(5)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
 
    get_stock_data = get_historical_data('aapl', downloadPath)
#    get_stock_data = get_historical_data("adbe",  downloadPath)
#    get_stock_data = get_historical_data("aapl",  downloadPath)
    # get_stock_data = get_historical_data("goog",  downloadPath)
    # get_stock_data = get_historical_data("wmt",  downloadPath)
    # get_stock_data = get_historical_data("cost",  downloadPath)
    # get_stock_data = get_historical_data("bby",  downloadPath)
    # get_stock_data = get_historical_data("amd",  downloadPath)
    # get_stock_data = get_historical_data("box",  downloadPath)
    # get_stock_data = get_historical_data("fb",  downloadPath)
    # get_stock_data = get_historical_data("smci",  downloadPath)      

if __name__ == "__main__":
    main()
    
# import requests
# from bs4 import BeautifulSoup
# 
# URL = 'http://www.nasdaq.com/symbol/amd/historical'
# page = requests.get(URL).text
# soup = BeautifulSoup(page, 'lxml')
# tableDiv = soup.find_all('div', id="historicalContainer")
# tableRows = tableDiv[0].findAll('tr')
# 
# for tableRow in tableRows[2:]:
#     row = tuple(tableRow.getText().split())
#     print ('"%s",%s,%s,%s,%s,"%s"' % row)    
