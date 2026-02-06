from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants.constants import Constants






def webdriver_wait(driver, element_tuple):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element_tuple))


def webdriver_wait(driver, element_tuple, timeout):
    WebDriverWait(driver, timeout= timeout).until(EC.visibility_of_element_located(element_tuple))

def webdriver_wait_url(driver, timeout):
    WebDriverWait(driver, timeout= timeout).until(EC.url_changes(Constants.app_dashboard_url()))

