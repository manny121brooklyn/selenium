from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://www.google.com')
print(f'Current page title is{driver.title}')
sch_field = driver.find_element(By.NAME, 'q')
sch_field.send_keys('Python tuttorial')
sch_field.submit()
driver.get('https://www.python.org')
time.sleep(2)
print(f'Current page title is {driver.title}')
driver.execute_script('window.history.go(-1)')
print(f'Current page title is {driver.title}')

driver.quit()
