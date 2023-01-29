import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Users/Nitish/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service = s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

time.sleep(2)

max = 500
current = 0

while current < max:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)
    ##app > main > div:nth-child(1) > div:nth-child(4) > div.sm-products.list.size-m.img-wide > div:nth-child(1)
    print(len(driver.find_elements(by=By.XPATH, value='//*[@id="app"]')))

#html = driver.page_source

#with open('smartprix.html','w',encoding='utf-8') as f:
    #f.write(html)

