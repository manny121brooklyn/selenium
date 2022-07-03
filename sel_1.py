import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(1)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#identify dropdown with Select class

# sel = Select(driver.find_element(By.XPATH, "//select[@name='continents']"))
# sel.select_by_visible_text('Europe')
# time.sleep(1)
# sel.select_by_index(0)
# driver.close()

sel = driver.find_element(By.XPATH, "//select[@name='continents']")
drop_down = Select(sel)
drop_down.select_by_visible_text('Europe')
drop_down.select_by_index(0)
driver.quit()