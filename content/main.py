from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pyautogui import typewrite
from webdriver_manager.chrome import ChromeDriverManager
import time

import json

import os

current_dir = os.getcwd()



f = open(f'{current_dir}/content/config.json')
config = json.load(f)
f.close()



while True:
    try:
        qnt_docs = int(input("Digite a quantidade de docs: "))
        break
    except:
        pass

LINK = config["ip_address"]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(f"{LINK}/login")
typewrite("thisisunsafe")



LIST_ADDED_USER = []


def logIn():
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





def addUser(last_user):

    global LIST_ADDED_USER
    #Entrando na pagina para criar o user

    driver.get(f"{LINK}/list_visitor")
    time.sleep(1)
    
    #Criando novo usuario

    btn_new = driver.find_element_by_id("btn_add_visitor").click()
    time.sleep(2)


    #Digitando o nome da usuario
    name_input = driver.find_element_by_xpath("//div[@class='row form-group']//input[@id='name']")
    name_input.send_keys(last_user)

    #Digitando a data de expiração
    driver.find_element_by_id("visitor_datelimit").clear()
    date_picker = driver.find_element_by_id("visitor_datelimit")
    date_picker.send_keys("18/01/2026")
    time.sleep(1)

    #Informaçoes adicionais (adicionar credito)


    additional_info = driver.find_element_by_xpath("//li[@id='additional'][2]//a")
    driver.execute_script("arguments[0].click();", additional_info)



    add_info_btn = driver.find_element_by_xpath("//div[@class='portlet-title']//div[@class='actions']//a")
    driver.execute_script("arguments[0].click();", add_info_btn)


    select = Select(driver.find_element_by_xpath("//div[@class='modal-content']//select"))

    select.select_by_value("number:1")
    time.sleep(2)

    driver.find_element_by_xpath("//div[@class='modal-content']//button[@id='btn_save']")
    time.sleep(2)



    # Indo até a pagina de QR Code e gerando
    # qr_code = driver.find_element_by_xpath("//li[@id='additional']//a")
    # driver.execute_script("arguments[0].click();", qr_code)

    # generate_qr_code = driver.find_element_by_id("btn_create_qrcode")
    # driver.execute_script("arguments[0].click();", generate_qr_code)


    # print_qrcode = driver.find_element_by_id("btn_printqrcode")
    # driver.execute_script("arguments[0].click();", print_qrcode)




    time.sleep(2)

    #Salvando o usuario
    # save = driver.find_element_by_id("btn_save")
    # driver.execute_script("arguments[0].click();", save)

    LIST_ADDED_USER.append(last_user)

    time.sleep(1)




def addUserContainer(times, start):
   
    for i in range(times):
        try:
            addUser(str(start + i))
        except:
            time.sleep(5)
            addUser(str(start + i))
        time.sleep(1)



def main():
    logIn()
    t1 = time.time()
    addUserContainer(qnt_docs, 1000)
    t2 = time.time()
    print(t2-t1)





main()


