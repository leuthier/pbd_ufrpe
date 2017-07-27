# -*- coding: utf-8 -*-
import persistencia.DataBase as dao
import webbrowser
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator as o
import numpy as np

uber = [[], [], []]
cabify = [[], [], []]
pop99 = [[], [], []]

def buscar_locais():
    resposta = dao.Busca_SQL("select nome_lugar from voudeque.lugar;")
    cidades = []
    for i in resposta:
        cidades.append(i[0])
    return cidades

def buscar_tweets():
    ###
    # posicao 1 = positivo, 2 = negativo e 3 = neutro
    # uber = 1, cabify = 2 uber = 3
    ###

    resultado =[[], [], []]

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])
    
    return resultado

# def quantidade(resultado):
#     pos_uber = resultado[0][0]
#     neg_uber = resultado[0][1]
#     neu_uber = resultado[0][2]
#     
#     pos_cabify = resultado[1][0]
#     neg_cabify = resultado[1][1]
#     neu_cabify = resultado[1][2]
#     
#     pos_99pop = resultado[2][0]
#     neg_99pop = resultado[2][1]
#     neu_99pop = resultado[2][2]
#     return 

def buscar_tweets_local(local):
    resultado = [[], [], []]

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])

    return resultado

def buscar_tweets_data(data):

    resultado = [[], [], []]

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo'  and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo'  and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro'  and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.dataHora like '" + data + "%' and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and marca.nome = '99pop';")[0][0])


    return resultado

def buscar_tweets_data_lugar(data,local):

    resultado = [[], [], []]

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%'  and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.tweet_local, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet_local.id_tweet = tweet.id and tweet_local.id_local = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])


    return resultado



cidades = buscar_locais()
#print(cidades)
###cÃ³digo para testar
# local = "jaboatÃ£o dos guararapes"
# data = "2017-07-18"
#
# lista1 = buscar_tweets()
# lista2 = buscar_tweets_data(data)
# lista3 = buscar_tweets_local(local)
# lista4 = buscar_tweets_data_lugar(data,local)
#
# print("tweets genÃ©ricos" + str(lista1))
# print("tweets data" + str(lista2))
# print("tweeets local" + str(lista3))
# print("tweets local e data" + str(lista4))

def menu():
        
    while True:  
        print("\n#################################################")
        print("##               VOU DE QUE                    ##")
        print("#################################################")
        esc = input ("\n1 - Pesquisar\n2 - Buscar por local\n3 - Buscar por data\n4 - Buscar por data e local\n5 - Buscar por sentimento\n6 - Sair\n>>> " ) 
        if esc == "6":
            print ("Saiba mais do nosso projeto em:\n\nhttps://github.com/leuthier/pbd_ufrpe\n")
            esc2 = input("Deseja acessar o repositorio? (S/N) ")
            esc2 = esc2.lower()
            if esc2 == "s":
                webbrowser.open_new("https://github.com/leuthier/pbd_ufrpe")
            print("Agradecemos a visita.")
            break
        elif esc == "2":
            if buscar_locais() != None:
                nums = []
                for i in range(len(cidades)):
                    print(i,"-", cidades[i])
                    nums.append(str(i))
                esc_local = input("Escolha o numero da cidade a ser analisada: ")
                if str(esc_local) in nums:
                    cidade_query = cidades[int(esc_local)]
                    esc_local = input("Qual marca vc deseja analisar em "+cidade_query+" ?\n1 - Uber\n2 - Cabify\n3 - 99pop\n4 - Comparar sentimento bom\n>>>> ")
                    resultado = buscar_tweets_local(cidade_query)
                    if esc_local == "1":
                        pos_uber = resultado[0][0]
                        neg_uber = resultado[0][1]
                        neu_uber = resultado[0][2]
                        total_uber = pos_uber + neg_uber + neu_uber
                        if (total_uber != 0):
                            sizes = [pos_uber/total_uber, neg_uber/total_uber, neu_uber/total_uber]
                            fig1, ax1 = plt.subplots()
                            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
                            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                            plt.show()
                        else:
                            print("\n** Erro ** Dados insuficientes\n")
                    
                    elif esc_local == "2":
                         pos_cabify = resultado[1][0]
                         neg_cabify = resultado[1][1]
                         neu_cabify = resultado[1][2]
                         total_cabify = pos_cabify + neg_cabify + neu_cabify
                         if (total_cabify != 0):
                             sizes = [pos_cabify/total_cabify, neg_cabify/total_cabify, neu_cabify/total_cabify]
                             fig1, ax1 = plt.subplots()
                             ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
                             ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                             plt.show()
                         else:
                            print("\n** Erro ** Dados insuficientes\n")
                         
                    elif esc_local == "3":
                         pos_99pop = resultado[2][0]
                         neg_99pop = resultado[2][1]
                         neu_99pop = resultado[2][2]
                         total_99pop = pos_99pop + neg_99pop + neu_99pop
                         if (total_99pop != 0):
                             sizes = [pos_99pop/total_99pop, neg_99pop/total_99pop, neu_99pop/total_99pop]
                             fig1, ax1 = plt.subplots()
                             ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
                             ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                             plt.show()
                         else:
                            print("\n** Erro ** Dados insuficientes\n")
                            
                    elif esc_local == "4":
                        labels = 'Uber', 'Cabify', '99Pop'
                        pos_uber = resultado[0][0]
                        pos_cabify = resultado[1][0]
                        pos_pop =resultado[2][0]
                        total_bom = pos_uber + pos_cabify + pos_pop
                        if total_bom == 0:
                            print("\n** Erro **\n Dados insuficientes para geração de gráficos")
                        else:
                            sizes = [pos_uber/total_bom, pos_cabify/total_bom, pos_pop/total_bom]
                            # only "explode" the 2nd slice (i.e. 'Hogs')
                        
                            fig1, ax1 = plt.subplots()
                            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
                            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                            plt.show()
                    else:
                        print("\n** Erro **\n Opcao invalida\n")
                    
                else:
                    print("\n** Erro **\n Numero da cidade escolhida invalido\n")
                
            else:
                print("Devido ao numero restrito de tweets, nenhuma cidade esta disponivel para analise :( ")
        elif esc == "3":
            print("A data deve seguir o padrao: ANO-MES-DIA")
            esc_data = input("\n>>>>")
            resultado = buscar_tweets_data(esc_data)
            #data = "2017-07-18"

            pos_uber = resultado[0][0]
            neg_uber = resultado[0][1]
            neu_uber = resultado[0][2]

            total_uber = pos_uber+neg_uber+neu_uber

            pos_cabify = resultado[1][0]
            neg_cabify = resultado[1][1]
            neu_cabify = resultado[1][2]

            total_cabify = pos_cabify+neg_cabify+neu_cabify

            pos_99pop = resultado[2][0]
            neg_99pop = resultado[2][1]
            neu_99pop = resultado[2][2]

            total_99pop = pos_99pop+neg_99pop+neu_99pop

            total = total_uber+total_cabify+total_99pop

            if total==0:
                print("\n** Erro ** Não há dados para essa data\n")
                pass

            dpoints = np.array([['Positivo', 'Uber', pos_uber],
                                ['Positivo', 'Cabify', pos_cabify],
                                ['Positivo', '99pop', pos_99pop],
                                ['Neutro', 'Uber', neu_uber],
                                ['Neutro', 'Cabify', neu_cabify],
                                ['Neutro', '99pop', neu_99pop],
                                ['Negativo', 'Uber', neg_uber],
                                ['Negativo', 'Cabify', neg_cabify],
                                ['Negativo', '99pop', neg_99pop]])

            fig = plt.figure()
            ax = fig.add_subplot(111)

            barplot(ax, dpoints)
            plt.subplots_adjust(bottom=0.20)
            plt.show()


        elif esc == "1":
            resultado = buscar_tweets()
            pos_uber = resultado[0][0]
            neg_uber = resultado[0][1]
            neu_uber = resultado[0][2]
             
            pos_cabify = resultado[1][0]
            neg_cabify = resultado[1][1]
            neu_cabify = resultado[1][2]
             
            pos_99pop = resultado[2][0]
            neg_99pop = resultado[2][1]
            neu_99pop = resultado[2][2]
            
            dpoints = np.array([['Positivo', 'Uber',  pos_uber],
                       ['Positivo', 'Cabify', pos_cabify],
                       ['Positivo', '99pop', pos_99pop],
                       ['Neutro', 'Uber', neu_uber],
                       ['Neutro', 'Cabify', neu_cabify],
                       ['Neutro', '99pop', neu_99pop],
                       ['Negativo', 'Uber', neg_uber],
                       ['Negativo', 'Cabify', neg_cabify],
                       ['Negativo', '99pop', neg_99pop]])
            
            fig = plt.figure()
            ax = fig.add_subplot(111)
            

                    
            barplot(ax, dpoints)
            plt.subplots_adjust(bottom=0.20)
            plt.show()
            
        elif esc == "4":
             print("A data deve seguir o padrao: ANO-MES-DIA")
             esc_data = input("\n>>>>")

             if buscar_locais() != None:
                 nums = []
                 for i in range(len(cidades)):
                     print(i, "-", cidades[i])
                     nums.append(str(i))

                 esc_local = input("Escolha o numero da cidade a ser analisada: ")
                 if str(esc_local) in nums:
                     cidade_query = cidades[int(esc_local)]

                 resultado = buscar_tweets_data_lugar(esc_data,cidade_query)

                 pos_uber = resultado[0][0]
                 neg_uber = resultado[0][1]
                 neu_uber = resultado[0][2]

                 total_uber = pos_uber + neg_uber + neu_uber

                 pos_cabify = resultado[1][0]
                 neg_cabify = resultado[1][1]
                 neu_cabify = resultado[1][2]

                 total_cabify = pos_cabify + neg_cabify + neu_cabify

                 pos_99pop = resultado[2][0]
                 neg_99pop = resultado[2][1]
                 neu_99pop = resultado[2][2]

                 total_99pop = pos_99pop + neg_99pop + neu_99pop

                 total = total_uber + total_cabify + total_99pop

                 if total == 0:
                     print("\n** Erro ** Não há dados para essa data\n")
                     pass

                 dpoints = np.array([['Positivo', 'Uber', pos_uber],
                                     ['Positivo', 'Cabify', pos_cabify],
                                     ['Positivo', '99pop', pos_99pop],
                                     ['Neutro', 'Uber', neu_uber],
                                     ['Neutro', 'Cabify', neu_cabify],
                                     ['Neutro', '99pop', neu_99pop],
                                     ['Negativo', 'Uber', neg_uber],
                                     ['Negativo', 'Cabify', neg_cabify],
                                     ['Negativo', '99pop', neg_99pop]])

                 fig = plt.figure()
                 ax = fig.add_subplot(111)

                 barplot(ax, dpoints)
                 plt.subplots_adjust(bottom=0.20)
                 plt.show()

        elif esc == "5":
             print("Método em construção. Tente novamente mais tarde.")
             pass
             #print("A data devera seguir o padrao: ANO-MES-DIA")
             #esc_data = input("\n>>>>")
             #resultado = buscar_tweets_data_lugar(esc_data,local)
             #help
            
    return


def barplot(ax, dpoints):
    # Aggregate the conditions and the categories according to their
    # mean values
    conditions = [(c, np.mean(dpoints[dpoints[:, 0] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 0])]
    categories = [(c, np.mean(dpoints[dpoints[:, 1] == c][:, 2].astype(float)))
                  for c in np.unique(dpoints[:, 1])]

    # sort the conditions, categories and data so that the bars in
    # the plot will be ordered by category and condition
    conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
    categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]

    dpoints = np.array(sorted(dpoints, key=lambda x: categories.index(x[1])))

    # the space between each set of bars
    space = 0.2
    n = len(conditions)
    width = (1 - space) / (len(conditions))

    # Create a set of bars at each position
    for i, cond in enumerate(conditions):
        indeces = range(1, len(categories) + 1)
        vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
        pos = [j - (1 - space) / 2. + i * width for j in indeces]
        ax.bar(pos, vals, width=width, label=cond,
               color=cm.Accent(float(i) / n))

    # Set the x-axis tick labels to be equal to the categories
    ax.set_xticks(indeces)
    ax.set_xticklabels(categories)
    plt.setp(plt.xticks()[1], rotation=90)

    # Add the axis labels
    ax.set_ylabel("Tweets")
    ax.set_xlabel("Marcas")

    # Add a legend
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc='upper left')

menu()

