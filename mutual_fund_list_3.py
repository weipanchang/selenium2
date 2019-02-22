#!/usr/bin/env python
import re
import string
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
#import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoSuchFrameException
#from selenium.common.exceptions import StaleElementReferenceException
#from selenium.common.exceptions import WebDriverException
#from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import *
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
#from bs4 import BeautifulSoup as bs

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
        driver.implicitly_wait(2)
        driver.set_page_load_timeout(5)    

        url =  "https://www.marketwatch.com/tools/mutual-fund/list/" + self.alpha_beta
        try:
            driver.get(url)
        except TimeoutException:
            pass
        WebDriverWait(driver, 2).until(url_to_be(url))
        print "Page is loaded"

        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[2]/table/tbody")))
#        WebDriverWait(driver, 10).until(visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[2]/table/tbody')))
        elm = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/table/tbody")
#        time.sleep(5)
        symb_elm = elm.find_elements_by_class_name("quotelist-symb")
        name_elm = elm.find_elements_by_class_name("quotelist-name")
        file_write = open( downloadPath + "/list/fund_list_" + alpha_beta +".csv","w")
        for i in range(1, len(symb_elm)):
            symb = symb_elm[i].find_element_by_tag_name("a").text
            name = name_elm[i].find_element_by_tag_name("a").text
            print symb, name
            line = symb + "," + name + "\n"
            file_write.write(line)
        file_write.close()
        time.sleep(1)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
    alpha_beta_list = list(string.ascii_uppercase)
    
    for alpha in alpha_beta_list:
        get_stock_data = get_historical_data(alpha, downloadPath)

if __name__ == "__main__":
    main()
