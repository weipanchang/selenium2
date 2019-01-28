#!/usr/bin/env python
import re
import string
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

    def __init__(self, alpha_beta, downloadPath):

        self.alpha_beta = alpha_beta
        print "Prossing: " + alpha_beta 
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

        url =  "https://www.marketwatch.com/tools/mutual-fund/list/" + self.alpha_beta
        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
        time.sleep(5)
        
#       /html/body/div[2]/div[3]/div[2]/table/tbody
        elm = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/table/tbody")

        time.sleep(5)
        
        symb_elm = elm.find_elements_by_class_name("quotelist-symb")
        name_elm = elm.find_elements_by_class_name("quotelist-name")
        file_write = open( downloadPath + "/list/fund_list" + "_" + alpha_beta +".csv","w")
        for i in range(1, len(symb_elm)):
            symb = symb_elm[i].find_element_by_tag_name("a").text
            name = name_elm[i].find_element_by_tag_name("a").text
#            print symb, name
            line = symb + "," + name + "\n"
            file_write.write(line)
        file_write.close()
        time.sleep(1)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'

    alpha_beta_list = list(string.ascii_uppercase)
    
    for i in alpha_beta_list:
        get_stock_data = get_historical_data(i, downloadPath)

if __name__ == "__main__":
    main()
