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
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

class get_historical_data():

    def __init__(self, stock_name, startDate, endDate, downloadPath):
#    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
        self.startDate = startDate
        self.endDate = endDate
        print "Get stock history data: " + stock_name.upper() + "   from " + startDate + " to " + endDate
        self.downloadPath = downloadPath
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", downloadPath)
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
        driver.set_page_load_timeout(60)    
        #url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
        url = "https://finance.yahoo.com"

        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
#        driver.maximize_window()
        time.sleep(1)
#        //*[@id="search-button"]
        stock_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/form/table/tbody/tr/td[1]/div/div/div[1]/input")
        stock_elm.send_keys(stock_name.upper())
        stock_elm.send_keys(Keys.RETURN)
#        stock_search_elm = driver.find_element_by_xpath("//*[@id='search-button']")
        time.sleep(5)
        print "Processing " + self.stock_name.upper() +" stock history data"

        
    #   close buy sell dialog box if presented
#/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div[2]
#/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button
#/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button
#/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[3]/div[2]/div[3]/div/div/button
#/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button
#        button_elm_lists = driver.find_elements_by_tag_name("button")
#        for button_elm in button_elm_lists:
        try:
#                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
#            button_elm = driver.find_element_by_xpath("//button[@class = 'Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
            button_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[3]/div/div/button")
            print "click at x button"
            button_elm.click()
            time.sleep(1)
#           break
        except:
            pass

#        elm = driver.find_element_by_xpath("//span[contains(text(), 'Historical Data')]")
#        elm = elm = driver.find_element_by_xpath ("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/section/div/ul/li[9]/a/span[text()='Historical Data']")

        elm = driver.find_element_by_xpath ("//span[contains(text(), 'Historical Data')]")
        print "click at Historical Data Button"
        elm.click()
        time.sleep(5)
        len_of_input_elm = 0
        
        while len_of_input_elm < 5:
            input_elm_lists = driver.find_elements_by_tag_name("input")
            len_of_input_elm = len(input_elm_lists)

        time.sleep(5)
        
        input_elm = input_elm_lists[4]
        print "click at input button"
        input_elm.click()
        time.sleep(1)
        
        elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
        print "click at max"
        elm.click()
        time.sleep(1)
        
#/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/input[1]
#/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/input[2]
#/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/div[3]/button[1]
#/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/div[3]/button[2]
        
#        elm = driver.find_element_by_name("endDate")
        elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/input[2]")
        endDate_default =  elm.get_attribute("value")
        endDate1 = time.strptime(endDate_default , "%m/%d/%Y")
        elm = driver.find_element_by_name("startDate")
        startDate_default =  elm.get_attribute("value")
        startDate1 = time.strptime(startDate_default , "%m/%d/%Y")
        startDate2 = time.strptime(startDate , "%m/%d/%Y")
        if (startDate1 < startDate2) and (endDate1 > startDate2):
            print "Input startDate: " + startDate
            elm.clear()
            elm.send_keys(startDate)
        else:
            print "Out of data range! Will display maximum possible data range with using default date as input: " + startDate_default
        time.sleep(5)
        
        elm = driver.find_element_by_name("endDate")
#        endDate_default =  elm.get_attribute("value")
        endDate1 = time.strptime(endDate_default , "%m/%d/%Y")
        endDate2 = time.strptime(endDate , "%m/%d/%Y")
#        print (endDate1 > endDate2) and (StartDate1 < endDate2)
        if (endDate1 > endDate2) and (startDate1 < endDate2):
            print "Input endDate: " + endDate
            elm.clear()
            elm.send_keys(endDate)
        else:
            print "Out of data range! Will display maximum possible data range with using default date as input: " + endDate_default
        time.sleep(5)

        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)' ]")
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
        time.sleep(2)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
 
    # get_stock_data = get_historical_data("amzn",  downloadPath)
    # get_stock_data = get_historical_data("adbe",  downloadPath)
    # get_stock_data = get_historical_data("aapl",  downloadPath)
    # get_stock_data = get_historical_data("goog",  downloadPath)       

    startDate = '6/28/2005'
    endDate = '6/28/2017'
#    stock_name = raw_input("Please enter the Stock Symbol:   ")
#    get_stock_data = get_historical_data(stock_name, startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("amzn", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("adbe", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("aapl", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("goog", startDate, endDate, downloadPath)
 #   get_stock_data = get_historical_data("flws", startDate, endDate, downloadPath)
    stock_name = raw_input("Please enter the Stock Symbol:   ")
    while 1:
        while 1:
            try:
                startDate = raw_input("Please enter the Start Date (mm/dd/yyyy):   ")
                input_date = time.strptime(startDate, "%m/%d/%Y" )
                break
            except:
                print "Invalid Date, please input again!" + '\n'
        while 1:
            try:
                endDate = raw_input("Please enter the end Date (mm/dd/yyyy):   ")
                input_date = time.strptime(endDate, "%m/%d/%Y" )
                break
            except:
                print "Invalid Date, please input again!" + '\n'
        if (time.strptime(startDate, "%m/%d/%Y" ) <= time.strptime(endDate, "%m/%d/%Y" )):
            break
        else:
            print "'Start' date must be prior to 'End' date! Please Re-enter the Start Date and End Date" + '\n'
    get_stock_data = get_historical_data(stock_name, startDate, endDate, downloadPath)

if __name__ == "__main__":
    main()
