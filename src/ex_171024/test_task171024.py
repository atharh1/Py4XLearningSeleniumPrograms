from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_task17oct():
    options=Options()
    options.add_argument("--start-maximized")
    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    username_textbox_element=driver.find_element(By.ID,"txt-username")
    username_textbox_element.send_keys("John Doe")
    password_textbox_element=driver.find_element(By.ID,"txt-password")
    password_textbox_element.send_keys("ThisIsNotAPassword")
    login_button_element=driver.find_element(By.ID,"btn-login")
    login_button_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
