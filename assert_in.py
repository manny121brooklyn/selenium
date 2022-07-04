import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# class TestStringMethods(unittest.TestCase):
#     def test_negative(self):
#         key = 'and'
#         container = 'mansur'
#         message = 'key is not in container'
#         self.assertIn(key, container, message)
#
# if __name__ == '__main__':
#     unittest.main()


# class TestStringMethods(unittest.TestCase):
#     def test_positive(self):
#         key = 'ansu'
#         container = 'mansur'
#         message = 'key is not in container'
#         self.assertIn(key, container, message)
#
# if __name__ == '__main__':
#     unittest.main()

class TestStringMethods(unittest.TestCase):
    def test_positive(self):
        self.assertIn('ansu', 'mansur', 'ansur is in mansur')

if __name__ == '__main__':
    unittest.main()
