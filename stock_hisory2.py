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

    def __init__(self, stock_name, startDate, endDate, downloadPath):
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
        # profile.set_preference("browser.download.manage.timeouts.pageLoadTimeout", 10)
        # profile.set_preference("http.response.timeout", 5)
        # profile.set_preference("dom.max_script_run_time", 5)
        # profile.set_preference("webdriver.load.strategy", "fast")
        profile.set_preference("browser.download.manager.closeWhenDone", False)
#        desiredCapabilities = DesiredCapabilities.FIREFOX.copy()
        desiredCapabilities = DesiredCapabilities.FIREFOX
        desiredCapabilities["pageLoadStrategy"] = "normal"
        desiredCapabilities['firefox_profile'] = profile.encoded
        driver = webdriver.Firefox(capabilities=desiredCapabilities)
        driver.set_page_load_timeout(15)
        url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
        try:
            driver.get(url)
        except TimeoutException:
            pass

        print "Page is loaded"
        time.sleep(1)

    #   close buy sell dialog box if presented

        button_elm_lists = driver.find_elements_by_tag_name("button")
        for button_elm in button_elm_lists:
            try:
                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
                    button_elm.click()
                    break
            except:
                pass

        elm_lists = driver.find_elements_by_tag_name("span")
        for elm in elm_lists:
            try:
                if elm.text == "Historical Data":
                    print "click at Historical Data Button"
                    elm.click()
                    time.sleep(1)
                    len_of_input_elm = 0

                    while len_of_input_elm < 5:
                        input_elm_lists = driver.find_elements_by_tag_name("input")
                        len_of_input_elm = len(input_elm_lists)

                    for input_elm in input_elm_lists:
                         if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":

                             print "click at input button"
                             input_elm.click()
                             time.sleep(5)

                             # elm = driver.find_element_by_name("startDate")
                             # print "Input startDate"
                             # elm.clear()
                             # elm.send_keys(startDate)
                             # 
                             # elm = driver.find_element_by_name("endDate")
                             # print "Input endDate"
                             # elm.clear()
                             # elm.send_keys(endDate)
                             break
                             
                    elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
                    print "click at max"
                    elm.click()
                   
                    for button_elm in button_elm_lists:
                            if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
                                print "Click at Done"
                                button_elm.click()
                                time.sleep(6)
                                break                    
#                    break
                    for input_elm in input_elm_lists:
                         if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":

                             print "click at input button"
                             input_elm.click()
                             time.sleep(5)

                             # elm = driver.find_element_by_name("startDate")
                             # print "Input startDate"
                             # elm.clear()
                             # elm.send_keys(startDate)
                             # 
                             # elm = driver.find_element_by_name("endDate")
                             # print "Input endDate"
                             # elm.clear()
                             # elm.send_keys(endDate)
                             break
                             
                    elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
                    print "click at max"
                    elm.click()
#                    break                
                    
                    button_elm_lists = driver.find_elements_by_tag_name("button")
                    for button_elm in button_elm_lists:
                            if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
                                print "Click at Done"
                                button_elm.click()
                                time.sleep(6)
                                break
            except:
                pass
     #   Click at Apply
        button_elm_lists = driver.find_elements_by_tag_name("button")
        for button_elm in button_elm_lists:
            if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)":
                print "Clikc at Apply"
                button_elm.click()
                time.sleep(1)
                break
        a_elm_lists = driver.find_elements_by_tag_name("a")
        for a_elm in a_elm_lists:
            if a_elm.get_attribute("class") == "Fl(end) Mt(3px) Cur(p)":
                print "click at download link"
                # url = a_elm.get_attribute('href')
                # print url
                a_elm.click()
                break
    #    driver.get(url)
    #    driver.find_element(By.LINK_TEXT, 'smilechart.xls').click()
        time.sleep(2)
        driver.quit()

def main():
    startDate = '6/28/2005'
    endDate = '6/28/2018'
    downloadPath = '/home/wchang/Downloads/data'

    get_stock_data = get_historical_data("amzn", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("adbe", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("aapl", startDate, endDate, downloadPath)
#    get_stock_data = get_historical_data("goog", startDate, endDate, downloadPath)

if __name__ == "__main__":
    main()
