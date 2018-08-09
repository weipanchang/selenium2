#!/usr/bin/env python
#import re, sys
import xml.etree.ElementTree as ET
import requests, urllib3, sys
#from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver


def init_firefox(downloadPath):

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
    url = "https://finance.yahoo.com"
    try:
        driver.get(url)
    except TimeoutException:
        pass

    print "Page is loaded"
    time.sleep(1)
    return driver

def search_stock(driver, stock_name):

    stock_elm = driver.find_element_by_xpath("//input[@placeholder='Search for news, symbols or companies']")
    stock_elm.send_keys(stock_name.upper())
    stock_elm.send_keys(Keys.RETURN)
    stock_search_elm = driver.find_element_by_xpath("//*[@id='search-button']")
    time.sleep(5)
    return None

def close_pop_up(driver):
    try:

        button_elm = driver.find_element_by_xpath("//button[@class = 'Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
        print "click at x button 2"
        button_elm.click()
        time.sleep(1)
    except:
        pass

    return None

def click_historical_data(driver):

    elm = driver.find_element_by_xpath("//span[contains(text(), 'Historical Data')]")
    print "click at Historical Data Button"
    elm.click()
    time.sleep(5)
    return None

def click_time_period(driver):

    len_of_input_elm = 0

    while len_of_input_elm < 4:
        input_elm_lists = driver.find_elements_by_tag_name("input")
        len_of_input_elm = len(input_elm_lists)
    time.sleep(1)
    input_elm = input_elm_lists[4]
    print "click at input button"
    input_elm.click()
    time.sleep(1)
    return None

def click_max(driver):
    elm = driver.find_element_by_xpath("//div[@class='Ta(c) C($gray)']/span[@data-value='MAX']")
    print "click at max"
    elm.click()
    time.sleep(1)
    return None

def input_date(driver, startDate, endDate):
    print "Input start date and end date"
    elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/span[2]/div/input[2]")
    endDate_default =  elm.get_attribute("value")

    endDate1 = time.strptime(endDate_default , "%m/%d/%Y")

    elm = driver.find_element_by_name("startDate")
    startDate_default =  elm.get_attribute("value")

    startDate1 = time.strptime(startDate_default , "%m/%d/%Y")
    if startDate == "":
        startDate2 = startDate1
    else:        
        startDate2 = time.strptime(startDate , "%m/%d/%Y")
    if (startDate1 < startDate2) and (endDate1 > startDate2):
        print "Input startDate: " + startDate
        elm.clear()
        elm.send_keys(startDate)
        
    elif (startDate1 == startDate2) or (endDate1 == startDate2):
        pass
    else:
        print "Out of data range! Will display maximum possible data range with using default date as input: " + startDate_default
        
    time.sleep(2)

    elm = driver.find_element_by_name("endDate")

    endDate1 = time.strptime(endDate_default , "%m/%d/%Y")
    if endDate == "":
        endDate2 = endDate1
    else:
        endDate2 = time.strptime(endDate , "%m/%d/%Y")

    if (endDate1 > endDate2) and (startDate1 < endDate2):
        print "Input endDate: " + endDate
        elm.clear()
        elm.send_keys(endDate)
    elif (endDate1 == endDate2) or (startDate1 == endDate2):
        pass
    else:
        print "Out of data range! Will display maximum possible data range with using default date as input: " + endDate_default

    time.sleep(5)

def click_done(driver):

    button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)' ]")

    print "click at Done"
    button_elm.click()
    time.sleep(6)
    return None

def click_apply(driver):
    button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']")
    print "clikc at Apply"
    button_elm.click()
    time.sleep(10)
    return None

def click_download_link(driver):
    a_elm = driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']")
    print "click at download link"
    a_elm.click()
    time.sleep(5)
    return None


def main():

    downloadPath = '/home/wchang/Downloads/data'

    get_stock_data = get_historical_data("fb",  downloadPath)
#    # get_stock_data = get_historical_data("cost",  downloadPath)
    # get_stock_data = get_historical_data("bby",  downloadPath)
#    get_stock_data = get_historical_data("amd",  downloadPath)
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
