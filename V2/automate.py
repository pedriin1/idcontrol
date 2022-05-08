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


def workflow(driver, start, qnt_docs):

    num_start = int(start)
    qnt_docs = int(qnt_docs)

    for i in range(num_start, qnt_docs + num_start ):
        driver.get(f"{LINK}/list_visitor")
        time.sleep(1)
        search_input = driver.find_element_by_xpath("//div[@id='datatablevisitor_filter']//label//input")
        
        number = str(i)
        search_input.send_keys(number)

        time.sleep(1)

        table_rows = driver.find_elements_by_xpath("//tbody//tr")

        for i in range(len(table_rows)):
            if i > 0:
                if driver.find_element_by_xpath(f"//tbody//tr[{i}]//td[2]").text == number:
                    driver.find_element_by_xpath(f"//tbody//tr[{i}]//td[7]").click()
                    print("Número encontrado")
                    time.sleep(2)
                    # Indo até a pagina de QR Code e gerando
                    
                    qr_code = driver.find_element_by_xpath("//li[@id='additional']//a")
                    driver.execute_script("arguments[0].click();", qr_code)

                    generate_qr_code = driver.find_element_by_id("btn_create_qrcode")
                    driver.execute_script("arguments[0].click();", generate_qr_code)


                    print_qrcode = driver.find_element_by_id("btn_printqrcode")
                    driver.execute_script("arguments[0].click();", print_qrcode)

                    time.sleep(2)

                    driver.find_element_by_css_selector("bootbox-close-button close").click()
                    
                    break
                        




def initialize(qnt_docs, start, type):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(f"{LINK}/login")
    typewrite("thisisunsafe")

    logIn(driver)
    time.sleep(1)

    
    workflow(driver, start, qnt_docs)


if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(f"{LINK}/login")
    typewrite("thisisunsafe")

    logIn(driver)
    time.sleep(1)
    workflow(driver, 1000, 50)
    
