# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginusername1():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginusername1(self):
    # Test name: login_username_1
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.saucedemo.com/")
    # 2 | setWindowSize | 706x728 | 
    self.driver.set_window_size(706, 728)
    # 3 | click | css=*[data-test="username"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    # 4 | type | css=*[data-test="username"] | standard_user
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    # 5 | click | css=*[data-test="password"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    # 6 | type | css=*[data-test="password"] | secret_sauce
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    # 7 | click | id=logout_sidebar_link | 
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
    # 8 | click | css=*[data-test="login-button"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
  