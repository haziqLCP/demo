from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import base64
# from cryptography.fernet import Fernet

class Encryption:

    def seleniumSetup(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://www.sellfromu.com/login')
        self.driver.maximize_window()
        time.sleep(1)

    def mainlogin(self): #sfu
        self.seleniumSetup()

        #click Register Tab
        self.driver.find_element_by_css_selector(
            'div.wrapper div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
        time.sleep(2)

        #click Sign In Tab
        self.driver.find_element_by_css_selector(
            'div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)

    """<--------------------------------Setup Section----------------------------------->"""
    def getDecodepassword(self):
        return

    """<--------------------------------Test Cases Section----------------------------------->"""
    def test1(self):
        self.mainlogin()

        keyin = 'haziqnyalas@gmail.com'

        Email = self.driver.find_element_by_id('email')
        Password = self.driver.find_element_by_id('password')
        LoginButton = self.driver.find_element_by_id('loginbtn')

        #<--Action-->
        Email.clear()
        Email.send_keys(keyin)

        Password.clear()
        Password.send_keys(self.getDecodepassword())

        LoginButton.click()
        time.sleep(5)

    def test2(self):
        self.mainlogin()

        keyin = 'haziqnyalas@gmail.com'

        Email = self.driver.find_element_by_id('email')
        Password = self.driver.find_element_by_id('password')
        LoginButton = self.driver.find_element_by_id('loginbtn')

        #<--Action-->



#Run Command
run = Encryption()
run.test1()
# run.test2()

