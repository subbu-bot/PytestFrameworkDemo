import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def slow_type(element, text, delay=0.2):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # Pause between keystrokes


def test_typing_slowly():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    username_field = driver.find_element(By.NAME,'username')

    # Simulate slow typing
    slow_type(username_field, "bulbul", delay=0.3)
    driver.quit()
