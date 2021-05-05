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
    def __init__(self, stock_name, downloadPath, stock_or_fund):
        self.stock_name = stock_name
        print ""
#        print "Processing " + self.stock_name.upper() +" stock history data"
        self.downloadPath = downloadPath
        self.stock_or_fund = stock_or_fund
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
        while True:
            try:
                driver.get(url)
                time.sleep(3)
                print "Yahoo finance Page is loaded"
                if 'finance' in str(driver.current_url):
                    break
            except TimeoutException:
                pass



        time.sleep(1)
#        stock_elm = driver.find_element_by_xpath("//*[@id='yfin-usr-qry']")
#        stock_elm.send_keys(stock_name.upper())
        delay = 0
#        time.sleep(delay + 1)
        while True:
            time.sleep(delay + 1)
            try:
                time.sleep(delay + 1)
#                elm = driver.find_element_by_xpath("//ul[@class='f470fc71']")
                stock_elm = driver.find_element_by_id('yfin-usr-qry')
                time.sleep(delay + 1)
                stock_elm.send_keys((self.stock_name.upper()) + (Keys.ENTER))
                time.sleep(delay + 1)
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
        a_elm.click()
        time.sleep(3)
        print ('\n')
        
        print "click at Stock Summary Button"
        try:
            elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Summary')]"))).click()
        except Exception:
            pass
        time.sleep(1)
        
        if self.stock_or_fund == 'stock':
            try:
                elm = driver.find_element_by_xpath("//div[@class= 'Fw(b) Fl(end)--m Fz(s) C($primaryColor']").text
#                <div class="Fw(b) Fl(end)--m Fz(s) C($primaryColor" data-reactid="189">Near Fair Value</div>
            except Exception:
                pass
            print elm,
            
            try:
                elm = driver.find_element_by_xpath("//span[@class= 'Trsdu(0.3s) ']").text
#                <div class="Fw(b) Fl(end)--m Fz(s) C($primaryColor" data-reactid="189">Near Fair Value</div>
            except Exception:
                pass
            print elm
#        else:
            # print "click at Fund Summary Button"
            # try:
            #     elm = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Summary')]"))).click()
            # except Exception:
            #     pass
            # time.sleep(1)
#            try:
# /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/span
# //*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[1]/span
            table_elm = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody')
            list_elm = table_elm.find_elements_by_xpath('//*/tr[2]')
     
            for elm in list_elm:
                if 'Beta (5Y Monthly)' in elm.text:
                    print elm.text
        else:
#            //*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[1]/span
            table_elm = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody')
            list_elm = table_elm.find_elements_by_xpath('//*/tr[6]')
            
            for elm in list_elm:
                # print elm.text
                if 'Beta' in elm.text:
                   print elm.text
            table_elm = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody')
            list_elm = table_elm.find_elements_by_xpath('//*/tr[2]')
            for elm in list_elm:
                # print elm.text
                if 'Beta' in elm.text:
                   print elm.text
#                /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/table/tbody/tr[6]/td[1]/span
#                /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/table/tbody/tr[6]/td[2]
#            //*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[1]/span/
#           //*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]/span
#            except Exception:
#                pass
#            print elm
            
        print ('\n') *3
#            <span class="Trsdu(0.3s) " data-reactid="173">571.99</span>


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
        stock_fund_names = stock_input_file.readlines()
#        print stock_fund_names
        
        for stock_fund_name in stock_fund_names:
            if len(stock_fund_name) < 2:
                continue
                
            print ("=") * len("Processing " + stock_fund_name.rstrip() +" history data")
            print "Processing " + stock_fund_name.rstrip() +" history data"
            print ("=") * len("Processing " + stock_fund_name.rstrip() +" history data")
            stock = re.search(('\(\w+\)'), stock_fund_name)
            is_stock =  re.search("ETF|Fund",stock_fund_name)
#            print is_stock
            if is_stock:
                stock_or_fund =  'Fund'
            else:
                stock_or_fund ='stock'
            # print stock.group()
            # time.sleep(10000)
            get_stock_data = get_historical_data(stock.group().rstrip().rstrip(')').lstrip('('),  downloadPath, stock_or_fund)


if __name__ == "__main__":
    main()
