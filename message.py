from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import sys

def automate_message(n, mess):
    cService = webdriver.ChromeService(executable_path='your chromedriver.exe file path')
    driver = webdriver.Chrome(service = cService)

    driver.get("https://linkedin.com")

    time.sleep(2)

    username = driver.find_element("xpath", "//input[@name='session_key']")
    password = driver.find_element("xpath", "//input[@name='session_password']")

    username.send_keys("your linkedin user email")
    password.send_keys("your linkedin password")

    time.sleep(2)

    submit = driver.find_element("xpath", "//button[@type='submit']").click()

    time.sleep(2)

    network = driver.find_element("xpath", "//a[@href ='https://www.linkedin.com/mynetwork/?']")
    print(network)
    network.click()

    time.sleep(2)

    connections = driver.find_element("xpath", "//a[@href ='/mynetwork/invite-connect/connections/']")
    connections.click()

    time.sleep(2)

    search = driver.find_element("xpath", "//input[@id='mn-connections-search-input']")
    search.send_keys(n)

    time.sleep(2)

    initiate_message = driver.find_element("xpath", f"//button[@aria-label='Send a message to {n}']").click()

    time.sleep(2)

    message_div = driver.find_element("xpath", "//div[starts-with(@class, 'msg-form__msg-content-container')]")
    message_div.click()

    time.sleep(2)

    message_text_div = driver.find_element("xpath", "//div[@aria-label='Write a message…']")
    message_para = message_text_div.find_element("xpath", './/p')
    message_para.send_keys(mess)

    time.sleep(2)
    message_submit = driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(2)

def send_multiple(names, mess):
    for i in names:
         automate_message(i, mess)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        exit(0)
    
    send_multiple(sys.argv[1:], "your message")
