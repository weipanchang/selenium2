from selenium import webdriver
 
 
driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
 
driver.maximize_window()
driver.get('http://www.google.com')
 
#confirming done
print "Done"