from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Purchase:

    def seleniumSetup(self): #general
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://www.sellfromu.com/login')
        self.driver.maximize_window()
        time.sleep(1)

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

    """<--------------------------------Setup Section----------------------------------->"""
    def paymentGateway(self, pay): #bank

        #payment gateway (Maybank) <-can choose any bank type
        self.driver.find_element_by_css_selector('body.bills.show:nth-child(2) div.page-bill.page-form:nth-child(1) div.container form.new_transaction:nth-child(2) div.bill-wrap:nth-child(5) div.bill-paymentoptions div.bill-payment-wrap div.body:nth-child(3) div.panel-group div.panel div.panel-collapse.collapse.in div.bill-payment-grid > label.col-xs-4.col-sm-3:nth-child(1)').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,700)")
        self.driver.find_element_by_css_selector('#btn-pay-bill').click()
        time.sleep(2)

        #need to find billpizz plugin and pass that status to the code
        success = self.driver.find_element_by_css_selector(''). click() #temperary code to trigger success
        fail = self.driver.find_element_by_css_selector('').click() #temperary code to trigger fail

        #return after done do the payment
        if pay == success:
            self.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
            self.driver.find_element_by_css_selector('#paidTab').click()
        elif pay == fail:
            self.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
            self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.my-account-section.section.position-relative.mb-50.fix:nth-child(3) div.container div.row div.col-12 div.row div.col-lg-3.col-12:nth-child(1) div.myaccount-tab-menu.nav > a.active:nth-child(1)').click()

        #logout
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
        time.sleep(2)
        self.driver.close()

    def paymentClickButton(self, click): #payment

        success = self.driver.find_element_by_css_selector('').click()
        fail = self.driver.find_element_by_css_selector('').click()

        if click == success:
            self.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
            self.driver.find_element_by_css_selector('#paidTab').click()
        elif click == fail:
            self.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
            self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.my-account-section.section.position-relative.mb-50.fix:nth-child(3) div.container div.row div.col-12 div.row div.col-lg-3.col-12:nth-child(1) div.myaccount-tab-menu.nav > a.active:nth-child(1)').click()

        #logout
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
        time.sleep(2)
        self.driver.close()

    #Report Generated (html)
    # def pytest_runtest_makereport(item, call):
        # pytest_html = item.config.pluginmanager.getplugin("html")
        # outcome =yield
        # report =outcome.get_results()
        # extra = getattr(report, "extra", [])
        #
        # if report.when == 'call':
        #     extra.append(pytest_html.extras.url("https://www.sellfromu.com/login"))
        #
        #     xfail = hasattr(report, "wasxfail")
        #     if (report.skipped and xfail) or (report.failed and not xfail):
        #         extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        #     report.extra = extra

    """<--------------------------------Test Cases Section----------------------------------->"""
    def purchaseFlowSingle(self): #purchase
        self.login()

        #click Order Tab
        self.driver.find_element_by_css_selector('#orders').click()
        time.sleep(2)

        #click Products Tab
        self.driver.find_element_by_css_selector('#shop_link').click()
        time.sleep(1)

        #choose Item (Pen) by Premrita Jegathisan
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(6) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,780)") #command to ask selenium scroll down (change only on Y-exist)

        #increase and decrease the total quantity
        self.driver.find_element_by_css_selector('#add2').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#sub2').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#add2').click()
        time.sleep(1)

        self.driver.find_element_by_id('remark').send_keys('Urgent. Please make fast delivery.')
        time.sleep(2)

        #click add button
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.single-product-content:nth-child(3) div.container div.single-product-content-container.mb-35 div.row div.col-lg-6.col-md-12.col-xs-12:nth-child(2) div.product-feature-details div.cart-buttons.mb-20:nth-child(20) div.add-to-cart-btn.btnatc:nth-child(2) > a:nth-child(1)').click()
        self.driver.implicitly_wait(30) #Added implicitly wait to prevent the code from executing before the page fully loads.

        #click add to cart button
        self.driver.find_element_by_id('cart_button2').click()
        time.sleep(2)

        self.driver.implicitly_wait(30)
        self.driver.execute_script("window.scrollTo(0,0)") #comment to ask selenium scroll up (Change only on Y-exist)
        time.sleep(2)
        self.driver.find_element_by_css_selector('#shopping-cart').click()
        time.sleep(2)

        #edit quantity inside field
        # self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.page-section.section.mb-50:nth-child(3) div.container div.row div.col-12 div.cart-table.table-responsive.mb-40:nth-child(1) table.table.hid:nth-child(9) tbody:nth-child(2) tr:nth-child(1) td.pro-quantity div.pro-qty > input.product_qty').clear()
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.page-section.section.mb-50:nth-child(3) div.container div.row div.col-12 div.cart-table.table-responsive.mb-40:nth-child(1) table.table.hid:nth-child(9) tbody:nth-child(2) tr:nth-child(1) td.pro-quantity div.pro-qty > input.product_qty').send_keys('1')
        # time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,750)")
        self.driver.find_element_by_id('btnthis').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.find_element_by_css_selector('#btnthis').click()
        time.sleep(1)

        #continue with payment gateway (Choose 1 only)
        # self.paymentClickButton() #staging
        # self.paymentGateway() #live

    def multipleProductSameStore(self): #same
        self.login()

        self.driver.find_element_by_css_selector('#shop_link').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        self.driver.execute_script("window.scrollTo(0,550)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.single-product-content:nth-child(3) div.container div.single-product-content-container.mb-35 div.row div.col-lg-6.col-md-12.col-xs-12:nth-child(2) div.product-feature-details div.cart-buttons.mb-20:nth-child(20) div.add-to-cart-btn.btnatc:nth-child(2) > a:nth-child(1)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('cart_button2').click()
        time.sleep(2)
        self.driver.implicitly_wait(30)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        self.driver.find_element_by_css_selector('#shop_link').click()
        self.driver.execute_script("window.scrollTo(0,210)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(4) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        self.driver.execute_script("window.scrollTo(0,550)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.single-product-content:nth-child(3) div.container div.single-product-content-container.mb-35 div.row div.col-lg-6.col-md-12.col-xs-12:nth-child(2) div.product-feature-details div.cart-buttons.mb-20:nth-child(20) div.add-to-cart-btn.btnatc:nth-child(2) > a:nth-child(1)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('cart_button2').click()
        time.sleep(2)
        self.driver.implicitly_wait(30)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        self.driver.find_element_by_css_selector('#shopping-cart').click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,750)")
        self.driver.find_element_by_id('btnthis').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.find_element_by_css_selector('#btnthis').click()
        time.sleep(1)

        #continue with payment gateway (Choose 1 only)
        # self.paymentClickButton() #staging
        # self.paymentGateway() #live

    def multipleProductDifferentStore(self): #different
        self.login()

        #add to cart first product
        self.driver.execute_script("window.scrollTo(0,950)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(11) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid'). click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,780)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_button').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#cart_button2').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('#shopping-cart').click()
        time.sleep(2)

        #add to cart second product
        self.driver.find_element_by_css_selector('#shop_link').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,780)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(4) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,780)")
        self.driver.find_element_by_css_selector('#add2').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#sub2').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('#cart_button').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#cart_button2').click()
        time.sleep(2)

        #confirmation to change area
        self.driver.find_element_by_css_selector('#area_change').click()
        time.sleep(1)

        #product first will move out from the cart
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('#shopping-cart').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,750)")
        self.driver.find_element_by_css_selector('#btnthis').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.find_element_by_css_selector('#button_section').click()
        time.sleep(2)

        #continue with payment gateway (Choose 1 only)
        # self.paymentClickButton() #staging
        # self.paymentGateway() #live

#Run Command
debug = Purchase()
# debug.purchaseFlowSingle() #Purchase Single Product
# debug.multipleProductSameStore() #Purchase Multiple Product (Same Store)
# debug.multipleProductDifferentStore() #Purchase Multiple Product (Different Store)


