from asyncio import timeout

from dotenv import set_key
# Dashboard Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from utils.common_utils import webdriver_wait


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    user_logged_in = (By.XPATH, "//h6[normalize-space()='Global']")

    def get_user_logged_in(self):
        webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=5)
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple= self.user_logged_in, timeout=5)
        return self.get_user_logged_in().text
