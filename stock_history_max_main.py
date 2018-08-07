#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from stock_history_function import *

def main():

    import stock_history_function
    stock_name = raw_input("Please enter the Stock Symbol:   ")
    # while 1:
    #     while 1:
    #         try:
    #             startDate = raw_input("Please enter the Start Date (mm/dd/yyyy):   ")
    #             input_date = time.strptime(startDate, "%m/%d/%Y" )
    #             break
    #         except:
    #             print "Invalid Date, please input again!" + '\n'
    #     while 1:
    #         try:
    #             endDate = raw_input("Please enter the end Date (mm/dd/yyyy):   ")
    #             input_date = time.strptime(endDate, "%m/%d/%Y" )
    #             break
    #         except:
    #             print "Invalid Date, please input again!" + '\n'
    #     if (time.strptime(startDate, "%m/%d/%Y" ) <= time.strptime(endDate, "%m/%d/%Y" )):
    #         break
    #     else:
    #         print "'Start' date must be prior to 'End' date! Please Re-enter the Start Date and End Date" + '\n'
    downloadPath = '/home/wchang/Downloads/data'
    driver = stock_history_function.init_firefox(downloadPath)
    stock_history_function.search_stock(driver, stock_name)
    time.sleep(5)
    stock_history_function.close_pop_up(driver)
    time.sleep(5)
    stock_history_function.click_historical_data(driver)
    stock_history_function.click_time_period(driver)
    stock_history_function.click_max(driver)
    stock_history_function.click_done(driver)
    stock_history_function.click_apply(driver)
    stock_history_function.click_download_link(driver)
    driver.quit()
    return None

if __name__ == "__main__":
    main()
