import time

# Allure is used for generating beautiful test reports
import allure

# Pytest is the test framework
import pytest

# Selenium WebDriver to automate browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Project level constants (URL etc.)
from constants.constants import Constants
from pageObjects.vwo.freeTrailPage import FreeTrialPage

# Page Object classes
from pageObjects.vwo.loginPage import LoginPage
from pageObjects.vwo.dashboardPage import DashboardPage

# For loading environment variables from .env file
from dotenv import load_dotenv
import os

# Utility functions (like screenshot)
from utils.utils import *


# ---------------- FIXTURE SETUP ----------------
# This fixture runs before every test that uses it
@pytest.fixture
def setup():

    # Load values from .env file (username, password etc.)
    load_dotenv()

    # Launch Chrome browser
    driver = webdriver.Edge()

    # Maximize the browser window
    driver.maximize_window()

    # Open application URL
    driver.get(Constants.app_url())

    # Return driver so tests can use it
    return driver

@allure.title("VWO Free Trail")
@allure.description("vwo free trail Check")
@allure.feature("Feature: vwo free tail")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.free_trail_button_click()
    take_screen_shot(driver= driver, name="test vwo ft negative")
    free_trail_page = FreeTrialPage(driver)
    free_trail_page.enter_free_trial_details_invalid("aman")
    error_msg_text = free_trail_page.get_error_message_text()
    assert error_msg_text == "The email address you entered is incorrect."
    driver.quit()
