import selenium
import time
import tkinter as tk
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

name = input("Твоят входящ номер: ")
access = input("Твоят код за достъп: ")
enter_username_password(name, access)

bulgarian_grade = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr[1]/td[3]")
math_grade = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/table/tbody/tr[2]/td[3]")


def waiting_for_update(value, check_interval):
    initial_value = value()
    while initial_value == value:
        time.sleep(check_interval)
        driver.refresh()
    else:
        print("something happened")


waiting_for_update(bulgarian_grade, 10)
waiting_for_update(math_grade, 10)

