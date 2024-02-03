import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.mark.usefixtures("setup_and_teardown")
@pytest.fixture()
def setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    yield
    driver.quit()


def test_register_with_mandate_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Arun")
    driver.find_element(By.ID, "input-lastname").send_keys("Lal")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("1234546")
    driver.find_element(By.ID, "input-confirm").send_keys("123456")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(3)
    expected_text = "Register Account"
    print("-------------")
    print(driver.find_element(By.XPATH, "//div[@id='content']/h1").text)
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)


# ------------------------------------------------------------------------------------------------

def test_register_with_all_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Arun")
    driver.find_element(By.ID, "input-lastname").send_keys("Lal")
    driver.find_element(By.ID, "input-email").send_keys("arunlala123@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("1234546")
    driver.find_element(By.ID, "input-confirm").send_keys("123456")
    driver.find_element(By.XPATH, "//input[@value=1][@name='newsletter']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(3)
    expected_heading_text = "Register Account"
    print("-------------")
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)


# ------------------------------------------------------------------------------------------------
def test_register_with_duplicate_email(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Arun")
    driver.find_element(By.ID, "input-lastname").send_keys("Lal")
    driver.find_element(By.ID, "input-email").send_keys("arunlala123@gmail.com")
    # print(generate_email_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    driver.find_element(By.ID, "input-password").send_keys("1234546")
    driver.find_element(By.ID, "input-confirm").send_keys("123456")
    driver.find_element(By.XPATH, "//input[@value=1][@name='newsletter']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(3)
    expected_warning_message = "Warning: E-Mail Address is already registered!"
    print("-------------")
    assert driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
        expected_warning_message)


# ------------------------------------------------------------------------------------------------
def test_register_without_entering_any_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("")
    driver.find_element(By.ID, "input-lastname").send_keys("")
    driver.find_element(By.ID, "input-email").send_keys("")
    # print(generate_email_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.ID, "input-confirm").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(3)
    print("-------------")
    expected_privacy_warning_message = "Warning: You must agree to the Privacy Policy!"
    assert driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
        expected_privacy_warning_message)
    # assert register_page.retrieve_privacy_policy_warning().__conatains__(expected_privacy_warning_message)
    time.sleep(3)
    expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
    # assert register_page.retrieve_first_name_warning().__eq__(expected_first_name_warning_message )
    assert driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(
        expected_first_name_warning_message)
    time.sleep(3)

    expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
    # assert register_page.retrieve_last_name_warning().__eq__(expected_last_name_warning_message)
    assert driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
        expected_last_name_warning_message)
    time.sleep(3)

    expected_email_address_warning_message = "E-Mail Address does not appear to be valid!"
    # assert register_page.retrieve_email_warning().__eq__(expected_email_address_warning_message)
    assert driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
        expected_email_address_warning_message)
    time.sleep(3)

    expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
    # assert register_page.retrieve_telephone_warning().__eq__(expected_telephone_warning_message)
    assert driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
        expected_telephone_warning_message)
    time.sleep(3)

    expected_password_warning_message = "Password must be between 4 and 20 characters!"
    # assert register_page.retrieve_password_warning().__eq__(expected_telephone_warning_message)
    assert driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
        expected_password_warning_message)
    time.sleep(3)

    # ------------------------------------------------------------------------------------------------
def generate_email_timestamp():
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "arun" + timestamp + "@gmail.com"