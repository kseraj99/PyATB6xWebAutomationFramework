from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Page Locator

    user_name = (By.ID,"login-username")
    user_pass = (By.ID,"login-password")
    login_button = (By.ID,"js-login-btn")
    error_msg = (By.ID,"js-notification-box-msg")