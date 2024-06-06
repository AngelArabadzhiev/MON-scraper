import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://infopriem.mon.bg/login")


def enter_username_password(username, password):
    user = driver.find_element(By.ID, "sn")
    user.click()
    user.send_keys(str(username), Keys.TAB)
    time.sleep(1)
    pswd = driver.find_element(By.ID, "webcode")
    pswd.click()
    pswd.send_keys(str(password), Keys.ENTER)
    time.sleep(1)
    driver.get("https://infopriem.mon.bg/student/marks")


def get_td():
    table = driver.find_element(By.TAG_NAME, 'table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    table_elements = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            table_elements.append(cell.text)
    table_elements.remove("10.06.2024 11:00")
    table_elements.remove("12.06.2024 08:00")
    print()
    for i in range(len(table_elements)):
        if i == 2 :
            print()
        print(table_elements[i])


#name = input("Твоят входящ номер: ")
#access = input("Твоят код за достъп: ")
enter_username_password("1034455", "5595163ef5")


def task():
    driver.refresh()
    get_td()


schedule.every(30).seconds.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)


