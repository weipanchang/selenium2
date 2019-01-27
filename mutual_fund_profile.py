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

import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

class get_profile_data():

    def __init__(self, fund, downloadPath):

        self.fund = fund
        print "Prossing: " + fund
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
        driver.set_page_load_timeout(30)
        
        def map_catagory(n):
            return ("Large-Cap Value" , "Large-Cap Blend", "Large-Cap Growth", "Mid-Cap Value", "Mid-Cap Blend", "Mid-Cap Growth", "Small-Cap Value", "Small-Cap Blend", "Small-Cap Growth")[n]

        url =  "https://finance.yahoo.com/quote/" + self.fund +"?p=" + self.fund + "&.tsrc=fin-srch"
#        url = "https://www.morningstar.com/funds/xnas/" + fund + "/quote.html"
        try:
            driver.get(url)
        except TimeoutException:
            pass
    
        print "Page is loaded"
        time.sleep(3)
        profile_elm = driver.find_element_by_xpath("//*[text()='Profile']")
        print "click at profile Button"
        profile_elm.click()
        time.sleep(3)

        fund_name_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[1]/div[1]/div[1]/p[1]")
        fund_name =  fund_name_elm.text
        print fund_name
        
        inception = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[7]/span[2]/span").text
        print inception
        
        img_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[1]/div[2]/div[3]")
        img_elm.click()
        time.sleep(3)
        img = img_elm.find_element_by_tag_name("img").get_attribute('src')
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq1.gif":
        #     category = "Large-Cap Value" 
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq2.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq3.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq4.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq5.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq6.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq7.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq8.gif":
        #     category = "Large-Cap Value"
        # if img == "http://us.i1.yimg.com/us.yimg.com/i/fi/3_0stylelargeeq9.gif":
        #     category = "Large-Cap Value"

        style = map_catagory(int(img[-5]))
        print style
        
        category = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[1]/span[2]").text
        print category
        
        # ytd_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/div[2]/div[1]/div/div[4]")
        # ytd_elm.click()
        # time.sleep(3)
        
        ytd_return = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[4]/span[2]").text
        print ytd_return
#        /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[4]/span[2]
        yeld = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[5]/span[2]").text
        print yeld        
        
        
        line = self.fund + "," + fund_name + "," + inception + ","  + style + "," + category + "," + ytd_return + "," + yeld + "\n"
        file_write = open( self.downloadPath + "/profile/" + self.fund + "_profile.csv","w")
                
        file_write.write(line)
        file_write.close()
        time.sleep(1)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
#    alpha_beta_list = list(string.ascii_uppercase)
    alpha_beta = 'Y'
    file_read = open(downloadPath + "/list/fund_list" + "_" + alpha_beta +".csv","r")
    
    with open(downloadPath + "/list/fund_list" + "_" + alpha_beta +".csv","r") as fp:
#        line = fp.readline()
        for line in fp:
 #           line = file_read.readline()
            line = line.rstrip()
            line_split = line.split(',')
            get_profile_data(line_split[0], downloadPath)
#    file_read.close()
if __name__ == "__main__":
    main()
