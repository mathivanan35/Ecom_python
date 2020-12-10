import time
from maintain.Base import base
from locators import locators_address, locators_buyNow, locators_search, locators_payment
from maintain.readSheet import read
import pytest


def test_search():
    b = base()
    driver = b.getDriver()
    driver.get("https://www.flipkart.com/")
    driver.implicitly_wait(150)
    driver.maximize_window()
    b.clk(locators_search.btn_close_xpath)
    b.type(locators_search.txt_search_xpath, read(4, 2))
    b.clk(locators_search.btn_searchIcon_xpath)
    b.clk(locators_search.btn_selectProduct_xpath)

    h = driver.window_handles
    for i in h:
        if i != driver.current_window_handle:
            driver.switch_to.window(i)

    b.clk(locators_buyNow.btn_buynow_xpath)
    b.type(locators_buyNow.txt_userId_xpath, read(1, 2))
    b.clk(locators_buyNow.btn_continue_xpath)
    b.type(locators_buyNow.txt_password_xpath, read(2, 2))
    b.clk(locators_buyNow.btn_login_xpath)

    b.clk(locators_address.btn_addAddress_xpath)
    b.type(locators_address.txt_name_xpath, read(6, 2))
    b.type(locators_address.txt_mobile_xpath, read(7, 2))
    b.type(locators_address.txt_pincode_xpath, read(8, 2))
    b.type(locators_address.txt_locality_xpath, read(9, 2))
    b.type(locators_address.txt_areaAddress_xpath, read(10, 2))
    time.sleep(4)
    # b.type(locators_address.txt_city_xpath, read(11, 2))
    b.option(locators_address.dropdown_state_xpath, read(12, 2))
    b.clk(locators_address.btn_addressType_xpath)
    b.clk(locators_address.btn_saveAndDeliverHere_xpath)
    b.clk(locators_address.btn_continueToPayment_xpath)

    b.clk(locators_payment.btn_creditCard_xpath)
    b.type(locators_payment.txt_cardNo_xpath, read(14, 2))
    b.option(locators_payment.dropdown_month_xpath, read(15, 2))
    # b.option_value(locators_payment.dropdown_year_xpath, read(16, 2))
    # b.type(locators_payment.txt_CVV_xpath, read(17, 2))
