from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome()
driver.get("https://localhost:30443/#/login")



def logIn():
    if "login" in driver.current_url:
        while True:
            try:
                user = driver.find_element_by_id("usr")
                pas = driver.find_element_by_id("pwd")

                user.send_keys("admin")
                pas.send_keys("1")


                driver.find_element_by_id("entrar").click()
                time.sleep(1)


                driver.get("https://localhost:30443/#/list_visitor")

                break
            except:
                pass


def addUser(qnt_user):
    select = Select(driver.find_element_by_name('datatablevisitor_length'))
    select.select_by_value('10000')
    driver.find_element_by_xpath("//thead/tr/th[2]").click()
    time.sleep(1)
    get_lastuser = driver.find_element_by_xpath("//tbody[1]/tr[1]/td[2]") 

    #Criando novo usuario

    btn_new = driver.find_element_by_id("btn_add_visitor").click()
    time.sleep(2)
    input_name = driver.find_element_by_id("name")
    input_name.send_keys(str(get_lastuser.text))




    print(get_lastuser.text)



def main():
    logIn()
    time.sleep(1)
    addUser(10)



main()


