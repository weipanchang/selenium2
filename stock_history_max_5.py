#!/usr/bin/env python
# import re
"""
Google Chromer version Version 80.0.3987.116 (Official Build) (64-bit)

"""
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
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
#         return driver.find_elemchromeOptionsents(*by)
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
#         except StaleElementReferenceException:
#             return False

class get_historical_data():

    #def __init__(self, stock_name, startDate, endDate, downloadPath):
    def __init__(self, stock_name, downloadPath):
        self.stock_name = stock_name
        print ""
        print "Processing " + self.stock_name.upper() +" stock history data"
        self.downloadPath = downloadPath
        
        # for Firefox
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", self.downloadPath)
        # profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
        # profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        # profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        # profile.set_preference("browser.download.manager.focusWhenStarting", False)
        # profile.set_preference("browser.download.manager.useWindow", False)
        # profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        # profile.set_preference("browser.download.manager.closeWhenDone", False)
        # profile.set_preference("browser.cache.disk.enable", False)
        # profile.set_preference("browser.cache.memory.enable", False)
        # profile.set_preference("browser.cache.offline.enable", False)
        # profile.set_preference("network.http.use-cache", False)
        # desiredCapabilities = DesiredCapabilities.FIREFOX.copy()
        # desiredCapabilities['firefox_profile'] = profile.encoded
        # driver = webdriver.Firefox(capabilities=desiredCapabilities)
        
        #  For Chrome
#        options.headless = True
        chromeOptions = webdriver.ChromeOptions()
#        prefs = {"download.default_directory" : self.downloadPath}
        chromeOptions.add_experimental_option("prefs", {
             "download.default_directory" : self.downloadPath,
             'profile.default_content_setting_values.automatic_downloads': 2,
              })
        chromeOptions.add_argument("--disable-user-media-security=true")
        chromeOptions.headless = True
        chromeOptions.add_argument('--disable-gpu') 
        chromedriver = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        # options.add_experimental_option("prefs", {
        # "download.default_directory": r"C:\Users\xxx\downloads\Test",
        # "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        # "safebrowsing.enabled": True })
        #      
        # from selenium import webdriver
        # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        # 
        # options = webdriver.ChromeOptions()
        # options.gpu = False
        # options.headless = True
        # options.add_experimental_option("prefs", {
        #     "download.default_directory" : "/data/books/chrome/",
        #     'profile.default_content_setting_values.automatic_downloads': 2,
        #     })
        # 
        # desired = options.to_capabilities()
        # desired['loggingPrefs'] = { 'performance': 'ALL'}
        # driver = webdriver.Chrome(desired_capabilities=desired)
  
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
        stock_elm = driver.find_element_by_xpath("//*[@id='yfin-usr-qry']")
        stock_elm.send_keys(stock_name.upper())
        delay = 0
#        time.sleep(delay + 1)
        while True:
            try:
                time.sleep(delay + 1)
                elm = driver.find_element_by_xpath("//ul[@class='f470fc71']")
#                print "Found"
                stock_elm.send_keys(Keys.ENTER)
                break
            except:
                stock_elm.clear()
                stock_elm.send_keys(stock_name.upper())
                print "Yahoo search slow, will reloop!"

            
#         try:
#              button_elm = driver.find_element_by_css_selector(".Z\(6\) > button:nth-child(3) > svg:nth-child(1)")
#              print "click at x button "
#              button_elm.click()
#              time.sleep(1)
#         except:
#             pass
# 
#         try:
# #                if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
#             button_elm = driver.find_element_by_xpath("//button[@class = 'Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close']")
#             print "click at x button"
#             button_elm.click()
#             time.sleep(1)
# #           break
#         except:
#             pass


        print "click at Historical Data Button"
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Historical Data')]"))).click()
        except TimeoutException:
            pass
        time.sleep(1)

        print "click at input button"
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='C($linkColor) Fz(14px)']"))).click()
#        input_elm = driver.find_element_by_xpath("//span[@class='C($linkColor) Fz(14px)']")

#        input_elm.click()
        time.sleep(1)

        # print "click at max"
        # driver.find_element_by_xpath("//ul[2]/li[4]/button[@data-value='MAX']").click()
        # time.sleep(1)
        # elm= driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/button")
        # elm.click()
 #       /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[1]/li[3]/button
 #       /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[1]/button
 
        # print "click at 1_D"
        # driver.find_element_by_xpath("//ul[1]/li[1]/button[@data-value='1_D']").click()
        # time.sleep(1)
        
        # print "click at 5 Days"
        # driver.find_element_by_xpath("//ul[1]/li[2]/button[@data-value='5_D']").click()
        # time.sleep(1)
        
        # print "click at 3 Month"
        # driver.find_element_by_xpath("//ul[1]/li[3]/button[@data-value='3_M']").click()
        # time.sleep(1)
        
        print "click at 6 Month"
        driver.find_element_by_xpath("//ul[1]/li[4]/button[@data-value='6_M']").click()
        time.sleep(1)
         
        print "clikc at Apply"
        # try:
        #     elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']"))).click()
        # except TimeoutException:
        #     pass
        button_elm = driver.find_element_by_xpath("//button[@class =' Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)']")
        button_elm.click()
        time.sleep(5)

        print "click at download link"
        driver.find_element_by_xpath("//a[@class = 'Fl(end) Mt(3px) Cur(p)']").click()
#        a_elm.click()
        time.sleep(3)
        driver.quit()

def main():

    downloadPath = '/home/wchang/Downloads/data'
    get_stock_data = get_historical_data("vgstx",  downloadPath)
    # get_stock_data = get_historical_data("aapl",  downloadPath)
    # get_stock_data = get_historical_data("goog",  downloadPath)
    # get_stock_data = get_historical_data("ibm",  downloadPath)
    # get_stock_data = get_historical_data("amzn",  downloadPath)
    # get_stock_data = get_historical_data("qai",  downloadPath)
    # get_stock_data = get_historical_data("bby",  downloadPath)
    # get_stock_data = get_historical_data("amd",  downloadPath)
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
