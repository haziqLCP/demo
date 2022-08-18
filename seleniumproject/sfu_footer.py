from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Footer:

    def seleniumSetup(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://www.sellfromu.com/login')
        self.driver.maximize_window()
        time.sleep(1)

    def login(self):
        self.seleniumSetup()

        #click Register Tab
        self.driver.find_element_by_css_selector('div.wrapper div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
        time.sleep(2)

        #click Sign In Tab
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)

        #login SellFromU
        self.driver.find_element_by_id('email').send_keys('haziqnyalas@gmail.com')
        time.sleep(1)
        self.driver.find_element_by_id('password').send_keys('1234567890')
        time.sleep(1)
        self.driver.find_element_by_id('loginbtn').click()
        time.sleep(2)

    """<--------------------------------Setup Section----------------------------------->"""
    def scrollSetup(self):

        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def footer(self):
        self.login()

        self.driver.find_element_by_link_text('MY ORDER').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)

        """<---------------------------------Information------------------------------------->"""
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

        self.driver.find_element_by_link_text('ABOUT US').click()
        self.scrollSetup()
        self.driver.find_element_by_link_text('PRIVACY POLICY').click()
        self.scrollSetup()
        self.driver.find_element_by_link_text('TERMS OF SERVICE').click()
        self.scrollSetup()

        """<-----------------------------------My Account--------------------------------------->"""
        # self.driver.find_element_by_link_text('MY ACCOUNT').click()
        # self.scrollSetup()
        # self.driver.find_element_by_link_text('MY ORDER').click()
        # self.scrollSetup()
        self.driver.find_element_by_link_text('SHOPPING CART').click()
        self.scrollSetup()

        """<---------------------------------Customer Service--------------------------------------->"""
        self.driver.find_element_by_link_text('CONTACT').click()
        self.scrollSetup()

        self.driver.find_element_by_link_text('FAQ').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,430)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,1450)")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

        """<---------------------------------Follow Us--------------------------------------->"""
        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

        #facebook
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.footer-navigation-section.pt-40.pb-40 div.container div.row div.col-lg-3.col-md-3.col-sm-6.col-xs-12.mb-xs-30:nth-child(4) div.social-media-section div.social-links:nth-child(2) > a.facebook').click()
        time.sleep(5)
        self.driver.back()
        time.sleep(1)

        #instagram
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.footer-navigation-section.pt-40.pb-40 div.container div.row div.col-lg-3.col-md-3.col-sm-6.col-xs-12.mb-xs-30:nth-child(4) div.social-media-section div.social-links:nth-child(2) > a.instagram').click()
        time.sleep(5)
        self.driver.back()
        time.sleep(1)

        self.driver.close()

#Run Command
run = Footer()
run.footer()



