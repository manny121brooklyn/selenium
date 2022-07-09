from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.youtube.com')
sch_field = driver.find_element(By.NAME, 'search_query')
sch_field.send_keys('Python Tuttorial')
sch_field.submit()
time.sleep(2)

driver.back()
time.sleep(2)
sch_field = driver.find_element(By.NAME, 'search_query')
sch_field.send_keys('Postman tuttorials')
time.sleep(2)

driver.quit()
