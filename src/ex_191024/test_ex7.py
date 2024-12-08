import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_anchorlink_tc():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    start_free_trail_link_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    start_free_trail_link_element.click()
    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.back()
    time.sleep(3)
    assert driver.current_url=="https://app.vwo.com/#/login"
    time.sleep(3)
    start_free_trail_partial_link_element=driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    start_free_trail_partial_link_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
