# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/Nitish/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service = s)

driver.get('http://google.com')
time.sleep(2)

# fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
user_input.send_keys('Campusx')
time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a')
link.click()

time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/section[2]/a[5]')
link2.click()
