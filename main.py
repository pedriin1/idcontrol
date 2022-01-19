from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pyautogui import typewrite
from webdriver_manager.chrome import ChromeDriverManager


import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://10.211.55.3:30443/#/login")

typewrite("thisisunsafe")




def logIn():
    if "login" in driver.current_url:
        while True:
            try:
                user = driver.find_element_by_id("usr")
                pas = driver.find_element_by_id("pwd")

                user.send_keys("admin")
                pas.send_keys("admin")


                driver.find_element_by_id("entrar").click()
                time.sleep(1)



                break
            except:
                pass


def addUser():
    driver.get("https://10.211.55.3:30443/#/list_visitor")
    time.sleep(1)


    select = Select(driver.find_element_by_name('datatablevisitor_length'))
    select.select_by_value('10000')
    driver.find_element_by_xpath("//thead/tr/th[2]").click()
    time.sleep(1)
    get_lastuser = driver.find_element_by_xpath("//tbody[1]/tr[1]/td[2]")

    last_user_number = get_lastuser.text

    #Criando novo usuario

    btn_new = driver.find_element_by_id("btn_add_visitor").click()
    time.sleep(2)

    if last_user_number:


        typewrite(str(int(last_user_number) + 1))
    else:
        typewrite("1000")


    driver.find_element_by_id("visitor_datelimit").clear()
    date_picker = driver.find_element_by_id("visitor_datelimit")
    date_picker.send_keys("18/01/2026")
    time.sleep(1)
    qr_code = driver.find_element_by_xpath("//li[@id='additional']//a")

    driver.execute_script("arguments[0].click();", qr_code)

    generate_qr_code = driver.find_element_by_id("btn_create_qrcode")
    driver.execute_script("arguments[0].click();", generate_qr_code)

    save = driver.find_element_by_id("btn_save")
    driver.execute_script("arguments[0].click();", save)


def main():
    logIn()
    for i in range(10):
        addUser()
        time.sleep(1)



main()


