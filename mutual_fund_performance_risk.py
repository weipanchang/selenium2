#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
import string
#import urllib2
import requests, urllib3, sys
# from bs4 import BeautifulSoup
# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import WebDriverWait
import time
# from bs4 import BeautifulSoup as bs
from selenium import webdriver

class wait_for_text_to_start_with(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).text
            return element_text.startswith(self.text)
            
        except StaleElementReferenceException:
            return False

class get_fund_data():

    def __init__(self, fund, downloadPath):
#    def __init__(self, stock_name, downloadPath):
        self.fund = fund
        print "Geting fund data: " + fund.upper() 
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
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(20)    
        def map_catagory(n):
            return ("Large-Cap Value" , "Large-Cap Blend", "Large-Cap Growth", "Mid-Cap Value", "Mid-Cap Blend", "Mid-Cap Growth", "Small-Cap Value", "Small-Cap Blend", "Small-Cap Growth")[n]

        url2 =  "https://finance.yahoo.com/quote/" + fund.upper() +"?p=" + fund.upper() + "&.tsrc=fin-srch"
        try:
            driver.get(url2)
        except TimeoutException:
            pass
    
        print "Page is loaded"
        time.sleep(3)
        
#       Summary Section
        print "click at Summary Button"        
        elm = driver.find_element_by_xpath("//*[text()='Summary']")
        elm.click()

#       Risk Section
        print "Processing " + self.fund.upper() +" risk information"  
        risk = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/span").text
        time.sleep(3)

        elm = driver.find_element_by_xpath("//*[text()='Risk']")
        print "click at Risk Button"
        elm.click()
        time.sleep(3)        

        file_write = open( downloadPath + "/risk/"+ fund + "_risk" + ".csv","w")
        line = ""
        for i in range(2,8):
            parm_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div/div[" + str(i) +"]/div[1]/span")
            parm = parm_elm.text
            value_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div/div[" + str(i) + "]/div[4]/span[1]")
            value =  value_elm.text
            line = line + (parm + "," + value + "\n")
        line = line +"Morning Star Rating" + "," + risk + "\n"
        file_write.write(line)    
        file_write.close()
        
        print "Processing " + self.fund.upper() +" Annual Total Return (%) History"
        print "click at Performance Button"
        
        elm = driver.find_element_by_xpath("//*[text()='Performance']")
        elm.click()
        time.sleep(2)
        print "locate Annual Total Return (%) History"

        WebDriverWait(driver, 5).until(wait_for_text_to_start_with((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div[1]/span[4]/span'), "Category"))
        performance_elm = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[3]/div/div")
        line = ""
        file_write = open( downloadPath + "/performance/"+ fund + "_performance" + ".csv","w")
        for child_elm in performance_elm:
            child_span_elm_list  = child_elm.find_elements_by_tag_name("span")
            line = child_span_elm_list[0].text + "," + child_span_elm_list[2].text + "\n"
            file_write.write(line)
        file_write.close()
        time.sleep(1)
        
        print "Processing " + self.fund.upper() +" Profile"
        print "click at profile Button"
        profile_elm = driver.find_element_by_xpath("//*[text()='Profile']")
        profile_elm.click()
#        time.sleep(50)
        
        WebDriverWait(driver, 10).until(wait_for_text_to_start_with((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/h3/span'), "Fund Overview"))
        fund_name_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[1]/div[1]/div[1]/p[1]")
        fund_name =  fund_name_elm.text

        inception = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[7]/span[2]/span").text
        img_elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[1]/div[2]/div[3]")
        img_elm.click()
        time.sleep(2)
        
        print "get fund summary"
        print "get fund investment style."
        img = img_elm.find_element_by_tag_name("img").get_attribute('src')
        style = map_catagory(int(img[-5]))
        
        category = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[1]/span[2]").text
        ytd_return = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[4]/span[2]").text
        yeld = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[5]/span[2]").text
        line = ""       
        line = self.fund + "," + fund_name + "," + inception + ","  + style + "," + category + "," + ytd_return + "," + yeld + "\n"
        file_write = open( self.downloadPath + "/profile/" + self.fund + "_profile.csv","w")
                
        file_write.write(line)
        file_write.close()
        time.sleep(1)        

        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
    
#    alpha_beta_list = list(string.ascii_uppercase)
    alpha_beta_list = ["K"]
    for a in alpha_beta_list:
        with open(downloadPath + "/list/fund_list_" + a + ".csv", "r") as fr:
            for line in fr:
                line = line.split(",")
                print ""
                print "=============="
                print line[0]
                fund_data = get_fund_data(line[0], downloadPath)                
                
    # fund_list = ["vgstx"]
    # 
    # for i in fund_list:
    #     fund_data = get_fund_data(i, downloadPath)

if __name__ == "__main__":
    main()
