#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
from bs4 import BeautifulSoup
import unittest
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
from bs4 import BeautifulSoup as bs
from selenium import webdriver

class get_historical_data():

    #def __init__(self, stock_name, startDate, endDate, downloadPath):
    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
#        self.startDate = startDate
#        self.endDate = endDate
#        print "Get stock history data: " + stock_name.upper() + "   from " + startDate + " to " + endDate
#        print "Get all stock history data: " + self.stock_name.upper() 
        self.downloadPath = downloadPath
        startDate = '6/28/2005'
        endDate = '6/28/2017'
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
        driver.set_page_load_timeout(15)    
        url = "https://finance.yahoo.com/quote/" + self.stock_name + "?p=" + self.stock_name + "&.tsrc=fin-srch"
        print "Processing " + self.stock_name +" stock history data"
        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
        time.sleep(1)
    
#       close buy sell dialog box if presented
    
        button_elm_lists = driver.find_elements_by_tag_name("button")
                
        for button_elm in button_elm_lists:
            try:
                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
                    button_elm.click()
                    break
            except:
                pass
        
#       
        elm = driver.find_element_by_xpath("//span[contains(text(), 'Historical Data')]")    
#        print "click at Historical Data Button"
        elm.click()
        time.sleep(5)
        len_of_input_elm = 0

        while len_of_input_elm < 5:
            input_elm_lists = driver.find_elements_by_tag_name("input")
            len_of_input_elm = len(input_elm_lists)
        time.sleep(2)
        input_elm = input_elm_lists[4]

#        print "click at input button"
        input_elm.click()
        time.sleep(5)
        
        elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
 #       print "click at max"
        elm.click()
        time.sleep(1)

        elm = driver.find_element_by_name("startDate")
        startDate_default =  elm.get_attribute("value")
        startDate1 = time.strptime(startDate_default , "%m/%d/%Y")
        startDate2 = time.strptime(startDate , "%m/%d/%Y")
        if (startDate1 < startDate2):
            print "Input startDate: " + startDate
            elm.clear()
            elm.send_keys(startDate)
        else:
            print "Out of data range! Will use default date as input: " + startDate_default
        time.sleep(2)
        
        elm = driver.find_element_by_name("endDate")
        endDate_default =  elm.get_attribute("value")
        endDate1 = time.strptime(endDate_default , "%m/%d/%Y")
        endDate2 = time.strptime(endDate , "%m/%d/%Y")
        if (endDate1 > endDate2):
            print "Input endDate: " + endDate
            elm.clear()
            elm.send_keys(endDate)
        else:
            print "Out of data range! Will use default date as input: " + endDate_default
        time.sleep(2)

        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)' ]")
         #       if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
#        print "click at Done"
        button_elm.click()
        time.sleep(6)                

        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']")
#        print "clikc at Apply"
        button_elm.click()
        time.sleep(10)

        a_elm = driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']")
#        print "click at download link"
        print "Saving file to " + stock_name.upper() + '.csv'

        a_elm.click()

        time.sleep(10)
        driver.quit()

def main():
    print "                                                              "
    print "             Develope by William Chang 5/23/2018              "
    print "             ===================================              "
    print "             This is a ample code for demo only!              "
    print "                                                              "
    downloadPath = '~/'

    get_stock_data = get_historical_data("aapl",  downloadPath)
    get_stock_data = get_historical_data("goog",  downloadPath)
    get_stock_data = get_historical_data("smci",  downloadPath)      

if __name__ == "__main__":
    main()
