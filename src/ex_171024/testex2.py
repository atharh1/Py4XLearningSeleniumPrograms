from selenium import webdriver

def test_pagesource():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert "CURA Healthcare Service" in driver.page_source
