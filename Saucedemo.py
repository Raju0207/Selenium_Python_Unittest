import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class Base_Page(unittest.TestCase):
    driver = None

    def setUp(self):
        service_chrome = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(120)
        print("I am running first")

    def tearDown(self):
        print("I am running at the last")
        self.driver.close()
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(10)
        textValue = self.driver.find_element(By.XPATH, '//div[@class ="app_logo"]').text
        assert textValue == 'Swag Labs'
        time.sleep(2)
        print("I am running after setUp method and before tearDown method")
        # self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
        # self.driver.find_element(By.ID, 'logout_sidebar_link').click()

    def test_invalid_login_with_blank(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(10)
        textValue = self.driver.find_element(By.XPATH, '//h3').text
        assert textValue == 'Epic sadface: Username is required'
        time.sleep(5)
        print(textValue)

    def test_invalid_login_with_wrong_user_name(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(10)
        textValue1 = self.driver.find_element(By.XPATH, '//h3').text
        assert textValue1 == 'Epic sadface: Username and password do not match any user in this service'
        time.sleep(5)
        print(textValue1)


    def test_invalid_login_with_wrong_password(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret')
        self.driver.find_element(By.ID, 'login-button').click()
        time.sleep(10)
        textValue2 = self.driver.find_element(By.XPATH, '//h3').text
        assert textValue2 == 'Epic sadface: Username and password do not match any user in this service'
        time.sleep(5)
        print(textValue2)




# driver = webdriver.Chrome()
# #time.sleep(5)
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
#
# driver.find_element(By.ID, 'user-name').send_keys('standard_user')
# driver.find_element(By.ID, 'password').send_keys('secret_sauce')
# driver.find_element(By.ID, 'login-button').click()
# time.sleep(10)
# textValue = driver.find_element(By.XPATH, '//div[@class ="app_logo"]').text
# assert textValue == 'Swag Labs'
# # textValue1 = driver.find_element(By.XPATH, "//strong").text
# # assert textValue1 == 'Congratulations student. You successfully logged in!'
# # textValue2 = driver.find_element(By.XPATH, '//a[@href ="https://practicetestautomation.com/practice-test-login/"]').text
# # assert textValue2 == 'Log out'