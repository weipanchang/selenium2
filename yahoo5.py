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
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

def get_historical_data(name):
    stock_name = name
#    url = "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"    
    url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
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
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"
        print "Page loading is done"
    time.sleep(.5)
    print "Finding tag span Done"
    elm_lists = driver.find_elements_by_tag_name("span")
    
    for elm in elm_lists:
        try:        
#               print elm.get_attribute('href'), elm.text
            if elm.text == "Historical Data":
                print "Found!!"
                print elm.text
                elm.click()
#                    print self.url
                time.sleep(2.5)
                len_of_input_elm = 0
                while len_of_input_elm < 5:
                    input_elm_lists = driver.find_elements_by_tag_name("input")
                    len_of_input_elm = len(input_elm_lists)
                print len(input_elm_lists)
                for input_elm in input_elm_lists:
                     if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":
                         print "find right input tag"
                         print input_elm.get_attribute("data-test")
                         input_elm.click()
                         time.sleep(2.5)
                         elm = driver.find_element_by_name("startDate")
                         print "Found startDate"
                         elm.clear()
                         elm.send_keys("6/25/2012")
                         elm = driver.find_element_by_name("endDate")
                         print "Found endDate"
                         elm.clear()
                         elm.send_keys("6/25/2015")
                         break
                button_elm_lists = driver.find_elements_by_tag_name("button")
                print len(button_elm_lists)
                for button_elm in button_elm_lists:
                        if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
                            print "Found Done"
                            button_elm.click()
                            time.sleep(5.5)                
#                         if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)":
#                             print "Found Apply"
#                             button_elm.click()
#                             time.sleep(5.5)                
# #                    print input_elm.get_attribute("class")
#                             break
                            break
        except:
            pass
    button_elm_lists = driver.find_elements_by_tag_name("button") 
    for button_elm in button_elm_lists:
        if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)":
            print "Found Apply"
            button_elm.click()
            time.sleep(5.5)                
    #                   print input_elm.get_attribute("class")
            break
    a_elm_lists = driver.find_elements_by_tag_name("a")
    for a_elm in a_elm_lists:
        if a_elm.get_attribute("class") == "Fl(end) Mt(3px) Cur(p)":
            print "Found download"
            url = a_elm.get_attribute('href')
            print url
            break
    driver.get(url)
    
get_historical_data('amzn')     
#            print "Not Found"
    
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


#data-test="date-picker-full-range"