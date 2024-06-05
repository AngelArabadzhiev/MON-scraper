import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://infopriem.mon.bg")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div/div[2]/div/a[6]").click()


def enter_username_password(username, password):
    user = driver.find_element(By.ID, "sn")
    user.click()
    user.send_keys(str(username), Keys.TAB)
    time.sleep(1)
    pswd = driver.find_element(By.ID, "webcode")
    pswd.click()
    pswd.send_keys(str(password), Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/div/div[2]/div/a[3]").click()


def wait_for_new():
    wait = WebDriverWait(driver, 10000000000)


name = input("Запиши твоят входящ номер: ")
access = input("Запиши твоят код за достъп: ")
enter_username_password(name, access)
wait_for_new()


