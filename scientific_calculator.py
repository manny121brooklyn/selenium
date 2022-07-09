from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get('https://www.tcsion.com/OnlineAssessment/ScientificCalculator/Calculator.html')
num1 = driver.find_element(By.ID, 'keyPad_btn9')
num1.click()
time.sleep(1)

opr1 = driver.find_element(By.ID, 'keyPad_btnMult')
opr1.click()
time.sleep(1)

num2 = driver.find_element(By.ID, 'keyPad_btn5')
num2.click()
time.sleep(1)

ans = driver.find_element(By.ID, 'keyPad_btnEnter')
ans.click()
time.sleep(1)

driver.quit()