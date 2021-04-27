#!/usr/bin/env python
#import re, sys
import xml.etree.ElementTree as ET
import requests, urllib3, sys

# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from dateutil.parser import parse

import time
import datetime
# from bs4 import BeautifulSoup as bs

class url_to_be(object):
    """An expectation for checking the current url.
    url is the expected url, which must be an exact match
    returns True if the url matches, false otherwise."""
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        return self.url == driver.current_url


class visibility_of_element_located(object):
    """ An expectation for checking that an element is present on the DOM of a
    page and visible. Visibility means that the element is not only displayed
    but also has a height and width that is greater than 0.
    locator - used to find the element
    returns the WebElement once it is located and visible
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            return _element_if_visible(_find_element(driver, self.locator))
        except StaleElementReferenceException:
            return False
        
class presence_of_element_located(object):
    """ An expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.
    locator - used to find the element
    returns the WebElement once it is located
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return _find_element(driver, self.locator)        

def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False

def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e

def _find_element(driver, by):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e

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
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(20)

    return driver

def search_stock(driver, stock_name, wait):
   delay = 0
   while True:
       url = "https://finance.yahoo.com"
       try:
           driver.get(url)
       except TimeoutException:
           pass

       print "Yahoo finance Page is loaded"

       time.sleep(1)
#       stock_elm = driver.find_element_by_xpath("//*[@id='yfin-usr-qry']")
       stock_elm = driver.find_element_by_id('yfin-usr-qry')
#       class="Bgc(t) Bd Bdrsbstart(2px)! Bdc(#b0b0b0) Bdendw(0) Bdrs(0) Bdrststart(2px)! Bxsh(n) Bxz(bb) D(b) Fz(15px) H(inh) M(0) O(0) Px(10px) W(100%) Bdc($c-fuji-blue-1-c):f Bdc(#949494):h finsrch-inpt"
       stock_elm.send_keys((stock_name.upper()) + (Keys.ENTER))
       time.sleep(2)

       if stock_name.upper() in str(driver.current_url):
           break
       else:
           print "Correct Page is not presented, will try it agein! "

def close_pop_up(driver):
   try:

        button_elm = driver.find_element_by_css_selector(".Z\(6\) > button:nth-child(3) > svg:nth-child(1)")
        print "click at x button"
        button_elm.click()
        time.sleep(1)
   except:
       pass
    
   try:
        button_elm = driver.find_element_by_xpath("//button[@class = 'Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
        print "click at x button"
        button_elm.click()
        time.sleep(1)
   except:
       pass

def click_historical_data(driver, wait):

    print "click at Historical Data Button"

    try:
        elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Historical Data')]"))).click()
    except TimeoutException:
        pass
    time.sleep(1) 
    return None

def click_time_period(driver):

    input_elm = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")
    print "click at input button"
    input_elm.click()
    time.sleep(1)
    return None

def click_max(driver):

#    elm = driver.find_element_by_xpath("//li[4]/button[@data-value='MAX']")
    elm =  driver.find_element_by_xpath("//span[contains(text(), 'Max')]")
    print "click at max"
    elm.click()
    time.sleep(1)
#    elm= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/button")
    elm =  driver.find_element_by_xpath("//span[contains(text(), 'Apply')]")
    elm.click()
    return None

def get_max_period(driver):
    input_elm = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")
    print "fatch max period"
    max_period = input_elm.text.encode('ascii','ignore')
    print max_period
    [start_max, end_max] = [str(parse(i))[:10] for i in max_period.split("-")]
#    print start_max
#    print end_max
    time.sleep(1)
    return [start_max, end_max]

def input_date(driver, startDate, endDate, start_max, end_max):
    print "Input start date and end date"
    input_elm = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")
    print "click at input button"
    input_elm.click()

    if startDate == "":
        startDate = start_max
        print "using IPO date as start date input: " + end_max
    else:        
        startDate = str(datetime.datetime.strptime(startDate, "%m/%d/%Y").date())
#        print startDate

    if endDate == "":
        endDate = end_max
        print "using cueent date as end date input: " + end_max
    else:
        endDate = str(datetime.datetime.strptime(endDate, "%m/%d/%Y").date())
#        print endDate
        
    if (startDate > start_max) and (end_max > startDate):

        print "Input startDate: " + startDate
        elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/input")
        elm.click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        elm.send_keys(Keys.ARROW_LEFT)
        elm.send_keys(Keys.ARROW_LEFT)
        elm.send_keys(Keys.ARROW_LEFT)

        startDateList = startDate.split("-")
#        print startDateList

        actions = ActionChains(driver)
        actions.send_keys(startDateList[1])
        actions.perform()
        actions.send_keys(startDateList[2])
        actions.perform()
        actions.send_keys(startDateList[0])
        actions.perform()
         
    elif (startDate == start_max) or (end_max == startDate):
        pass
    else:
        print "Out of data range! Will display maximum possible data range with using default date as input: " + start_max
        
    time.sleep(1)
    print "Input endDate: " + endDate
    if (end_max > endDate) and (start_max < endDate):
#        print "Input endDate: " + endDate
        elm = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/input")
        elm.click()
        time.sleep(1)

        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        elm.send_keys(Keys.ARROW_LEFT)
        elm.send_keys(Keys.ARROW_LEFT)
        elm.send_keys(Keys.ARROW_LEFT)

        endDateList = endDate.split("-")

        actions = ActionChains(driver)
        actions.send_keys(endDateList[1])
        actions.perform()
        actions.send_keys(endDateList[2])
        actions.perform()
        actions.send_keys(endDateList[0])
        actions.perform()

    elif (end_max == endDate) or (start_max == endDate):
        pass
    else:
        print "Out of data range! Will display maximum possible data range with using default date as input: " + end_max

    time.sleep(5)

def click_done(driver):

    button_elm = driver.find_element(By.XPATH,'//span[text()="Done"]')
#    button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($linkColor) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($linkActiveColor):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)' ]")
    print "click at Done"
    button_elm.click()
    time.sleep(3)
    return None

def click_apply(driver):
    button_elm = driver.find_element(By.XPATH, '//span[text()="Apply"]')
    #button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($linkColor) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($linkActiveColor):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']")
    print "clikc at Apply"
    button_elm.click()
    time.sleep(10)
    return None

def click_download_link(driver):
    a_elm = driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']")
    print "click at download link"
    a_elm.click()
    time.sleep(2)
    return None


# def main():
# 
#     downloadPath = '/home/wchang/Downloads/data'
#     get_stock_data = get_historical_data("^NYA",  downloadPath)
#     get_stock_data = get_historical_data("^IXIC",  downloadPath)
#     # get_stock_data = get_historical_data("cost",  downloadPath)
#     # get_stock_data = get_historical_data("bby",  downloadPath)
# 
# 
#     # startDate = '6/28/2005'
#     # endDate = '6/28/2018'
# 
# 
# if __name__ == "__main__":
#     main()
