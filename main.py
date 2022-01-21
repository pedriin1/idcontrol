from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pyautogui import typewrite
from webdriver_manager.chrome import ChromeDriverManager
import time



LINK = "https://localhost:30443/#"

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


                user.send_keys("admin")
                pas.send_keys("1")


                driver.find_element_by_id("entrar").click()
                time.sleep(1)



                break
            except:
                pass


def addGroup():
    driver.refresh()
    driver.get(f"{LINK}/list_groups_visitors")

    time.sleep(2)


    driver.get(f"{LINK}/edit_group_visitors/1001")
    time.sleep(1)

    visitors_btn = driver.find_element_by_xpath("//li//a[@name='departiments_tab_users']")
    driver.execute_script("arguments[0].click();", visitors_btn)

    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='portlet-title']//div[@class='actions']//a").click()
    time.sleep(1)

    try:
        driver.find_element_by_xpath("//thead/tr/th[6]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[@id='select_all']//a").click()
    except:
        pass
        
   
    add_btn = driver.find_element_by_xpath("//div[@class='modal-content']//div[@class='margiv-top-10']//button[@class='btn green ng-binding']")
    driver.execute_script("arguments[0].click();", add_btn)

    save_btn = driver.find_element_by_xpath("//div[@class='margiv-top-10']//button[@class='btn green ng-binding']")
    driver.execute_script("arguments[0].click();", save_btn)



def getLastUser():
    driver.get(f"{LINK}/list_visitor")
    time.sleep(1)

    try:
        get_firstuser = driver.find_element_by_xpath("//tbody[1]/tr[1]/td[2]")
        get_firstuser = get_firstuser.text
    except:
        get_firstuser = 0
   
    select = Select(driver.find_element_by_name('datatablevisitor_length'))
    select.select_by_value('10000')

    
    driver.find_element_by_xpath("//thead/tr/th[2]").click()
    time.sleep(1)
    get_lastuser = driver.find_element_by_xpath("//tbody[1]/tr[1]/td[2]")

    try:

        last_user_number = int(get_lastuser.text) + 1
    except:
        last_user_number = 1000

    return last_user_number, int(get_firstuser or 0) 



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

    #Indo até a pagina de QR Code e gerando
    qr_code = driver.find_element_by_xpath("//li[@id='additional']//a")
    driver.execute_script("arguments[0].click();", qr_code)

    generate_qr_code = driver.find_element_by_id("btn_create_qrcode")
    driver.execute_script("arguments[0].click();", generate_qr_code)


    print_qrcode = driver.find_element_by_id("btn_printqrcode")
    driver.execute_script("arguments[0].click();", print_qrcode)




    time.sleep(2)

    #Salvando o usuario
    save = driver.find_element_by_id("btn_save")
    driver.execute_script("arguments[0].click();", save)

    LIST_ADDED_USER.append(last_user)

    time.sleep(1)




def addUserContainer(times):
    last_user, first_user = getLastUser()
    times_arr = []
 
    if first_user != 1000:
        for i in range(times):
            if i+1000 < first_user:
                times_arr.append(1000 + i)
            else:
                times_arr.append(i+last_user)

    else:
        for i in range(times):
            times_arr.append(i+last_user)

    print(last_user)
    print(first_user)
    for i in times_arr:
        try:
            addUser(str(i))
        except:
            time.sleep(5)
            addUser(str(i))
        time.sleep(1)



def main():
    logIn()
    t1 = time.time()
    addUserContainer(15)
    addGroup()
    t2 = time.time()

    print(t2-t1)





main()


