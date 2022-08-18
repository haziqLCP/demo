from selenium import webdriver
import time

class Topics:

    def seleniumSetup(self):
        self.driver = webdriver.Chrome("E://PROGRAM INSTALLER//chrome_driver//chromedriver.exe")
        self.driver.get('https://200oksolutionsdemo.com/rekachef/admin/login')
        self.driver.maximize_window()
        time.sleep(1)

    def login(self):
        self. seleniumSetup()

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

    def goToTopicsModule(self):
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar section.sidebar ul.sidebar-menu.linkclass > li:nth-child(7)').click()
        time.sleep(3)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def filter(self):
        self.login()

        self.goToTopicsModule()

        #filter 1st Topic
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Drink coffee')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        #filter 2nd Topic
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        #filter 3rd Topic
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Testing video')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        self.logout()

    def attachment(self):
        self.login()

        self.goToTopicsModule()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(3) a.showAttachment > i.fa.fa-eye').click()
        time.sleep(5)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.wrapper:nth-child(2) div.example-modal div.modal.attachmentModal.in div.modal-dialog div.modal-content div.modal-header button.close > span:nth-child(1)').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(5) td:nth-child(3) a.showAttachment > i.fa.fa-eye').click()
        time.sleep(5)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.wrapper:nth-child(2) div.example-modal div.modal.attachmentModal.in div.modal-dialog div.modal-content div.modal-header button.close > span:nth-child(1)').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.even-row:nth-child(4) td:nth-child(3) a.showAttachment > i.fa.fa-eye').click()
        time.sleep(5)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini.modal-open:nth-child(2) div.wrapper:nth-child(2) div.example-modal div.modal.attachmentModal.in div.modal-dialog div.modal-content div.modal-header button.close > span:nth-child(1)').click()
        time.sleep(2)

        self.logout()

    def viewTotalComment(self):
        self.login()

        self.goToTopicsModule()

        #click total comment
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(5) > a:nth-child(1)').click()
        time.sleep(5)

        #filter inside total comment
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('Nice')
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(4) section.content div.row div.col-xs-12 div.box:nth-child(2) div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(1)

        self.driver.find_element_by_link_text('Back').click()
        time.sleep(2)

        self.logout()

run = Topics()
run.filter()
run.attachment()
run.viewTotalComment()


