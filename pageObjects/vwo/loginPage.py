from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.common_utils import webdriver_wait

from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Page Locator

    user_name = (By.ID,"login-username")
    user_pass = (By.ID,"login-password")
    login_button = (By.ID,"js-login-btn")
    error_msg = (By.ID,"js-notification-box-msg")
    free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")

    # Page Action

    def get_username(self):
        return self.driver.find_element(*LoginPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LoginPage.user_pass)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trail)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def login_to_vwo(self,usr,psw):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(psw)
            self.get_submit_button().click()
        except Exception as e:
            print(e)

    def get_error_message_as_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_msg, timeout=5)
        return self.get_error_message().text

    def free_trail_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)


