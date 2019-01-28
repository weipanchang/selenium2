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

    def __init__(self, stock_name, group, downloadPath):
#    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
        print "Get stock performance data: " + stock_name.upper() 
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
        driver.set_page_load_timeout(70)    


        url2 =  "https://finance.yahoo.com/quote/" + stock_name.upper() +"?p=" + stock_name.upper() + "&.tsrc=fin-srch"
        try:
            driver.get(url2)
        except TimeoutException:
            pass
    
        print "Page is loaded"
#        driver.maximize_window()
        time.sleep(10)
        
        # url = "https://finance.yahoo.com"       
        # stock_elm = driver.find_element_by_xpath("//input[@placeholder='Search for news, symbols or companies']")
        # stock_elm.send_keys(stock_name.upper())
        # stock_elm.send_keys(Keys.RETURN)        

        print "Processing " + self.stock_name.upper() +" Annual Total Return (%) History"
        elm = driver.find_element_by_xpath("//*[text()='Performance']")
#        elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/section/div/ul/li[7]/a/span")
        print "click at Performance Button"
        elm.click()
        time.sleep(20)
        
        print "locate Annual Total Return (%) History"
#        /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]
        performance_elm = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div")
#        /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div
#        /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]
        #/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[2]
        # /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div
        # /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[2]
        # /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[2]
        # /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[2]/span[1]
        # /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[2]/span[3]
#        child_elms_list = performance_elm.find_elements_by_tag_name("span")

        file_write = open( downloadPath + "/"+ stock_name + "_performance" + ".csv","w")
        for child_elm in performance_elm:
            child_span_elm_list  = child_elm.find_elements_by_tag_name("span")
            line = child_span_elm_list[0].text + "," + child_span_elm_list[2].text + "," + group + "\n"
            file_write.write(line)
#            print child_span_elm_list[0].text, child_span_elm_list[2].text

#         time.sleep(10)

        file_write.close()
        time.sleep(2)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
    group  = 'Large-Cap Blend'
    stock_list = ["vmrgx", "vwusx", "vigax", "trbcx", "ftqgx", "msegx", "ialax", "acfox"]
    for i in stock_list:
        get_stock_data = get_historical_data(i, group, downloadPath)
#    get_stock_data = get_historical_data("VHDYX", downloadPath)
#    get_stock_data = get_historical_data("VLCAX", downloadPath)

if __name__ == "__main__":
    main()
