import allure
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_invalid_username_password():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    username_textbox_element=driver.find_element(By.NAME,"username")
    username_textbox_element.send_keys("abc@gmail.com")
    password_textbox_element=driver.find_element(By.ID,"login-password")
    password_textbox_element.send_keys("password@1234")
    sign_in_button_element=driver.find_element(By.ID,"js-login-btn")
    sign_in_button_element.click()
    time.sleep(5)
    error_message_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    assert error_message_element.text=="Your email, password, IP address or location did not match"
    time.sleep(5)

