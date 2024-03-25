import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome()
# time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.find_element(By.ID, 'username').send_keys('student')
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.ID, 'submit').click()
time.sleep(5)
textValue = driver.find_element(By.XPATH, "//h1").text
assert textValue == 'Logged In Successfully'
textValue1 = driver.find_element(By.XPATH, "//strong").text
assert textValue1 == 'Congratulations student. You successfully logged in!'
textValue2 = driver.find_element(By.XPATH, '//a[@href ="https://practicetestautomation.com/practice-test-login/"]').text
assert textValue2 == 'Log out'




