from selenium import webdriver
import time

class Rtt:

    def seleniumSetup(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://200oksolutionsdemo.com/rekachef/admin/login')
        self.driver.maximize_window()
        time.sleep(1)

    def login(self):
        self.seleniumSetup()

        self.driver.find_element_by_css_selector('#useremail').send_keys('yedda.lee@lcpbuildsofttechnology.com')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#password').send_keys('Test@123')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btnLogin').click()
        time.sleep(1)

    """<--------------------------------Setup Section----------------------------------->"""
    def logout(self):
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) header.main-header nav.navbar.navbar-static-top div.navbar-custom-menu ul.nav.navbar-nav li.dropdown.user.user-menu > a.dropdown-toggle').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) header.main-header nav.navbar.navbar-static-top div.navbar-custom-menu ul.nav.navbar-nav li.dropdown.user.user-menu.open ul.dropdown-menu li.user-footer div.pull-right > a.btn.btn-default.btn-flat').click()
        time.sleep(3)

        self.driver.close()

    """<--------------------------------Test Cases Section----------------------------------->"""
    def radiusModule(self):
        self.login()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar section.sidebar ul.sidebar-menu.linkclass > li:nth-child(8)').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('#radius').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#radius').send_keys('30')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btnSubmit').click()
        time.sleep(5)

        self.logout()

    def taxModule(self):
        self.login()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar section.sidebar ul.sidebar-menu.linkclass > li:nth-child(9)').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('#tax_percentage').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#tax_percentage').send_keys('7.00')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btnSubmit').click()
        time.sleep(5)

        self.logout()

    def tipCommissionModule(self):
        self.login()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar section.sidebar ul.sidebar-menu.linkclass > li:nth-child(10)').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('#tip_commission_percentage').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#tip_commission_percentage').send_keys('5.00')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#btnSubmit').click()
        time.sleep(5)

        self.logout()

    def cart(self):
        self.login()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar:nth-child(2) section.sidebar ul.sidebar-menu.linkclass > li:nth-child(11)').click()
        time.sleep(3)

        #1st filter
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Vallabh')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        #2st filter
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Prateek')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        self.logout()

run = Rtt()
run.radiusModule()
run.taxModule()
run.tipCommissionModule()
run.cart()


