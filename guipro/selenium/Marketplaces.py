from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os
from time import sleep
import pyfiglet

global SEARCH
SEARCH = str(input('Pesquisa: '))


class Centauro:
    @staticmethod
    def iniciar():
        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("CENTAURO", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 20%...')


        # Final Url
        url = "https://www.centauro.com.br/busca?q="+SEARCH

        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)

        # Init
        navegador.get(url)
        sleep(2)

        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")
        for i in range (1, 3):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)
        for i in range(1, 10):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []


        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_ = "_e4x16a")

        url_centauro = "https://www.centauro.com.br"

        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_nome = produto.find('a', {'class': '_xe1nr1'}).getText()
            produto_preco = produto.find('span', {'class': '_9pmwio'}).getText()
            produto_link = url_centauro + produto.find('a', href=True).get('href')

            # Adicionando cada produto na lista criada
            dados_produtos.append([produto_nome, produto_preco, produto_link])


        # Convertendo os dados da lista para um Data Frame
        dados = pd.DataFrame(dados_produtos, columns=['nome', 'preco', 'link'])

        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/centauro.xlsx', index=False, encoding='utf-8')

        # Quit navegado
        navegador.quit()

class Dafiti:
    @staticmethod
    def iniciar():

        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("DAFITI", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 40%...')


        # Final url
        url = "https://www.dafiti.com.br/catalog/?q="+SEARCH+"&wtqs=1"


        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)


        # Init
        navegador.get(url)
        sleep(2)


        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")

        for i in range (1, 20):
            body.send_keys(Keys.PAGE_DOWN)
        sleep(4)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []

        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_ = "product-box")


        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_nome = produto.find('p', {'class': 'product-box-title'}).getText()
            produto_preco_de = produto.find('span', {'class': 'product-box-price-from'}).getText()
            produto_preco_promocional = produto.find('span', {'class': 'product-box-price-to'})
            produto_link = produto.find('a', href=True).get('href')

            # Validando se o preço promocional existe para armazenar
            if (produto_preco_promocional != None):
                new_preco_promocional = produto_preco_promocional.getText()
                dados_produtos.append([produto_nome, produto_preco_de, new_preco_promocional, produto_link])
            else:
                dados_produtos.append([produto_nome, produto_preco_de, '',produto_link])


        # Convertendo os dados da lista para um Data Frame
        dados = pd.DataFrame(dados_produtos, columns=['nome', 'preco-normal','preco-promocional', 'link'])

        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/dafiti.xlsx', index=False, encoding='utf-8')

        # Quit navegador
        navegador.quit()

class Netshoes:
    @staticmethod
    def iniciar():
        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("NETSHOES", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 60%...')

        # User
        url = "https://www.netshoes.com.br/busca?nsCat=Natural&q="+SEARCH

        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)

        # Init
        navegador.get(url)
        sleep(2)

        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")

        for i in range (1, 20):
            body.send_keys(Keys.PAGE_DOWN)
        sleep(4)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []

        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_ = "item-desktop--3")

        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_nome = produto.find('div', {'class': 'item-card__description__product-name'}).getText()
            produto_link_pre = produto.findPrevious('a', href=True).get('href')
            produto_link = produto_link_pre[2:]
            try:
                produto_preco = produto.find('span', {'data-price': 'price'}).getText()
                dados_produtos.append([produto_nome, produto_preco, produto_link])
            except AttributeError:
                dados_produtos.append([produto_nome, 'none',produto_link])
                print('Dev Error: Linha 205')



            dados_produtos.append([produto_nome, produto_preco, produto_link])


        # Convertendo os dados da lista para um Data Frame
        dados = pd.DataFrame(dados_produtos, columns=['nome', 'produto_preco', 'link'])

        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/netshoes.xlsx', index=False, encoding='utf-8')

        # Quit navegado
        navegador.quit()

class MercadoLivre:
    @staticmethod
    def iniciar():
        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("MERCADO LIVRE", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 80%...')

        # Final User
        url = "https://lista.mercadolivre.com.br/" + SEARCH

        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)

        # Init
        navegador.get(url)
        sleep(2)

        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")


        for i in range(1, 20):
            body.send_keys(Keys.PAGE_DOWN)
        sleep(4)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []

        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_="ui-search-layout__item")

        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_nome = produto.find('h2', {'class': 'ui-search-item__title'}).getText()
            produto_link = produto.find('a', href=True).get('href')

            # SE TIVER 3 PREÇOS (PREÇO NORMAL, PREÇO PROMOCIONAL, PREÇO PARCELADO)
            try:
                produto_preco = produto.findAll('span', attrs={'class': 'price-tag-amount'})[0].getText()
                produto_preco2 = produto.findAll('span', attrs={'class': 'price-tag-amount'})[1].getText()
                produto_preco3 = produto.findAll('span', attrs={'class': 'price-tag-amount'})[2].getText()
                dados_produtos.append([produto_nome, produto_preco2, produto_link])
            except IndexError:
                produto_preco = produto.findAll('span', attrs={'class': 'price-tag-amount'})[0].getText()
                produto_preco2 = produto.findAll('span', attrs={'class': 'price-tag-amount'})[1].getText()
                dados_produtos.append([produto_nome, produto_preco, produto_link])

        # Convertendo os dados da lista para um Data Frame
        dados = pd.DataFrame(dados_produtos, columns=['nome', 'produto_preco', 'link'])


        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/mercadolivre.xlsx', index=False, encoding='utf-8')


        # Quit navegado
        navegador.quit()

class Shopee:
    @staticmethod
    def iniciar():
        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("SHOPEE", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 98%...')

        # Final User
        url = "https://shopee.com.br/search?keyword=" + SEARCH

        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)

        # Init
        navegador.get(url)
        sleep(2)

        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")
        for i in range(1, 3):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)
        for i in range(1, 10):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []

        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_="shopee-search-item-result__item")

        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_link = produto.findNext('a', href=True).get('href').getText()
            print(produto_link)

            produto_preco = produto.find('span', attrs={'class': '_3c5u7X'}).getText()
            print(produto_preco)

            produto_nome = produto.find('div', {'class': '_3IqNCf'}).getText()
            print(produto_nome)
            dados_produtos.append([produto_nome, produto_preco, produto_link])


        '''
        # Convertendo os dados da lista para um Data Frame
        dados = pd.DataFrame(dados_produtos, columns=['nome', 'produto_preco', 'link'])

        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/shopee.xlsx', index=False, encoding='utf-8')
        '''
        # Quit navegado
        navegador.quit()

class Americanas:
    @staticmethod
    def iniciar():
        # Limpando tela
        clear = lambda: os.system('cls')
        clear()
        print('-----------------------------------------------------')
        out = pyfiglet.figlet_format("AMERICANAS", font="slant")
        print(out)
        print('-----------------------------------------------------')
        print('LOADING 85%...')

        # Final User
        url = "https://www.americanas.com.br/busca/" + SEARCH

        # Settings
        option = Options()
        option.headless = True
        navegador = webdriver.Firefox(options=option)

        # Init
        navegador.get(url)
        sleep(2)

        # Descendo a pagina para carregar todos os produtos
        body = navegador.find_element(By.CSS_SELECTOR, "body")
        for i in range (1, 3):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)
        for i in range(1, 10):
            body.send_keys(Keys.PAGE_DOWN)
            sleep(2)

        # Save page
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        # Criando a lista de produtos para ser armazenadas
        dados_produtos = []

        # Pegando div inteira do produto (img, nome, link, description...)
        produtos_quadrantes = site.findAll(class_="cJnBan")

        # Pegando info de cada um
        for produto in produtos_quadrantes:
            produto_nome = produto.find('h3', {'class': 'gUjFDF'}).getText()
            produto_link = "https://www.americanas.com.br" + produto.find('a', href=True).get('href')
            try:
                produto_preco = produto.find('span', {'class': 'liXDNM'}).getText()
                dados_produtos.append([produto_nome, produto_preco, produto_link])
            except:
                print('Dev Error: Erro ao achar o preço')
                dados_produtos.append([produto_nome, 'none', produto_link])


        dados = pd.DataFrame(dados_produtos, columns=['nome', 'none', 'link'])

        # Salvando o arquivo em xlsx
        dados.to_excel('C:/Users/FAT-01/Downloads/americanas.xlsx', index=False, encoding='utf-8')


        # Quit navegado
        navegador.quit()

class Amazon:
        @staticmethod
        def iniciar():
            # Limpando tela
            clear = lambda: os.system('cls')
            clear()
            print('-----------------------------------------------------')
            out = pyfiglet.figlet_format("AMAZON", font="slant")
            print(out)
            print('-----------------------------------------------------')
            print('LOADING 91%...')

            # Final User
            url = "https://www.amazon.com.br/s?k=" + SEARCH

            # Settings
            option = Options()
            option.headless = True
            navegador = webdriver.Firefox(options=option)

            # Init
            navegador.get(url)
            sleep(2)

            # Descendo a pagina para carregar todos os produtos
            body = navegador.find_element(By.CSS_SELECTOR, "body")
            for i in range(1, 3):
                body.send_keys(Keys.PAGE_DOWN)
                sleep(2)
            for i in range(1, 10):
                body.send_keys(Keys.PAGE_DOWN)
                sleep(2)

            # Save page
            page_content = navegador.page_source
            site = BeautifulSoup(page_content, 'html.parser')

            # Criando a lista de produtos para ser armazenadas
            dados_produtos = []

            # Pegando div inteira do produto (img, nome, link, description...)
            produtos_quadrantes = site.findAll('div', {'data-component-type': 's-search-result'})

            # Pegando info de cada um
            for produto in produtos_quadrantes:
                produto_nome = produto.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).getText()
                produto_preco = produto.find('span', {'class': 'a-offscreen'}).getText()
                produto_link = "https://www.amazon.com.br" + produto.find('a', href=True).get('href')

                print(produto_nome)
                print(produto_preco)
                print(produto_link)




                dados_produtos.append([produto_nome, produto_preco, produto_link])

            dados = pd.DataFrame(dados_produtos, columns=['nome', 'none', 'link'])

            # Salvando o arquivo em xlsx
            #dados.to_excel('C:/Users/FAT-01/Downloads/amazon.xlsx', index=False, encoding='utf-8')

            # Quit navegado
            navegador.quit()