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

class TestFgv():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_fgv(self):
    self.driver.get("https://comfy.ua/ua/")
    self.driver.set_window_size(1050, 748)
    element = self.driver.find_element(By.CSS_SELECTOR, ".header-bottom-profile__link > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".header-bottom-profile__link > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "c-1248").click()
    self.driver.find_element(By.ID, "c-1248").send_keys("+38(068)-220-01-22")
    self.driver.find_element(By.CSS_SELECTOR, ".cmf-button-primary").click()
  
test = TestFgv()
test.setup_method(1)
test.teardown_method(1)
test.test_fgv()