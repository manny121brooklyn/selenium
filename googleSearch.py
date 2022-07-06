from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.com')
# sch_field = driver.find_element(by=By.NAME, value='q')
sch_field = driver.find_element(By.NAME, 'q')
sch_field.send_keys('RD auto')
sch_field.submit()
time.sleep(2)
# sch_field.send_keys(Keys.BACK_SPACE)
sch_field.back()
sch_field.send_keys('omation')

sch_field.submit()
time.sleep(2)
