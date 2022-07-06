from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options=Options()
options.headless = True
driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe', options=options)
driver.get('https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys('Python tuttorial')
print(driver.title)
driver.quit()