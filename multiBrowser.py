from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path='C:\selenium2\drivers\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path='C:\\selenium2\\geckodriver.exe')
# driver = webdriver.Edge(executable_path='C:/selenium2/m)
# driver = webdriver.Ie(executable_path='C:/selenium2/IEDriverServer.exe')
driver.get('http://www.google.com')
#print title of the page
print(f'Title of this website is {driver.title}')
#print current URL
print(f'Current URL address is {driver.current_url}')
#print page source of the web page
print(f'This is page source of the page {driver.page_source}')

driver.quit()


