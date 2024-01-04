
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_the_button(browser):
    browser.get(link)
    button = len(browser.find_elements(By.XPATH, "//button[@type='submit' and @class='btn btn-lg btn-primary btn-add-to-basket']"))
    time.sleep(5)
    assert button > 0, "че считать то, кнопки нет"


