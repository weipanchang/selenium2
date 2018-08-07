#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
#import Selenium2Library
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
def get_historical_data(name):
    stock_name = name
#    url = "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"    
    url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
#    driver = webdriver.Firefox(executable_path="/home/wchang/Downloads/geckodriver")
    driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
#    webdriver.FirefoxProfile()
    webdriver.FirefoxProfile().set_preference("browser.download.manager.showWhenStarting", False)
    webdriver.FirefoxProfile().set_preference("browser.download.manager.showAlertOnComplete", False)
    webdriver.FirefoxProfile().set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    webdriver.FirefoxProfile().set_preference("browser.download.dir", "~/Downloads")
#    url = "http://finance.yahoo.com/quote/AMZN/history?p=AMZN"    
    try:
        driver.get(url)
#        delay = 3
#        print "Page is ready!"
    except TimeoutException:
#        print "Loading took too much time!"
        print "Page loading is done"
    time.sleep(.5)

    elm_lists = driver.find_elements_by_tag_name("span")
#    elm_lists = driver.find_elements_by_tag_name("span")
    print "Found tag span"    
    for elm in elm_lists:
#               print elm.get_attribute('href'), elm.text
        if elm.get_attribute("data-reactid") == "40":
                print "Found Historical Data"
#                time.sleep(2.5)
#                print elm.text
                elm.send_keys("\n")
#                elm.click()
                break
#                    print self.url

    len_of_input_elm = 0
    while 1:
        input_elm_lists = driver.find_elements_by_tag_name("input")
        if input_elm_lists[-1].get_attribute("class") =="C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":
            len_of_input_elm = len(input_elm_lists)
            print "number of input element:" + str(len(input_elm_lists))
            input_elm_lists[-1].elm.click()
            time.sleep(.5)
            break
    
    # for input_elm in input_elm_lists:
    #     print input_elm.get_attribute("class")
    #     if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":
    #         print "find right input tag"
    #         print input_elm.get_attribute("data-test")
    #         input_elm.click()
    #         time.sleep(.5)
    #         break            
    input_elm = driver.find_element_by_class_name("Bdrs(0) Bxsh(n)! Fz(s) Bxz(bb) D(ib) Bg(n) Pend(5px) Px(8px) Py(0) H(34px) Lh(34px) Bd O(n):f O(n):h Bdc($c-fuji-grey-c) Bdc($c-fuji-blue-1-b):f M(0) Pstart(10px) Bgc(white) W(90px) Mt(5px)")
    print "Found startDate"
    input_elm.clear()
    input_elm.send_keys("6/25/2015")
    elm = driver.find_element_by_name("endDate")
    print "Found endDate"
    input_elm.clear()
    input_elm.send_keys("6/25/2017")
    
    button_elm_lists = driver.find_elements_by_tag_name("button")
    print "button_elm_lists" + str(len(button_elm_lists))
    for button_elm in button_elm_lists:
            if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
                print "Found Done"
                button_elm.click()
                driver.implicitly_wait(10)
#                            time.sleep(2.5)
#                button_elm_lists = driver.find_elements_by_tag_name("button")
#                for button_elm in button_elm_lists:
#                        url = Selenium2Library.Selenium2Library().get_location()
#                        driver.get(url)
#                        print current_url.text
#                        driver.get(driver.current_url)
    #             span_elm_lists = driver.find_elements_by_tag_name("span")
    #             wait.until(ExpectedConditions.stalenessOf(span_elm))
    #             for span_elm in span_elm_lists:
    #                 if span_elm.get_attribute("data-reactid") == "26 ":
    #                     
    #                     print "Found Apply"
    #                     span_elm.click()
    #                     time.sleep(.5)                            
    # #                    print input_elm.get_attribute("class")
    #                     break
    #             break
    # a_elm_lists = driver.find_elements_by_tag_name("a")
    # for a_elm in a_elm_lists:
    #     if a_elm.get_attribute("class") == "Fl(end) Mt(3px) Cur(p)":
    #         print "Found download"
    #         a.elm.click()
    #         break
    # driver.close()
#            print "Not Found"

# from selenium.common.exceptions import StaleElementReferenceException
# 
# def _loop_is_text_present(text, max_attempts=3):
#     attempt = 1
#     while True:
#         try:
#             return self.browser.is_text_present(text)
#         except StaleElementReferenceException:
#             if attempt == max_attempts:
#                 raise
#             attempt += 1
 

    
# from selenium.webdriver.support.ui import WebDriverWait
# ...
# ...
# def find(driver):
#     element = driver.find_elements_by_id("data")
#     if element:
#         return element
#     else:
#         return False
# element = WebDriverWait(driver, secs).until(find)    
    
#    rows = bs(urllib2.urlopen(url).read(), 'lxml').findAll('table')[0].tbody.findAll('tr')
#    page = bs(urllib2.urlopen(url).read(), 'lxml').find('body')
    # for tag in page.findAll():
    #     try:
    #         if tag.attrs['data-value']=="YTD" :
    #             print "found"            
    #             key_list = list()
    #             key_list.extend(list(tag.attrs))
    #             print key_list
    #             print tag.prettify()
    #         # try:
    #         #     if len(key_list)  ==0:
    #             print tag.name
    #     except:
    #         pass
#     for div in page.findAll():
# #        if "data-reactid" in div.attrs.keys():
# #            if div.attrs['data-reactid'] == '3':
# #            try:
# #                if div.attrs['class'] == "'Mt(15px)', 'drop-down-selector', 'historical'":
#         try:
#             if div.attrs.has_key('class') and div.attrs['class'][2] == 'historical':
# #                print div.attrs['class']
#                 children = div.findChildren()
#                 for child in children:
#                     if child.name =='span':
#                         children2  = child.findChildren()   
#                         for child2 in children2:
#                             if child2.name =='span':
#                                 print child2.prettify()
#         except:
#             pass
    # for span in  page.findAll('span'):
    #     for span2 in span.findAll('span'):
    #         children =  span2.findChildren()
    #         for child in children:
    #             print child.name
# for tag in tags:
#     tags_keys = list()
#     for line in htmlist:
#         aux=BeautifulSoup(line, "html.parser").find(tag)
#         if aux:
#             tags_keys.extend(list(aux.attrs))
#     print(tag+":"+",".join(sorted(set(tags_keys))))
#    doc = rows.prettify()
#    print doc.encode('utf-8')
#    with open("python.txt",'a', encoding='utf-8') as inputfile:
#        inputfile.write(doc)
    # for j in rows.findAll('input'):
    #     try: 
    #         if j.find(attrs={"data-test" :"date-picker-full-range"}):
    #             print "Found"
    #     except:
    #         pass
        #         
        # for tag in j.findAll():
        #     print tag.name
        # for k in j.findAll('input'):
        #     try:
        #         if k.findAll(attrs={"data-test":"date-picker-full-range"}):
        #             print k
        #     except:
        #        pass
#        for k in j.findAll('span'):
#            for l in k.findAll(string =  'Time Period'):
#                print l
            
    # for each_row in rows:
    #     divs = each_row.findAll('td')
    #     if divs[1].span.text  != 'Dividend': #Ignore this row in the table
    #         #I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
    #         data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text.replace(',',''))})
    # 
    # return data[:number_of_days]

#Test
# for i in get_historical_data('amzn', 5):
#     print i

# def get_historical_data(name, number_of_days):
#     url = "https://finance.yahoo.com/quote/" + name + "/history/"
# 
#     page = bs(urllib2.urlopen(url).read(), 'lxml')
#     tree = ET.parse(page)

#      
#     rows = page.body.findAll("input", {"data-test","date-picker-full-range"})
#     print rows
get_historical_data('amzn')

#data-test="date-picker-full-range"