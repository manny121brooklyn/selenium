from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_amazon_search():
    driver = webdriver.Chrome(executable_path='C:\selenium2\\drivers\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://www.amazon.com')
    sch_field = driver.find_element(By.ID, 'twotabsearchtextbox')
    sch_field.send_keys('dress', Keys.RETURN)

    expected_text = '"dress"'
    actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    print(driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text)
    assert expected_text == actual_text, f'Expected text{expected_text} and actual text is {actual_text}'
    driver.quit()