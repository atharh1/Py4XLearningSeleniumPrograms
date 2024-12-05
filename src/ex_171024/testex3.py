from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_options():
    options=Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=900,600")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    time.sleep(2)