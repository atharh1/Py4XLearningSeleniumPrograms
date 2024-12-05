from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.title("Chrome Test case")
@allure.description("Chrome Parallel Test case1")
def test_parallel_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"

@allure.title("Edge Test Case ")
@allure.description("Edge Parallel Test Case")
def test_parallel_edge():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"

@allure.title("Firefox Test Case ")
@allure.description("Firefox Parallel Test Case")
def test_parallel_firefox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"