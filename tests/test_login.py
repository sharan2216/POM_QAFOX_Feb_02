import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(level=logging.INFO, filename="logfile.log",
                    format = "%(asctime)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)
handler=logging.FileHandler('test.log')
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("test the custom logger")

# //new comments added here
def test_login_with_valid_credentials():
    logging.info('Checking for test_login_with_valid_credentials')
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    driver.find_element(By.ID,"input-email").send_keys("sksharan666@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)
    actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
    expected_text="Edit your account information"
    assert actual_text.__eq__(expected_text)
    driver.quit()



def test_login_with_invalid_email_and_valid_password():
    logging.info('Checking for test_login_with_invalid_email_and_valid_password')
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    driver.find_element(By.ID,"input-email").send_keys(generate_email_with_time_stamp())
    # driver.find_element(By.ID, "input-email").send_keys("sksharan666000@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)
    # actual_text=driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
    # expected_text="Warning: No match for E-Mail Address and/or Password."
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    actual_warning_message = driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text
    assert expected_warning_message.__contains__(actual_warning_message)
    driver.quit()


def test_login_with_valid_email_and_invalid_password():
    logging.info('Checking for test_login_with_valid_email_and_invalid_password')
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    driver.find_element(By.ID,"input-email").send_keys("sksharan666000@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412000")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)
    # actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
    # expected_text="Edit your account information"
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    actual_warning_message = driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text
    assert expected_warning_message.__contains__(actual_warning_message)
    driver.quit()


def test_login_without_entering_credentials():
    logging.info('Checking for test_login_without_entering_credentials')
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    # driver.find_element(By.ID,"input-email").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.ID,"input-email").send_keys('')
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)
    # actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
    # expected_text="Edit your account information"
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    actual_warning_message = driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text
    assert expected_warning_message.__contains__(actual_warning_message)
    driver.quit()


def generate_email_with_time_stamp():
    logging.info('Checking for generate_email_with_time_stamp')
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "sksharan666"+time_stamp+"@gmail.com"