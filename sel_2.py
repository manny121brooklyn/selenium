import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.google.com')

    def test_search_by_text(self):
        #get the search text box
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.send_keys('Selenium webdriver interview questions')
        search_field.submit()

        lists = driver.find_elements(By.CLASS_NAME, 'r')
        no = len(lists)
        print(no)
        self.assertEqual(11, len(lists))

    def test_search_by_name(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.send_keys('Python class')
        search_field.submit()
        list_new = driver.find_elements(By.CLASS_NAME, 'r')
        self.assertEqual(10, len(list_new))

    def tearDown(self):
        self.driver.quit()
#to run the tests from command line require us to add a call to the main() method
if __name__ == '__main__':
    unittest.main()
