from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path='C:\selenium2\geckodriver.exe')
driver.get('https://earth.google.com/web/')

try:
    wait = WebDriverWait(driver, 20)
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sign-in-button']/earth-i18n")))
    btn.click()
finally:

    driver.quit()