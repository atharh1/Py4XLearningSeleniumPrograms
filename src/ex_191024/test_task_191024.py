import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Task 19 OCT 2024 to use xpath")
@allure.description("Automation for the Registration Page of the AwesomeQA.com/UI")
def test_awesomeqa_registration_page():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    fn_textbox_element=driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    fn_textbox_element.send_keys("Ath")
    ln_textbox_element=driver.find_element(By.XPATH,"//input[@name='lastname']")
    ln_textbox_element.send_keys("Hus")
    email_textbox_element=driver.find_element(By.XPATH,"//input[@type='email']")
    email_textbox_element.send_keys("aa@aa.com")
    telephone_textbox_element=driver.find_element(By.XPATH,"//input[@placeholder='Telephone']")
    telephone_textbox_element.send_keys("123")
    password_textbox_element=driver.find_element(By.XPATH,"//input[@id='input-password']")
    password_textbox_element.send_keys("1234")
    password_textbox_confirm_element=driver.find_element(By.XPATH,"//input[@id='input-confirm']")
    password_textbox_confirm_element.send_keys("1234")
    checkbox_element = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox_element.click()
    continue_button_element=driver.find_element(By.XPATH,"//input[@class='btn btn-primary']")
    continue_button_element.click()
    time.sleep(3)
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"