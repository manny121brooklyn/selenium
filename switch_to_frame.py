from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path='C:\\selenium2\\geckodriver.exe')
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html')
#switch to the first frame
driver.switch_to.frame('packageListFrame')
#click on the first frame
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.opera').click()
#back to default web page frame
driver.switch_to.default_content()
#switch to 2nd frame
driver.find_element(By.LINK_TEXT, 'OperaOptions').click()
#back to default web page frame
driver.switch_to.default_content()
#switch to 3rd frame
driver.switch_to.frame('classFrame')
#click on the second frame
driver.find_element(By.XPATH, '/html/body/div[1]/ul/li[4]/a')
time.sleep()
driver.close()