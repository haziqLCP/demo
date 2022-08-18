from selenium import webdriver
import time

class Buyer:

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

    def goToBuyerModule(self):
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar section.sidebar ul.sidebar-menu.linkclass > li:nth-child(4)').click()
        time.sleep(3)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def action(self):
        self.login()

        self.goToBuyerModule()

        #<--Change Status-->

        #Change to Block
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(6) > a.blockUnblockUser').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.bootbox.modal.fade.bootbox-confirm.in:nth-child(7) div.modal-dialog div.modal-content div.modal-footer > button.btn.btn-primary.bootbox-accept:nth-child(2)').click()
        time.sleep(5)

        #Change to Unblock
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(6) > a.blockUnblockUser').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.bootbox.modal.fade.bootbox-confirm.in:nth-child(7) div.modal-dialog div.modal-content div.modal-footer > button.btn.btn-primary.bootbox-accept:nth-child(2)').click()
        time.sleep(5)

        self.logout()

    def filter(self):
        self.login()

        self.goToBuyerModule()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('michelle')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)

        self.driver.refresh()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('huiyuanLCP')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)

        self.driver.refresh()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Jason')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)

        self.driver.refresh()

        self.logout()

run = Buyer()
# run.action()
# run.filter()

