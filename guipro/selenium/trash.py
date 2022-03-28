'''
            try:
                produto_preco_por = produto.findAll('span', attrs={'class': 'price-tag-fraction'})[1].getText()
            except IndexError:
                print('')
            try:
                produto_fracao_por = produto.findAll('span', attrs={'class': 'price-tag-cents'})[1].getText()
            except IndexError:
                print('')


            if (str(produto_fracao_de) != 'None' and str(produto_fracao_por) != 'None'):
                dados_produtos.append([produto_nome, produto_preco_de + ',' + produto_fracao_de, produto_preco_por + ',' + produto_fracao_por, produto_link])

            elif(str(produto_fracao_de) == 'None' and str(produto_fracao_por) == 'None'):
                dados_produtos.append([produto_nome, produto_preco_de + ',' + '00', produto_preco_por + ',' + '00', produto_link])

            elif(str(produto_fracao_de) != 'None' and str(produto_fracao_por) == 'None'):
                dados_produtos.append([produto_nome, produto_preco_de + ',' + produto_fracao_de, produto_preco_por + ',' + '00', produto_link])

            elif(str(produto_fracao_de) == 'None' and str(produto_fracao_por) != 'None'):
                dados_produtos.append([produto_nome, produto_preco_de + ',' + '00', produto_preco_por + ',' + produto_fracao_por, produto_link])

            '''