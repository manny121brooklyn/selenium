from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path='C:\\selenium2\\geckodriver.exe')
driver.get('https://the-internet.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Frames').click()
driver.find_element(By.LINK_TEXT, 'Nested Frames').click()

#swtich to frame with name (find name by inspecting its code)
driver.switch_to.frame('frame-bottom')
bottom = driver.find_element(By.XPATH, '//body').text
print(bottom)
driver.switch_to.default_content()

driver.switch_to.frame('frame-left')
# leftFrame = driver.find_element(By.XPATH, "//left").text
# print(leftFrame)
driver.switch_to.default_content()

driver.switch_to.frame('frame-middle')
driver.switch_to.default_content()

driver.switch_to.frame('frame-right')
driver.switch_to.default_content()

driver.quit()

# https://the-internet.herokuapp.com/nested_frames
