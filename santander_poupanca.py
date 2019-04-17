# -*- coding: utf-8 -*-
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
print('[ {"inicio": "%s"},' % str(datetime.now()))
# necessario para funcionar remotamente
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
opts = FirefoxOptions()
# opts.add_argument("--headless")
firefox = webdriver.Firefox(firefox_options=opts)
wait = WebDriverWait(firefox, 10)
# ============================================

# parametros
cpf = sys.argv[1]
user_pass = sys.argv[2]
try: 
    dir_file = sys.argv[3]
except:
    pass
default_file_name = 'erro.png'
# =====================================

# PAGINA DE LOGIN
firefox.get('https://www.santander.com.br/')
try:
    # preenchendo o CPF
    # login = firefox.find_element_by_name('txtCPF')
    login = firefox.find_element_by_xpath("//input[contains(@class, 'login')]")
    login.send_keys("", cpf)
    login.send_keys(Keys.ENTER)
    sleep(5)
    # ====================================

    # preenchendo senha    
    senha = firefox.find_element_by_xpath('//*[@id="senha"]')    
    senha.send_keys("", user_pass)
    senha.send_keys(Keys.ENTER)
    sleep(5)
    #  ======================================

    # CLICANDO NO MENU    
    menu = firefox.find_element_by_xpath('//*[@id="investimentos"]')   
    menu.click()        
    menu_extrato = firefox.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/ul/li[3]/a')   
    menu_extrato.click()
    sleep(5)

    # GERANDO EXTRATO
    
    table_extrato = firefox.find_elements_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/article/div[2]/div/div/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/table/tbody/tr")
    # extraindo extrato 
    print('{"extrato" : [')
    print_extrato = ""
    for row in table_extrato:    
        if row.find_element_by_xpath('./td[1]').text:        
            data = datetime.strptime(row.find_element_by_xpath('./td[1]').text, '%d/%m/%Y')
            documento = row.find_element_by_xpath("./td[2]").text
            historico = row.find_element_by_xpath("./td[3]").text
            valor_movimento = (row.find_element_by_xpath("./td[4]").text).replace('.', '').replace(',','.')
            saldo = (row.find_element_by_xpath("./td[5]").text).replace('.', '').replace(',','.')
            # print("==> %s, %s, %s, %s, %s, " % (data, documento, historico, valor_movimento, saldo))
            print_extrato = print_extrato + ('{ "data": "%s", "documento": "%s",  "historico": "%s", "valor_movimento": "%s", "saldo": "%s"},' % (data, documento, historico, valor_movimento, saldo))
            # print("==> %s, %s, %s, %s, %s, " % (data, documento, historico, valor_movimento, saldo))
    print(print_extrato[0:-1])
    print(']},')
    #  ===============================================

    # Extraindo Aniversarios
    table_aniversario = firefox.find_elements_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/article/div[2]/div/div/div/form/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr")
    print('{"aniversario": [')
    print_aniversario = ""
    for row2 in table_aniversario:
        data1 = (row2.find_element_by_xpath("./td[1]").text).replace('*', '').replace(' ','')
        valor1 = (row2.find_element_by_xpath("./td[2]").text).replace('.', '').replace(',','.')
        data2 = (row2.find_element_by_xpath("./td[3]").text).replace('*', '').replace(' ','')
        valor2 = (row2.find_element_by_xpath("./td[4]").text).replace('.', '').replace(',','.')    
        print_aniversario = print_aniversario +  ('{ "data": "%s", "valor": "%s"}, { "data": "%s", "valor": "%s"},' % (data1, valor1, data2, valor2))
    print(print_aniversario[0:-1])
    print(']},')
    #  LogOff do santander 
    firefox.switch_to.default_content()
    firefox.get('https://www.santandernet.com.br/IBPF_Logout.asp')
    firefox.get('https://www.santandernet.com.br/logout.asp')
    # ===================================


    # Fechar navegador
    # firefox.quit()
    print('{"fim": "%s"} ]' % str(datetime.now()))
except Exception:  
    # if dir_file is not None:
    #     firefox.save_screenshot(dir_file + "/" + default_file_name)
    #     pass
    # firefox.quit()
    raise