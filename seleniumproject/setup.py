# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
#
# class General:
#
#     def seleniumSetup(general):
#         general.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
#         general.driver.get('https://www.sellfromu.com/login')
#         general.driver.maximize_window()
#         time.sleep(1)
#
#     def login(sfu):
#         # sfu.seleniumSetup()
#
#         # click Register Tab
#         sfu.driver.find_element_by_css_selector(
#             'div.wrapper div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
#         time.sleep(2)
#
#         # click Sign In Tab
#         sfu.driver.find_element_by_css_selector(
#             'div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(1) > a:nth-child(1)').click()
#         time.sleep(2)
#
#         # login SellFromU
#         sfu.driver.find_element_by_id('email').send_keys('haziqnyalas@gmail.com')
#         time.sleep(1)
#         sfu.driver.find_element_by_id('password').send_keys('1234567890')
#         time.sleep(1)
#         sfu.driver.find_element_by_id('loginbtn').click()
#         time.sleep(2)
#
#     def paymentGateway(bank, pay):
#
#         #payment gateway (Maybank) <-can choose any bank type
#         bank.driver.find_element_by_css_selector('body.bills.show:nth-child(2) div.page-bill.page-form:nth-child(1) div.container form.new_transaction:nth-child(2) div.bill-wrap:nth-child(5) div.bill-paymentoptions div.bill-payment-wrap div.body:nth-child(3) div.panel-group div.panel div.panel-collapse.collapse.in div.bill-payment-grid > label.col-xs-4.col-sm-3:nth-child(1)').click()
#         time.sleep(2)
#         bank.driver.execute_script("window.scrollTo(0,700)")
#         bank.driver.find_element_by_css_selector('#btn-pay-bill').click()
#         time.sleep(2)
#
#         #need to find billpizz plugin and pass that status to code
#         success = bank.driver.find_element_by_css_selector(''). click() #temperary code to trigger success
#         fail = bank.driver.find_element_by_css_selector('').click() #temperary code to trigger fail
#
#         #return after done do the payment
#         if pay == success:
#             bank.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
#             bank.driver.find_element_by_css_selector('#paidTab').click()
#         elif pay == fail:
#             bank.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
#             bank.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.my-account-section.section.position-relative.mb-50.fix:nth-child(3) div.container div.row div.col-12 div.row div.col-lg-3.col-12:nth-child(1) div.myaccount-tab-menu.nav > a.active:nth-child(1)').click()
#
#         #logout
#         bank.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
#         time.sleep(2)
#         bank.driver.close()
#
#     def paymentClickButton(payment, click):
#
#         success = payment.driver.find_element_by_css_selector('').click()
#         fail = payment.driver.find_element_by_css_selector('').click()
#
#         if click == success:
#             payment.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
#             payment.driver.find_element_by_css_selector('#paidTab').click()
#         elif click == fail:
#             payment.driver.get('https://sellfromu.com/myorder?billplz%5Bid%5D=ktqbou58&billplz%5Bpaid%5D=false&billplz%5Bpaid_at%5D=&billplz%5Bx_signature%5D=1c014610776bd56438ff4d91dfb0e569fc557692639e822d52943cad4793de07')
#             payment.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.my-account-section.section.position-relative.mb-50.fix:nth-child(3) div.container div.row div.col-12 div.row div.col-lg-3.col-12:nth-child(1) div.myaccount-tab-menu.nav > a.active:nth-child(1)').click()
#
#         #logout
#         payment.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shopify-section:nth-child(1) div.header-top.pt-10.pb-10.pt-lg-10.pb-lg-10.pt-md-10.pb-md-10 div.container div.row div.col-lg-8.col-md-8.col-sm-8.col-xs-12.text-center.text-sm-right div.header-top-menu ul:nth-child(1) li:nth-child(2) > a:nth-child(1)').click()
#         time.sleep(2)
#         payment.driver.close()