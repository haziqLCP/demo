from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Product:

    def seleniumSetup(self):
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
    def chooseArea(self):

        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 > div.nice-select.select-area:nth-child(3)').click()
        time.sleep(1)

    def scrollCategories(self):

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)

    """<--------------------------------Test Cases Section----------------------------------->"""
    def productGeneral(self):
        self.login()

        self.driver.find_element_by_link_text('MY ORDER').click()
        time.sleep(1)

        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)

        """Delivery Service"""
        #click delivery service (Delivery)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-3.order-2 div.sidebar-area div.sidebar.mb-35:nth-child(1) label.container1:nth-child(3) > span.checkmark:nth-child(2)').click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-3.order-2 div.sidebar-area div.sidebar.mb-35:nth-child(1) label.container1:nth-child(3) > span.checkmark:nth-child(2)').click()
        time.sleep(1)

        #click delivery service (Self pickup)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-3.order-2 div.sidebar-area div.sidebar.mb-35:nth-child(1) label.container1:nth-child(2) > span.checkmark:nth-child(2)').click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,2500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-3.order-2 div.sidebar-area div.sidebar.mb-35:nth-child(1) label.container1:nth-child(3) > span.checkmark:nth-child(2)').click()
        time.sleep(1)

        """Area"""
        #choose Area
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(2)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(3)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(4)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(5)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(6)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(7)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(10)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(11)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(12)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(13)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(14)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(15)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(33)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(34)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(67)').click()
        time.sleep(2)
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(74)').click()
        time.sleep(2)

        #back to all data
        self.chooseArea()
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-4.col-md-4.col-sm-12.d-flex.align-items-center div.view-mode-icons.mb-xs-10 div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.select-area.open:nth-child(3) ul.list > li.option:nth-child(1)').click()
        time.sleep(2)

        """Sort By"""
        self.driver.refresh()
        time.sleep(2)

        #by defaults, system already sort by price
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        #sort by price: Low to High
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 > div.nice-select.price-sort:nth-child(3)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.price-sort.open:nth-child(3) ul.list > li.option:nth-child(2)').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,250)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        #sort by price: High to Low
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 > div.nice-select.price-sort:nth-child(3)').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-header.mb-35 div.row div.col-lg-8.col-md-8.col-sm-12.d-flex.flex-column.flex-sm-row.justify-content-between.align-items-left.align-items-sm-center div.sort-by-dropdown.d-flex.align-items-center.mb-xs-10 div.nice-select.price-sort.open:nth-child(3) ul.list > li.option:nth-child(3)').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,250)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(2) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        """Favourite"""
        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,250)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

        #favourite first method
        self.driver.execute_script("window.scrollTo(0,370)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div.ttip:nth-child(3) > a:nth-child(1)').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,370)")
        time.sleep(1)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div.ttip:nth-child(3) > a:nth-child(1)').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,370)")
        time.sleep(2)

        #favourite second method
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12:nth-child(3) div.gf-product.shop-grid-view-product div.ttip:nth-child(3) > a:nth-child(1)').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,370)")
        time.sleep(1)
        self.driver.find_element_by_partial_link_text('FAVOURI').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('My Favourite').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,370)")
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(2) div.container div.row div.col-lg-12.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-3.col-lg-3.col-md-6.col-sm-6.col-12:nth-child(3) div:nth-child(1) div.gf-product.shop-grid-view-product span:nth-child(4) a:nth-child(1) > i.fas.fa-times-circle').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,370)")
        time.sleep(1)

        self.driver.close()

    def productCategories(self):
        self.login()

        self.driver.find_element_by_link_text('MY ORDER').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('PRODUCTS').click()
        time.sleep(1)

        self.driver.find_element_by_link_text('Bakery/Bread').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Vegetable').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Fruits').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Fast Food').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Shushi').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Drinks').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Korean Food').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Bento Box').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Ligtning').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Major Appliance').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Small Appliances').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('IT equitment').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Jackets & Coats').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Trouser & Shorts').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Suits').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Underwear').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Skirts and dress').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Shoes/boots/slippers').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Parts of shoes,boots and slipers').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Sweaters and waistcoasts').click()
        self.scrollCategories()
        self.driver.find_element_by_link_text('Others').click()
        self.scrollCategories()

        self.driver.close()

    def searchTopBar(self):
        self.login()

        #1st search
        self.driver.find_element_by_css_selector('#global_search').send_keys('logitech')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#search_result_btn').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12 div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        self.driver.execute_script("window.scrollTo(0,280)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element_by_css_selector('#global_search').clear()
        time.sleep(1)

        #2nd search
        self.driver.find_element_by_css_selector('#global_search').send_keys('chicken')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#search_result_btn').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12 div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        self.driver.execute_script("window.scrollTo(0,280)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element_by_css_selector('#global_search').clear()
        time.sleep(1)

        #3rd Search
        self.driver.find_element_by_css_selector('#global_search').send_keys('Basket')
        time.sleep(1)
        self.driver.find_element_by_css_selector('#search_result_btn').click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(2)
        self.driver.find_element_by_css_selector('div.wrapper:nth-child(1) div.shop-page-container.mb-50:nth-child(3) div.container div.row div.col-lg-9.order-1.mb-sm-35.mb-xs-35 div.shop-product-wrap.grid.row.no-gutters.mb-35 div.col-xl-4.col-lg-4.col-md-6.col-sm-6.col-12 div.gf-product.shop-grid-view-product div:nth-child(1) div.image a:nth-child(1) > img.img-fluid').click()
        self.driver.execute_script("window.scrollTo(0,280)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element_by_css_selector('#global_search').clear()

        self.driver.close()


#Run Command
run = Product()
# run.productGeneral()
# run.productCategories()
# run.searchTopBar()


