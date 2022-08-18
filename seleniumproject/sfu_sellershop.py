from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#call another class from another file
from sfu_purchase import Purchase as purchase

class SellerShop:

    def seleniumSetup(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://www.sellfromu.com/login')
        self.driver.maximize_window()
        time.sleep(1)

        # purchase.login() # <- to call login in another class

    def login(self): #sfu
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

    def loginAdminPanel(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://sellfromu.com/public/admin/index.php')
        self.driver.maximize_window()
        time.sleep(1)

        #Login Admin panel
        self.driver.find_element_by_css_selector('#username').send_keys('admin')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#password').send_keys('LCPAdmin@123')
        time.sleep(1)

        self.driver.find_element_by_css_selector('body.account-page:nth-child(2) div.main-wrapper:nth-child(1) div.account-content div.container div.account-box div.account-wrapper form:nth-child(2) div.form-group.text-center:nth-child(3) > button.btn.btn-primary.account-btn').click()
        time.sleep(2)

    """<--------------------------------Setup Section----------------------------------->"""
    def checkSellerShop(self):

        #Looping to call every shop/seller
        shop = self.driver.find_elements_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(1) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid')

        for i in shop:

            self.driver.execute_script("arguments[0].click();", i)

            self.driver.execute_script("window.scrollTo(0,450)")
            time.sleep(1)
            self.driver.back()
            time.sleep(2)

    def shop(self):

        #search by Shop
        self.driver.find_element_by_css_selector('#search_shop').send_keys('irfan bakery')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,350)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,400)")

        #click Profile Tab
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.container:nth-child(4) div.page nav.menu ul.menu__list > li.menu__group:nth-child(2)').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,250)")
        time.sleep(1)

        self.driver.implicitly_wait(30)

        #click Home Tab
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/nav[1]/ul[1]/li[1]').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(1)

    def seller(self):

        #search by Seller
        self.driver.find_element_by_css_selector('#search_shop').send_keys('Henry Lim')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,350)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,400)")

        #click Profile Tab
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.container:nth-child(4) div.page nav.menu ul.menu__list > li.menu__group:nth-child(2)').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,250)")
        time.sleep(1)

        self.driver.implicitly_wait(30)

        #click Home Tab
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/nav[1]/ul[1]/li[1]').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(1)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def searchInside(self): #tab
        self.login()
        self.driver.implicitly_wait(30)

        """Shop"""
        self.driver.find_element_by_link_text("SELLER/SHOP").click()
        time.sleep(1)

        #1st Method follow checked
        self.shop()

        self.driver.find_element_by_partial_link_text('+ FOLL').click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('- UNFOLL').click()
        time.sleep(2)

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #2nd Method follow checked
        self.shop()

        self.driver.find_element_by_partial_link_text('+ FOLL').click()
        time.sleep(2)

        #click Favourite
        self.driver.find_element_by_partial_link_text('FAVOURI').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#fav2').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product span:nth-child(3) a:nth-child(1) > i.fas.fa-times-circle').click()

        #checking either already unfollow or not (Shop)
        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        self.driver.find_element_by_css_selector('#search_shop').send_keys('irfan bakery')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,350)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        """Seller"""
        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        #1st Method follow checked
        self.seller()

        self.driver.find_element_by_partial_link_text('+ FOLL').click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('- UNFOLL').click()
        time.sleep(2)

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        #2nd Method follow checked
        self.seller()

        self.driver.find_element_by_partial_link_text('+ FOLL').click()
        time.sleep(1)

        #click Favourite
        self.driver.find_element_by_partial_link_text('FAVOURI').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#fav2').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product span:nth-child(3) a:nth-child(1) > i.fas.fa-times-circle').click()

        #checking either already unfollow or not (Seller)
        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('#search_shop').send_keys('Henry Lim')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,350)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        self.driver.close()

    def searchNotInside(self):
        self.login()

        self.driver.find_element_by_link_text("SELLER/SHOP").click()
        time.sleep(1)

        #search Shop
        self.driver.find_element_by_css_selector('#search_shop').send_keys('Family Mart')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        #checking dia dapat x link ni
        link = self.driver.get('https://sellfromu.com/seller?_token=rkzJV08bBIdnpghLeTjmPK5j5xwNycTRCkFukTC3&type=shop&search_shop=family+mart')
        newlink = 'https://sellfromu.com/seller?_token=rkzJV08bBIdnpghLeTjmPK5j5xwNycTRCkFukTC3&type=shop&search_shop=family+mart'

        if link == newlink:
            print("No Shop Found. Test Successful")
        else:
            print("Error. Test Failed")

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        #search Seller
        self.driver.find_element_by_css_selector('#search_shop').send_keys('Guinevere')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        #checking dia dapat x link ni
        link2 = self.driver.get('https://sellfromu.com/seller?_token=rkzJV08bBIdnpghLeTjmPK5j5xwNycTRCkFukTC3&type=seller&search_shop=Guinevere')
        newlink2 = 'https://sellfromu.com/seller?_token=rkzJV08bBIdnpghLeTjmPK5j5xwNycTRCkFukTC3&type=seller&search_shop=Guinevere'

        if link2 == newlink2:
            print("No Seller Found. Test Successful")
        else:
            print("Error. Test Failed")

        self.driver.close()

    def searchInactiveAccount(self):

        """Open SellFromU System"""
        self.login()

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #search Shop
        self.driver.find_element_by_css_selector('#search_shop').send_keys('haziq')

        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        #search Seller
        self.driver.find_element_by_css_selector('#search_shop').send_keys('haziq')

        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12 div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(2)

        self.driver.close()

        """inactive account at Admin Panel"""
        self.loginAdminPanel()

        self.driver.implicitly_wait(30)
        self.driver.get('https://sellfromu.com/public/admin/user_list.php')
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        self.driver.find_element_by_link_text('3').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[16]/td[1]/input[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element_by_link_text('Update Active/Unactive').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.modal-open:nth-child(2) div.main-wrapper:nth-child(1) div.page-wrapper div.modal.fade.show:nth-child(7) div.modal-dialog.modal-sm div.modal-content div.modal-body form:nth-child(1) div.form-group select.select.floating.select2-hidden-accessible > option:nth-child(2)').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.modal-open:nth-child(2) div.main-wrapper:nth-child(1) div.page-wrapper div.modal.fade.show:nth-child(7) div.modal-dialog.modal-sm div.modal-content div.modal-footer > button.btn.btn-secondary.btn-sm:nth-child(2)').click()
        time.sleep(4)

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        self.driver.find_element_by_link_text('3').click()
        time.sleep(3)

        #click logout button
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/ul[1]/li[1]').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('Logout').click()
        time.sleep(2)

        self.driver.close()

        """Check again at SellFromU System"""
        self.login()

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #search Shop
        self.driver.find_element_by_css_selector('#search_shop').send_keys('haziq')  #<--Remarks: Need to search account already inactive from the system

        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)


        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #drop down menu (Shop -> Seller)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center form:nth-child(1) div:nth-child(2) select:nth-child(1) > option:nth-child(2)').click()
        time.sleep(2)

        #search Seller
        self.driver.find_element_by_css_selector('#search_shop').send_keys('haziq')  #<--Remarks: Need to search account already inactive from the system

        time.sleep(1)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]').click()
        time.sleep(2)

        self.driver.close()

        """active back that account at Admin Panel"""
        self.loginAdminPanel()

        self.driver.implicitly_wait(30)
        self.driver.get('https://sellfromu.com/public/admin/user_list.php')
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        self.driver.find_element_by_link_text('3').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[16]/td[1]/input[1]').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element_by_link_text('Update Active/Unactive').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.modal-open:nth-child(2) div.main-wrapper:nth-child(1) div.page-wrapper div.modal.fade.show:nth-child(7) div.modal-dialog.modal-sm div.modal-content div.modal-body form:nth-child(1) div.form-group select.select.floating.select2-hidden-accessible > option:nth-child(1)').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.modal-open:nth-child(2) div.main-wrapper:nth-child(1) div.page-wrapper div.modal.fade.show:nth-child(7) div.modal-dialog.modal-sm div.modal-content div.modal-footer > button.btn.btn-secondary.btn-sm:nth-child(2)').click()
        time.sleep(4)

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        self.driver.find_element_by_link_text('3').click()
        time.sleep(3)

        #Try to find logout button
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/ul[1]/li[1]').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('Logout').click()
        time.sleep(2)

        self.driver.close()

    def clickingSellerShop(self):
        self.login()

        self.driver.find_element_by_link_text('SELLER/SHOP').click()
        time.sleep(1)

        #1st Image
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(1) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,630)")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        #2nd Image
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(3) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,630)")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        #3rd Image
        self.driver.execute_script("window.scrollTo(0,650)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(7) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,630)")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.implicitly_wait(30)

        #4th Image
        self.driver.execute_script("window.scrollTo(0,1180)") #scroll ke paling bawah
        time.sleep(1)
        self.driver.find_element_by_link_text('4')
        time.sleep(1)
        # self.driver.execute_script("window.scrollTo(0,630)")
        # time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(11) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,630)")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.implicitly_wait(30)

        #5th Image
        self.driver.execute_script("window.scrollTo(0,1180)")  # scroll ke paling bawah
        time.sleep(1)
        self.driver.find_element_by_link_text('6').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(1) div:nth-child(1) div.gf-product.shop-grid-view-product div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,630)")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        self.driver.close()

#Run Command
run = SellerShop()
# run.searchInside()
# run.searchNotInside()
# run.searchInactiveAccount()
# run.clickingSellerShop()



