import sys

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

class TestAmazonBestsellers():
    driver = ''

    def test_setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com')

    def test_amazon_bestsellers_link(self):
        self.driver.find_element(By.XPATH,"//div[@id='nav-xshop']/a[contains(@href, 'bestsellers')]").click()
        actual_links = self.driver.find_elements(By.XPATH, "//div[@id='zg_header']//li").text
        print(self.driver.find_elements(By.XPATH, "//div[@id='zg_header']//li").text)
        assert len(actual_links) == 7, f'Expected to see 5 bestseller headers, but got {len(actual_links)}'

    @pytest.mark.skip
    def test_amazon_find_dress(self):
        sch_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        sch_box.send_keys('pants for men', Keys.RETURN)
        expected_text = "pants for men"
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")

    @pytest.mark.skip(reason='test is skipped')
    def test_amazon_find_dress(self):
        sch_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        sch_box.send_keys('pants for men', Keys.RETURN)
        expected_text = "pants for men"
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")

    @pytest.mark.skipif(sys.version_info < (3, 7), reason='requires python 3.7 or higher')
    def test_skip_if_sys_version_lower(self):
        sch_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        sch_box.send_keys('pants for men', Keys.RETURN)
        expected_text = "pants for men"
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def teardown_method(self):
        self.driver.quit()
