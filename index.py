from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

codigos = ['22316', '21897', '22469', '22192', '22567', '22153', '21778', '22281', '22941', '22882', '21603', '22740', '21587', '23009', '22500', '22424', 
           '23167', '22423', '22816', '23103', '22592', '23317', '23067', '22804']
url = 'http://redmine.rs.dbseller.com.br/issues/'
file = open('redmines.txt', 'w')

titulos = []
descricoes = []
descr = []
for codigo in codigos:
    browser.get(url+codigo)
    file.write(browser.title)
    file.write("\n\n")
    descricao = browser.find_elements(By.CLASS_NAME, "wiki")
    resultado = descricao[1].find_elements(By.TAG_NAME, "p")
    for x in resultado:
        linha = x.get_attribute('innerHTML')
        linha = linha.replace('<br>','')
        file.write(linha+"\n")
    file.write("\n\n")
    file.write("\n\n")

browser.quit()