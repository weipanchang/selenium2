#!/usr/bin/env python
# import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
# from bs4 import BeautifulSoup
# import unittest
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
import time
# from bs4 import BeautifulSoup as bs
from selenium import webdriver

class get_historical_data():

    #def __init__(self, stock_name, startDate, endDate, downloadPath):
    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
#        self.startDate = startDate
#        self.endDate = endDate
#        print "Get stock history data: " + stock_name.upper() + "   from " + startDate + " to " + endDate
#        print "Get all stock history data: " + self.stock_name.upper()
        print ""
        print "Processing " + self.stock_name.upper() +" stock history data"
        self.downloadPath = downloadPath
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", self.downloadPath)
        profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        profile.set_preference("browser.download.manager.focusWhenStarting", False)
        profile.set_preference("browser.download.manager.useWindow", False)
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        profile.set_preference("browser.download.manager.closeWhenDone", False)
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        desiredCapabilities = DesiredCapabilities.FIREFOX.copy()
        desiredCapabilities['firefox_profile'] = profile.encoded
        driver = webdriver.Firefox(capabilities=desiredCapabilities)
        driver.implicitly_wait(10) # seconds
        driver.set_page_load_timeout(20)    
#        url = "https://finance.yahoo.com/quote/" + self.stock_name + "?p=" + self.stock_name + "&.tsrc=fin-srch"
        url = "https://finance.yahoo.com"
        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
        time.sleep(1)
#        /html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[1]/div/div/div[1]/input
        stock_elm = driver.find_element_by_xpath("//input[@placeholder='Search for news, symbols or companies']")
        
        stock_elm.send_keys(stock_name.upper())
        stock_elm.send_keys(Keys.RETURN)
        stock_search_elm = driver.find_element_by_xpath("//*[@id='search-button']")
        time.sleep(5)
#        print "Processing " + self.stock_name.upper() +" stock history data"    
#       close buy sell dialog box if presented
    
        # button_elm_lists = driver.find_elements_by_tag_name("button")
        #         
        # for button_elm in button_elm_lists:
        #     try:
        #         if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
        #             button_elm.click()
        #             print "click at X button 1"
        #             break
        #     except:
        #         pass

        try:
#                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
            button_elm = driver.find_element_by_xpath("//button[@class = 'Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
#            button_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button")
            print "click at x button"
            button_elm.click()
            time.sleep(1)
#           break
        except:
            pass            
#         try:
#                 if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
#             button_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div[2]/div[3]/div/div/button")
#             print "click at x button"
#             button_elm.click()
#                 break
#         except:
#             pass            
        
#        elm_lists = driver.find_elements_by_tag_name("span")
#        i = -1
#        for elm in elm_lists:
            
#            try:        
#                i = i + 1
#                print i
#                if elm.text == "Historical Data":
#        elm = driver.find_element_by_xpath ("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/section/div/ul/li[9]/a")
        elm = driver.find_element_by_xpath("//span[contains(text(), 'Historical Data')]")    
        print "click at Historical Data Button"
        elm.click()
        time.sleep(5)
        len_of_input_elm = 0

        while len_of_input_elm < 5:
            input_elm_lists = driver.find_elements_by_tag_name("input")
            len_of_input_elm = len(input_elm_lists)
        time.sleep(1)
        input_elm = input_elm_lists[4]
#                         if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":

        print "click at input button"
        input_elm.click()
        time.sleep(1)
        
        elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
        print "click at max"
        elm.click()
        time.sleep(1)
#                    button_elm_lists = driver.find_elements_by_tag_name("button")
#                    for button_elm in button_elm_lists:
        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)' ]")
         #       if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
        print "click at Done"
        button_elm.click()
        time.sleep(6)                

        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']")
        print "clikc at Apply"
        button_elm.click()
        time.sleep(10)

        a_elm = driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']")
        print "click at download link"

        a_elm.click()
        time.sleep(10)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
 
    #get_stock_data = get_historical_data("amzn",  downloadPath)
    #get_stock_data = get_historical_data("adbe",  downloadPath)
    get_stock_data = get_historical_data("aapl",  downloadPath)
    get_stock_data = get_historical_data("goog",  downloadPath)
    get_stock_data = get_historical_data("wmt",  downloadPath)
    get_stock_data = get_historical_data("amzn",  downloadPath)
    get_stock_data = get_historical_data("qai",  downloadPath)
    get_stock_data = get_historical_data("bby",  downloadPath)
    get_stock_data = get_historical_data("amd",  downloadPath)
    # get_stock_data = get_historical_data("box",  downloadPath)
    # get_stock_data = get_historical_data("fb",  downloadPath)
    # get_stock_data = get_historical_data("smci",  downloadPath)      

    # startDate = '6/28/2005'
    # endDate = '6/28/2018'
    # get_stock_data = get_historical_data("amzn", startDate, endDate, downloadPath)
    # get_stock_data = get_historical_data("adbe", startDate, endDate, downloadPath)
    # get_stock_data = get_historical_data("aapl", startDate, endDate, downloadPath)
    # get_stock_data = get_historical_data("goog", startDate, endDate, downloadPath)     

if __name__ == "__main__":
    main()
