from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
import time

class get_bank_balance():
    delay = 0
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    
    # options.add_argument("--headless")
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
    #driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\DIPRAJ\Programming\adclick_bot\chromedriver.exe")
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    #url = "https://login.morganstanleyclientserv.com/ux/"
    driver.set_page_load_timeout(10)
#    wait = WebDriverWait(driver, 100, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    def Morgan_Stanley_balance(self):
         url = "https://login.morganstanleyclientserv.com/ux/"
         while True:
    
             try:
                 self.driver.get(url)
                 self.driver.implicitly_wait(10)
    #                self.driver.delete_all_cookies()
                 time.sleep(self.delay + 1)
                 print ("Morgan Stanley is loaded")
                 if 'login.morganstanleyclientserv.com' in str(self.driver.current_url):
                     break
             except TimeoutException:
                 pass
    
    
         username=self.driver.find_element_by_xpath("//*[@id='page-layout-main-container']/div/form/div[1]/div/input")
    #                stock_elm.send_keys((self.stock_name.upper()) + (Keys.ENTER))
         username.clear()
         username.send_keys('weipanchang')
         time.sleep(self.delay + 5)
         password=self.driver.find_element_by_xpath("//*[@id='ms-password-field__ms-password-1']")
         password.send_keys('Cupertin0!!')
         time.sleep(self.delay + 5)
         self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
         time.sleep(self.delay + 10000)
    #driver.get(url)
    #time.sleep(5)
         driver.quit()
    
def main():

#    downloadPath = "C:\\Users\\William Chang\\Downloads\\Data"
    bank_balance = get_bank_balance()
    Morgan_Stanley_balance = bank_balance.Morgan_Stanley_balance()
    # eTrade_balance
    # Chase_balance


if __name__ == "__main__":
    main()