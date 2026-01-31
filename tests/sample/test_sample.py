import time
import allure
from selenium import webdriver

@allure.title("Dry run of pass testcases")
@allure.description("TC#1 Dry run of pass testcases")
def test_sample_pass():
    print("Hi")
    assert True == True

@allure.title("Dry run of failed testcases")
@allure.description("TC#2 Dry run of failed testcases")
def test_sample_failed():
    print("Hi")
    assert True == False