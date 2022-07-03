import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#negative test case
class TestingMethods(unittest.TestCase):
   def test_negative(self):
       firstValue = 'mansur'
       secondValue = 'mansu'
       #error message in case if test case fails
       message = 'First value and second value are not equal!'
       self.assertEqual(firstValue, secondValue, message)
if __name__=='__main__':
    unittest.main()


'''
assertEqual() is used in unit testing to check equality of two values
it takes three parameters as input and returns boolean value True or False
syntax: self.assertEqual(firtvalue, secondvalue, message
'''

class TestMethods(unittest.TestCase):
    def test_positive(self):
        firstValue = 'mansur'
        secondValue = 'mansur'
        message = 'First and second values are equal!'
        self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
    unittest.main()