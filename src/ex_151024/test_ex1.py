from selenium import webdriver

def test_ex():
    driver=webdriver.Firefox()
    driver.get("https://google.com")
    print(driver.title)