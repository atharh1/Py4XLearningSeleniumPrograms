from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_exfindelementbyid():
    options=Options()
    options.add_argument("--start-maximized")
    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"