from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = ""  # YOUR CHROMEDRIVER.EXE LOCATION
USERNAME = ''  # YOUR INSTAGRAM USERNAME
PASSWORD = ''  # YOUR INSTAGRAM PASSWORD
SEARCH_ACCOUNT = ''  # Account name that you would like to search

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get('https://www.instagram.com/accounts/login/')
driver.maximize_window()
time.sleep(5)

# --------------------------------------- LOGIN TO INSTAGRAM-------------------------------------------------

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys(USERNAME)
password.send_keys(PASSWORD)

login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

time.sleep(5)

# ------------------------------ SEARCH AN ACCOUNT TO FOLLOW ITS FOLLOWERS-----------------------------------
search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys(SEARCH_ACCOUNT)

time.sleep(2)

search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)

time.sleep(5)

# ------------------------------------ FOLLOW THE USERS ON THIS ACCOUNT ------------------------------------

following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
following.click()

time.sleep(3)

to_be_followed = driver.find_elements_by_css_selector('.isgrP ul div li div button')
for follow in to_be_followed:
    follow.click()
    time.sleep(2)

# -------------- UNCOMMENT THE CODE BELOW TO ALSO USE THE UNFOLLOW FUNCTIONALITY OF THE BOT----------------


# to_unfollow = driver.find_elements_by_css_selector('.isgrP ul div li div button')
# for unfollow in to_unfollow[1:]:
#     unfollow.click()
#     time.sleep(3)
#     confirm_unfollow = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
#     confirm_unfollow.click()
#     time.sleep(2)


driver.quit()
