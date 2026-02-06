# assertion and page object class
# Webdriver start
# user interaction+Assertion
# close driver
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
    driver = webdriver.Chrome()

    # Maximize the browser window
    driver.maximize_window()

    # Open application URL
    driver.get(Constants.app_url())

    # Return driver so tests can use it
    return driver


# ---------------- NEGATIVE LOGIN TEST ----------------
@allure.title("vwo Login Negative Testcase")
@allure.description("TC#1 vwo login with invalid credential")
@allure.feature("vwo login with invalid credential")
@allure.id("Jira Id-1234")
@pytest.mark.negative
def test_vwo_login_negative(setup):

    # Get driver from fixture
    driver = setup

    # Create object of Login Page
    login_page = LoginPage(driver)

    # Perform login using invalid credentials from .env file
    login_page.login_to_vwo(
        usr=os.getenv("INVALID_USERNAME"),
        psw=os.getenv("INVALID_PASSWORD")
    )

    # Fetch error message shown on UI
    error_msg_element_text = login_page.get_error_message_as_text()

    # Take screenshot for report/debugging
    take_screen_shot(driver=driver, name="test vwo login negative")

    # Validate actual error message with expected one
    assert error_msg_element_text == os.getenv("error_message_expected")

    driver.quit()

# ---------------- POSITIVE LOGIN TEST ----------------

# Allure title shown in the report for this test case
@allure.title("vwo Login Testcase")

# Detailed description in Allure report
@allure.description("TC#1 vwo login with valid credential")

# Feature grouping in Allure report
@allure.feature("vwo login with valid credential")

# Pytest marker to categorize this as a positive test case
@pytest.mark.positive
def test_vwo_login_positive(setup):

    # Getting the WebDriver instance from pytest fixture (browser setup)
    driver = setup

    # Creating object of LoginPage (Page Object Model)
    login_page = LoginPage(driver)

    # Performing login using username & password from .env file
    login_page.login_to_vwo(
        usr=os.getenv("USERNAME_NEW"),   # Fetch username securely from environment variable
        psw=os.getenv("PASSWORD")        # Fetch password securely from environment variable
    )

    # Creating object of DashboardPage after successful login
    dashboard_page = DashboardPage(driver=driver)

    # Getting the logged-in user's name displayed on dashboard
    user_name = dashboard_page.user_logged_in_text()

    # Taking screenshot for evidence in test report
    take_screen_shot(driver=driver, name="test vwo login positive")

    # Validating actual logged-in user with expected value from .env file
    assert os.getenv("LOGGED_IN_USER") == user_name

    # Closing the browser after test execution
    driver.quit()

