from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pyautogui import typewrite
from webdriver_manager.chrome import ChromeDriverManager
import time



config = {
  "ip_address": "https://localhost:30443/#",
  "qnt_docs": 10,
  "group_visitor_id": 1001,
  "group_visitor_id_banho": 1003,
  "user": "Admin",
  "password": "ti@3232"
}



LINK = config["ip_address"]

LIST_ADDED_USER = []


def logIn(driver):
    if "login" in driver.current_url:
        while True:
            try:
                user = driver.find_element_by_id("usr")
                pas = driver.find_element_by_id("pwd")


                user.send_keys(config["user"])
                pas.send_keys(config["password"])


                driver.find_element_by_id("entrar").click()
                time.sleep(1)

                break
            except:
                pass


if __name__ == "__main__":
    logIn()