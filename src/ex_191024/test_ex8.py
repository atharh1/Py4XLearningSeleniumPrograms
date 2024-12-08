import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Find all buttons with links/tags")
def testfindallbuttonswithlink():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    all_anchor_elements=driver.find_elements(By.TAG_NAME,"a")
    print(len(all_anchor_elements))
    for i in all_anchor_elements:
        print(i.text)
    all_elements=driver.find_elements(By.TAG_NAME,"button")
    print(" No of elements ",len(all_elements))
    for i in all_elements:
        print(i.text)