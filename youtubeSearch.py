from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe')
driver = webdriver.Firefox(executable_path='C:\\selenium2\\geckodriver.exe')
driver.maximize_window()
driver.get('https://www.youtube.com')
# search_field = driver.find_element(By.XPATH, "//input[@name='search_query']")
search_field = driver.find_element(by=By.XPATH, value="//input[@name='search_query']")
search_field.send_keys('RD auto')
search_field.submit()
time.sleep(2)
# search_field.send_keys(Keys.BACK_SPACE)
search_field.back()

# search_field.back()
search_field.send_keys('omation')
search_field.submit()
time.sleep(2)
driver.quit()
