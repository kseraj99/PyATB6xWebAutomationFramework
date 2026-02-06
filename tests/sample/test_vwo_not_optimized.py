import allure
import time
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from utils.utils import take_screen_shot



@allure.title("vwo Login Negative Testcase")
@allure.description("TC#1 vwo login with invalid credential")
@allure.feature("vwo login with invalid credential")
def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)

        case "edge":
            edge_options = Options()
            edge_options.add_argument("--inprivate")
            driver = webdriver.Edge(options=edge_options)

        case _:
            print("Browser not found")
            exit(1)
    driver.maximize_window()
    driver.get(os.getenv("URL"))

    user_email = driver.find_element(By.ID,"login-username")
    user_email.send_keys(os.getenv("INVALID_USERNAME"))

    user_pass = driver.find_element(By.ID,"login-password")
    user_pass.send_keys(os.getenv("INVALID_PASSWORD"))

    login_button = driver.find_element(By.ID,"js-login-btn")
    login_button.click()

    time.sleep(2)
    error_msg = driver.find_element(By.ID,"js-notification-box-msg").text
    print(error_msg)

    take_screen_shot(driver=driver, name="vwo login step1")

    assert error_msg == os.getenv("error_message_expected")


    time.sleep(2)
    driver.quit()


