from selenium import webdriver
import time

class AdminRoles:

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
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) header.main-header nav.navbar.navbar-static-top div.navbar-custom-menu ul.nav.navbar-nav li.dropdown.user.user-menu > a.dropdown-toggle').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) header.main-header nav.navbar.navbar-static-top div.navbar-custom-menu ul.nav.navbar-nav li.dropdown.user.user-menu.open ul.dropdown-menu li.user-footer div.pull-right > a.btn.btn-default.btn-flat').click()
        time.sleep(3)

        self.driver.close()

    def goToAdminRolesModule(self):
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar:nth-child(2) section.sidebar ul.sidebar-menu.linkclass li.treeview:nth-child(2) a:nth-child(1) > span:nth-child(2)').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            'body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) aside.main-sidebar:nth-child(2) section.sidebar ul.sidebar-menu.linkclass li.treeview.active:nth-child(2) ul.treeview-menu.menu-open:nth-child(2) li:nth-child(2) > a:nth-child(1)').click()
        time.sleep(3)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def createNewRoles(self):
        self.login()

        #scroll Dashboard
        self.driver.execute_script("window.scrollTo(0,450)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        self.goToAdminRolesModule()

        #filter
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').send_keys('tes')
        time.sleep(3)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-header div.dataTables_filter label:nth-child(1) > input.form-control.form-control-sm:nth-child(2)').clear()
        time.sleep(2)

        #add roles
        self.driver.find_element_by_css_selector('#addrole').click()
        time.sleep(1)

        #click cancel button
        self.driver.find_element_by_css_selector('#btnCancel').click()
        time.sleep(1)

        #add roles
        self.driver.find_element_by_css_selector('#addrole').click()
        time.sleep(1)

        #fill in form
        self.driver.find_element_by_css_selector('#role_name').send_keys('Manual Tester') #please change this name
        self.driver.find_element_by_css_selector('#status').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-6:nth-child(3) select.form-control:nth-child(2) > option:nth-child(1)').click()
        time.sleep(1)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(1) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(2) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(4) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(5) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(6) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(7) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(9) td:nth-child(3) > button.btn.btn-xs.btn-rounded.border-info.text-info.btn-flat.getRelativePermission').click()
        time.sleep(2)

        #click save button
        self.driver.find_element_by_css_selector('#btnSubmit').click()
        time.sleep(2)

        self.logout()

    def updateStatus(self):
        self.login()

        self.goToAdminRolesModule()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(4) > select.active-role').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(4) select.active-role > option:nth-child(2)').click()
        time.sleep(3)

        self.driver.refresh()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(4) > select.active-role').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(4) select.active-role > option:nth-child(1)').click()
        time.sleep(7)

        self.logout()

    def editRoles(self):
        self.login()

        self.goToAdminRolesModule()

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(5) a:nth-child(1) > i.fa.fa-fw.fa-edit').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#role_name').clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#role_name').send_keys('Automation Tester')
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,350)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(6) td:nth-child(2) div.checkbox-custom.checkbox-primary.pull-xs-left:nth-child(2) > input:nth-child(1)').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper:nth-child(3) section.content div.row div.col-md-12 div.box.box-primary div.box-body form.form-horizontal div.box-body div.row div.col-md-12:nth-child(4) table.table tbody:nth-child(2) tr:nth-child(5) td:nth-child(2) div.checkbox-custom.checkbox-primary.pull-xs-left:nth-child(2) > input:nth-child(1)').click()
        time.sleep(1)

        self.driver.find_element_by_css_selector('#btnSubmit').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('body.skin-red.sidebar-mini:nth-child(2) div.wrapper:nth-child(2) div.content-wrapper section.content div.row div.col-xs-12 div.box div.box-body div.dataTables_wrapper.dt-bootstrap4.no-footer div.datatable-scroll-wrap table.table.table-bordered.table-striped.dataTable.no-footer.dtr-inline tbody:nth-child(2) tr.alpha-slate:nth-child(1) td:nth-child(5) a:nth-child(1) > i.fa.fa-fw.fa-edit').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        self.driver.refresh()
        time.sleep(2)

        self.logout()

run = AdminRoles()
# run.createNewRoles()
# run.updateStatus()
# run.editRoles()


