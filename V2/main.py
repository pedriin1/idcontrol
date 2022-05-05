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


def workflow(driver):
    driver.get(f"{LINK}/list_visitor")
    time.sleep(1)
    search_input = driver.find_element_by_xpath("//div[@id='datatablevisitor_filter']//label//input")
    search_input.send_keys("1000")

    time.sleep(1)

    table_rows = driver.find_elements_by_tag_name("tr")
    print(table_rows)
    for i in table_rows:
        print(i)



if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(f"{LINK}/login")
    typewrite("thisisunsafe")

    logIn(driver)
    time.sleep(1)
    workflow(driver)
    
