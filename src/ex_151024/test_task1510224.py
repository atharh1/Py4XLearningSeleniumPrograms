from selenium import webdriver
import allure
import pytest

@allure.title("Sample test task")
def test_task1():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    assert driver.title=="CURA Healthcare Service"
    print(driver.current_url)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    #print(driver.page_source)
    #assert driver.page_source=="CURA Healthcare Service"