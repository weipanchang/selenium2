#!/usr/bin/env python
# import re
"""
Firefox version: 73.0 (64-bit)
"""
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
import re
# from bs4 import BeautifulSoup
# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.firefox.options import Options
import time
# from bs4 import BeautifulSoup as bs
from selenium import webdriver

# class url_to_be(object):
#     """An expectation for checking the current url.
#     url is the expected url, which must be an exact match
#     returns True if the url matches, false otherwise."""
#     def __init__(self, url):
#         self.url = url
# 
#     def __call__(self, driver):
#         return self.url == driver.current_url
# 
# class visibility_of_element_located(object):
#     """ An expectation for checking that an element is present on the DOM of a
#     page and visible. Visibility means that the element is not only displayed
#     but also has a height and width that is greater than 0.
#     locator - used to find the element
#     returns the WebElement once it is located and visible
#     """
#     def __init__(self, locator):
#         self.locator = locator
# 
#     def __call__(self, driver):
#         try:
#             return _element_if_visible(_find_element(driver, self.locator))
#         except StaleElementReferenceException:
#             return False
# 
# class presence_of_element_located(object):
#     """ An expectation for checking that an element is present on the DOM
#     of a page. This does not necessarily mean that the element is visible.
#     locator - used to find the element
#     returns the WebElement once it is located
#     """
#     def __init__(self, locator):
#         self.locator = locator
# 
#     def __call__(self, driver):
#         return _find_element(driver, self.locator)
# 
# def _element_if_visible(element, visibility=True):
#     return element if element.is_displayed() == visibility else False
# 
# def _find_elements(driver, by):
#     try:
#         return driver.find_elements(*by)
#     except WebDriverException as e:
#         raise e
# def _find_element(driver, by):
#     """Looks up an element. Logs and re-raises ``WebDriverException``
#     if thrown."""
#     try:
#         return driver.find_element(*by)
#     except NoSuchElementException as e:
#         raise e
#     except WebDriverException as e:
#         raise e
# 
# class wait_for_text_to_start_with(object):
#     def __init__(self, locator, text_):
#         self.locator = locator
#         self.text = text_
# 
#     def __call__(self, driver):
#         try:
#             element_text = EC._find_element(driver, self.locator).text
#             return element_text.startswith(self.text)
# 
#         except StaleElem       stock_elm = driver.find_element_by_id('yfin-usr-qry')entReferenceException:
#             return False

class get_historical_data():

    #def __init__(self, stock_name, startDate, endDate, downloadPath):
    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
        print ""
#        print "Processing " + self.stock_name.upper() +" stock history data"
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
        options = Options()
#        options.add_argument("--headless")

        driver = webdriver.Firefox(capabilities=desiredCapabilities, firefox_options=options)
        driver.implicitly_wait(10) # seconds
        driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver, 120, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
#        url = "https://finance.yahoo.com/quote/" + self.stock_name + "?p=" + self.stock_name + "&.tsrc=fin-srch"


        url = "https://finance.yahoo.com"
        try:
            driver.get(url)
        except TimeoutException:
            pass

        print "Yahoo finance Page is loaded"

        time.sleep(1)
#        stock_elm = driver.find_element_by_xpath("//*[@id='yfin-usr-qry']")
#        stock_elm.send_keys(stock_name.upper())
        delay = 0
#        time.sleep(delay + 1)
        while True:
            try:
                time.sleep(delay + 1)
#                elm = driver.find_element_by_xpath("//ul[@class='f470fc71']")
                stock_elm = driver.find_element_by_id('yfin-usr-qry')


                stock_elm.send_keys((self.stock_name.upper()) + (Keys.ENTER))
                time.sleep(2)
#                print self.stock_name.upper(), str(driver.current_url)
                if self.stock_name.upper() in str(driver.current_url):
                    break
           
            except:
                stock_elm.clear()
#                stock_elm.send_keys(stock_name.upper())
#                stock_elm.send_keys((stock_name.upper()) + (Keys.ENTER))
#                time.sleep(2)
                print "Yahoo search slow, will reloop!"


        print "click at Historical Data Button"
        try:
            elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Historical Data')]"))).click()
        except TimeoutException:
            pass

        time.sleep(1)

        input_elm = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")
        print "click at input button"
        input_elm.click()
        time.sleep(1)

        elm = driver.find_element_by_xpath("//li[4]/button[@data-value='MAX']")
        print "click at max"
        elm.click()
        time.sleep(1)
        # elm= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/button")
        # elm.click()
        
        print "clikc at Apply"
        try:
#            elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']"))).click()
            elm = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Apply"]'))).click()
        except TimeoutException:
            pass

        time.sleep(5)

        a_elm = driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']")
        print "click at download link"
        print ('\n') *3

        a_elm.click()
        time.sleep(3)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'

    # get_stock_data = get_historical_data("VTI",  downloadPath)
    # get_stock_data = get_historical_data("VIG",  downloadPath)
    # get_stock_data = get_historical_data("VYM",  downloadPath)
    # get_stock_data = get_historical_data("SCHD",  downloadPath)
    # get_stock_data = get_historical_data("vt",  downloadPath)
    # get_stock_data = get_historical_data("sdy",  downloadPath)
    # get_stock_data = get_historical_data("dvy",  downloadPath)

    with open("stock_list_2.txt","r") as stock_input_file:
        stock_symbols = stock_input_file.readlines()
#        print stock_symbols
        
        for stock_symbol in stock_symbols:
            print ("=") * len("Processing " + stock_symbol.rstrip() +" stock history data")
            print "Processing " + stock_symbol.rstrip() +" stock history data"
            print ("=") * len("Processing " + stock_symbol.rstrip() +" stock history data")
            stock = re.search(('\(\w+\)'), stock_symbol)
            # print stock.group()
            # time.sleep(10000)
            get_stock_data = get_historical_data(stock.group().rstrip().rstrip(')').lstrip('('),  downloadPath)


if __name__ == "__main__":
    main()
