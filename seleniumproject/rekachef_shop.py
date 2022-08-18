from selenium import webdriver
import time

class Shop:

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

    def goToShopModule(self):
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar:nth-child(2) section.sidebar ul.sidebar-menu.linkclass > li:nth-child(5)').click()
        time.sleep(3)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def action(self):
        self.login()

        self.goToShopModule()

        #<--follower-->
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.even-row:nth-child(2) td:nth-child(11) > a:nth-child(1)').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 p:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)

        #<--products-->
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.even-row:nth-child(2) td:nth-child(11) > a:nth-child(2)').click()
        time.sleep(3)

        #image
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate td:nth-child(3) a.showProductImage > i.fa.fa-eye').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.wrapper:nth-child(2) div.example-modal:nth-child(6) div.modal.attachmentModal.in div.modal-dialog div.modal-content div.modal-header button.close > span:nth-child(1)').click()
        time.sleep(2)

        #block
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate td:nth-child(6) > a.blockUnblockProduct').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.bootbox.modal.fade.bootbox-confirm.in:nth-child(7) div.modal-dialog div.modal-content div.modal-footer > button.btn.btn-primary.bootbox-accept:nth-child(2)').click()
        time.sleep(2)

        #unblock
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate td:nth-child(6) > a.blockUnblockProduct').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.bootbox.modal.fade.bootbox-confirm.in:nth-child(7) div.modal-dialog div.modal-content div.modal-footer > button.btn.btn-primary.bootbox-accept:nth-child(2)').click()
        time.sleep(2)

        #detail product
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate td:nth-child(8) > a:nth-child(1)').click()
        time.sleep(5)
        self.driver.find_element_by_css_selector('#btnCancel').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 p:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)

        #<--Payout History-->
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.even-row:nth-child(2) td:nth-child(11) > a:nth-child(3)').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 p:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)

        self.logout()

    def filter(self):
        self.login()

        self.goToShopModule()

        #view image
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.even-row:nth-child(2) td:nth-child(7) > a.showShopImage').click()
        time.sleep(4)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.wrapper:nth-child(2) div.example-modal div.modal.attachmentModal.in div.modal-dialog div.modal-content div.modal-header button.close > span:nth-child(1)').click()
        time.sleep(2)

        #filter
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('jalaram')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Reka Cafe')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Vallabh')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)

        self.logout()

run = Shop()
# run.action()
# run.filter()

