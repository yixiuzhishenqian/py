from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.bilibili.com/")
sleep(3)

search = driver.find_elements(By.CSS_SELECTOR, '.nav-search-input')
btn = driver.find_elements(By.CSS_SELECTOR, '.nav-search-btn')
# driver.find_ele
search[0].send_keys('说唱新世代')
sleep(1)
btn[0].click()

sleep(30)
