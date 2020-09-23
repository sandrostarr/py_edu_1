from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')

sleep(5)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("<имя пользователя>")
password_input.send_keys("<пароль>")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(15)

browser.close()