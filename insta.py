import random
from time import sleep
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')

sleep(5)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("sandrostarr.art")
password_input.send_keys("5andr5wagm0ney0ne")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(8)

# search_input = browser.find_element_by_class_name("x3qfX")
# search_input.send_keys("#abstractart")
# search_input.submit()

browser.get('https://www.instagram.com/explore/tags/abstractart/')

sleep(8)


browser.find_elements_by_class_name('v1Nh3')[9].click() # click on photo to open and upload


item = 1
likes = 40
while item <= likes: # loop with how many photos to like

    sleep(random.uniform(3, 7))

    if random.randint(1, 5) != 5:
        browser.find_element_by_class_name('fr66n').click() # click the like button

    sleep(random.uniform(1, 3))
    browser.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
    item = item + 1

print(f'Number of photos liked: \033[0;33m{item - 1}\033[m')

# sleep(15)

# browser.close()    
# 
