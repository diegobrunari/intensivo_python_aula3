from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions() #~~tentar entender~~
options.add_experimental_option('excludeSwitches', ['enable-logging']) #same~~


#Pesquisar cotações
#necessário baixar chrome web driver e alocar na pasta de uso no caso do vscode
#dolar
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

#euro
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

#ouro
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(',', '.')
print (cotacao_ouro)
#navegador.quit() não precisa devido ao exludeSwitches

#importar banco de dados
tabela = pd.read_excel('Produtos.xlsx')


#Atualizando dados
tabela.loc[tabela['Moeda']=='Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda']=='Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda']=='Ouro', 'Cotação'] = float(cotacao_ouro)

#Atualizando preço de compra
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela ['Cotação']

#Atualizando Preço de venda
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

print(tabela)

#Exportar tabela para o excel

tabela.to_excel('Produtos Novo.xlsx', index=False) #index=False -> para não exportar as linhas 0,1,2,3,4.. porque já tem no excel




