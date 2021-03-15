import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def test_guest_should_see_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")
