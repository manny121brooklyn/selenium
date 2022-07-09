from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

#create object of webdriver
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
#navigate to URL
driver.get('https://www.amazon.com')

#find search_box by id
sch_field = driver.find_element(By. ID, 'twotabsearchtextbox')
sch_field.send_keys('dress', Keys.RETURN)


expected_text = '"dress"'
#check if expected text is equal to actual text
actual_text = driver.find_element\
    (By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text)

assert expected_text == actual_text, f'Expected text is{expected_text}, but actual text is {actual_text}'
driver.quit()

