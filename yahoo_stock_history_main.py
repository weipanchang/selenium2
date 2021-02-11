#!/usr/bin/env python
import re,sys
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#from bs4 import BeautifulSoup as bs
from selenium import webdriver
from stock_history_function import *

def main():

    if len(sys.argv) == 2:
        stock_name = sys.argv[1]

    elif len(sys.argv) == 1:
        stock_name = raw_input("Please enter the Stock Symbol:   ")
        while 1:
            while 1:
                startDate = raw_input("Please enter the Start Date (mm/dd/yyyy):   ")
                if startDate != "":
                    try:
                        input_date = time.strptime(startDate, "%m/%d/%Y" )
                        break
                    except:
                        print "Invalid Date, please input again!" + '\n'
                else: break
            while 1:

                endDate = raw_input("Please enter the end Date (mm/dd/yyyy):   ")
                if endDate != "":
                    try:
                        input_date = time.strptime(endDate, "%m/%d/%Y" )
                        break
                    except:
                        print "Invalid Date, please input again!" + '\n'
                else: break
            if (startDate != "") and (endDate != ""):
                if time.strptime(startDate, "%m/%d/%Y" ) <= time.strptime(endDate, "%m/%d/%Y" ):
                    break
                else:
                    print "'Start' date must be prior to 'End' date! Please Re-enter the Start Date and End Date" + '\n'
            else: break
    import stock_history_function
    downloadPath = '/home/wchang/Downloads/data'
#    wait = WebDriverWait(driver, 120, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    driver = stock_history_function.init_firefox(downloadPath) 
    print ""
    print "Processing " + stock_name.upper() + " ........"
    print ""
    wait = WebDriverWait(driver, 120, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    stock_history_function.search_stock(driver, stock_name, wait)
    time.sleep(1)
    stock_history_function.close_pop_up(driver)
    time.sleep(1)
    
    stock_history_function.click_historical_data(driver, wait)
    stock_history_function.click_time_period(driver)
    stock_history_function.click_max(driver)

    [start_max, end_max] = stock_history_function.get_max_period(driver)

    if len(sys.argv) == 1 and startDate != "" and endDate !="":
        if time.strptime(startDate, "%m/%d/%Y") > time.strptime(start_max, "%Y-%m-%d") \
            or time.strptime(endDate, "%m/%d/%Y") < time.strptime(end_max, "%Y-%m-%d"):
            stock_history_function.input_date(driver, startDate, endDate, start_max, end_max)
        stock_history_function.click_done(driver)
    stock_history_function.click_apply(driver)
    stock_history_function.click_download_link(driver)
    driver.quit()
    return None

if __name__ == "__main__":
    main()
