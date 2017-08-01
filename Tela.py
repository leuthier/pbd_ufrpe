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
    resposta = dao.Busca_SQL("select DISTINCT nome_lugar from voudeque.lugar;")
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

def quantidadeTweets(resultado):
    pos_uber = resultado[0][0]
    neg_uber = resultado[0][1]
    neu_uber = resultado[0][2]
    total_uber = pos_uber+neu_uber+neu_uber

    pos_cabify = resultado[1][0]
    neg_cabify = resultado[1][1]
    neu_cabify = resultado[1][2]
    total_cabify = pos_cabify+neg_cabify+neu_cabify

    pos_99pop = resultado[2][0]
    neg_99pop = resultado[2][1]
    neu_99pop = resultado[2][2]
    total_99pop = pos_99pop+neg_99pop+neu_99pop

    total = total_uber+total_99pop+total_cabify

    return pos_uber, neg_uber, neu_uber, total_uber, pos_cabify, neg_cabify, neu_cabify, total_cabify, pos_99pop, neg_99pop, neu_99pop, total_99pop, total

def buscar_tweets_local(local):
    resultado = [[], [], []]

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])

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

    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])
    resultado[0].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'uber';")[0][0])

    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])
    resultado[1].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = 'cabify';")[0][0])

    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Positivo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%'  and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Negativo' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])
    resultado[2].append(dao.Busca_SQL("select count(*) from voudeque.tweet, voudeque.sentimento, voudeque.marca, voudeque.tweet_marca, voudeque.lugar where tweet.id_sentimento = sentimento.id and sentimento.classe = 'Neutro' and tweet.id_lugar = lugar.id and tweet_marca.id_marca = marca.id and tweet_marca.id_tweet = tweet.id and tweet.dataHora like '" + data + "%' and lugar.nome_lugar = '" + local + "' and marca.nome = '99pop';")[0][0])

    return resultado



cidades = buscar_locais()

def menu():
    while True:
        print("\n#################################################")
        print("##               VOU DE QUÊ?                    ##")
        print("#################################################")
        esc = input ("\n1 - Pesquisar\n2 - Buscar por local\n3 - Buscar por data\n4 - Buscar por data e local\n5 - Sair\n>>> " )
        if esc == "5":  #sair
            print ("Saiba mais sobre nosso projeto em:\n\nhttps://github.com/leuthier/pbd_ufrpe\n")
            esc2 = input("Deseja acessar o repositório? (S/N) ")
            esc2 = esc2.lower()
            if esc2 == "s":
                webbrowser.open_new("https://github.com/leuthier/pbd_ufrpe")
            print("Agradecemos a visita.")
            break
        elif esc == "2":  #buscar por local
            if buscar_locais() != None:
                nums = []
                for i in range(len(cidades)):
                    print(i,"-", cidades[i])
                    nums.append(str(i))
                esc_local = input("Escolha o número da cidade a ser analisada: ")
                if str(esc_local) in nums:
                    cidade_query = cidades[int(esc_local)]
                    resultado = buscar_tweets_local(cidade_query)

                    graficoBarra(quantidadeTweets(resultado))

                        #####
                    pos_uber, neg_uber, neu_uber, total_uber, pos_cabify, neg_cabify, neu_cabify, total_cabify, pos_99pop, neg_99pop, neu_99pop, total_99pop, total = quantidadeTweets(resultado)
                    pos_list = [pos_uber,pos_cabify,pos_99pop]
                    neg_list = [neg_uber,neg_cabify,neg_99pop]
                    neu_list = [neu_uber,neu_cabify,neu_99pop]

                    labels_list1,labels_list2,labels_list3=['','',''],['','',''],['','','']

                    if pos_list[0]!=0:
                        labels_list1[0]='Uber'
                    if pos_list[1] !=0:
                        labels_list1[1]='Cabify'
                    if pos_list[2] !=0:
                        labels_list1[2]='99Pop'

                    if neg_list[0]!=0:
                        labels_list2[0]='Uber'
                    if neg_list[1] !=0:
                        labels_list2[1]='Cabify'
                    if neg_list[2] !=0:
                        labels_list2[2]='99Pop'

                    if neu_list[0]!=0:
                        labels_list3[0]='Uber'
                    if neu_list[1] !=0:
                        labels_list3[1]='Cabify'
                    if neu_list[2] !=0:
                        labels_list3[2]='99Pop'

                    fig, eixos = plt.subplots(nrows=1, ncols=3, figsize=(7, 4))

                    pie_1 = eixos[0].pie(pos_list, labels=labels_list1,
                                         autopct='%1.1f%%', colors=['gray', 'lightskyblue', 'gold'])
                    eixos[0].set_title('Positivo')
                    eixos[0].axis('equal')

                    pie_2 = eixos[1].pie(neg_list, labels=labels_list2,
                                         autopct='%1.1f%%', startangle=50, colors=['gray', 'lightskyblue', 'gold'])
                    eixos[1].set_title('Negativo')
                    plt.axis('equal')

                    pie_3 = eixos[2].pie(neu_list, labels=labels_list3,
                                         autopct='%1.1f%%', startangle=90, colors=['gray', 'lightskyblue', 'gold'])
                    eixos[2].set_title('Neutro')
                    plt.axis('equal')

                    plt.subplots_adjust(wspace=1)

                    plt.suptitle(cidade_query.upper())
                    plt.show()

                else:
                    print("\n** Erro **\n Número de cidade inválido\n")

            else:
                print("Devido ao número restrito de tweets com locais, nenhuma cidade está disponível para análise :( ")


        elif esc == "3":  # buscar por data
            print("A data deve seguir o padrão: ANO-MES-DIA")
            esc_data = input("\n>>>>")

            resultado = buscar_tweets_data(esc_data)

            verificacao_data = esc_data.split("-")
            if len(verificacao_data[0]) == 4 and len(verificacao_data[1]) == 2 and len(verificacao_data[2]) == 2:
                try:
                    int(verificacao_data[0]), int(verificacao_data[1]), int(verificacao_data[2])
                    pos_uber, neg_uber, neu_uber, total_uber, pos_cabify, neg_cabify, neu_cabify, total_cabify, pos_99pop, neg_99pop, neu_99pop, total_99pop, total = quantidadeTweets(resultado)

                    if total!=0:

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

                    else:
                        print("\n** Erro ** Não há dados para essa data\n")
                except:
                    print("\n** Erro **\n Data inválida\n")

            else:
                print("\n** Erro **\n Data inválida\n")

        elif esc == "1": #análise geral
            resultado = buscar_tweets()

            pos_uber, neg_uber, neu_uber, total_uber, pos_cabify, neg_cabify, neu_cabify, total_cabify, pos_99pop, neg_99pop, neu_99pop, total_99pop, total = quantidadeTweets(resultado)

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

        elif esc == "4": # buscar por data e local
             print("A data deve seguir o padrao: ANO-MES-DIA")
             esc_data = input("\n>>>>")

             if buscar_locais() != None:
                 nums = []
                 for i in range(len(cidades)):
                     print(i, "-", cidades[i])
                     nums.append(str(i))

                 esc_local = input("Escolha o número da cidade a ser analisada: ")
                 if str(esc_local) in nums:
                     cidade_query = cidades[int(esc_local)]

                 resultado = buscar_tweets_data_lugar(esc_data,cidade_query)

                 pos_uber, neg_uber, neu_uber, total_uber, pos_cabify, neg_cabify, neu_cabify, total_cabify, pos_99pop, neg_99pop, neu_99pop, total_99pop, total = quantidadeTweets(resultado)

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

        else:
            print("\n** Erro ** \n Opção inválida\n")
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


def graficoBarra(pos_uber,neg_uber,neu_uber,total_uber,pos_cabify,neg_cabify,neu_cabify,total_cabify,pos_99pop,neg_99pop,neu_99pop,total_99pop,total):
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
    plt.grid()
    plt.show()

