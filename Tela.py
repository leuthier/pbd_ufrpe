# -*- coding: utf-8 -*-
import persistencia.DataBase as dao
import matplotlib.pyplot as plt

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
        print("#################################################")
        print("##               VOU DE QUE                    ##")
        print("#################################################")
        esc = input ("\n1 - Pesquisar\n2 - Buscar por local\n3 - Buscar por data\n4 - Buscar por data e local\n5 - Buscar por sentimento\n6 - Sair\n>>> " ) 
        if esc == "6":
            print ("Saiba mais do nosso projeto em:\n\nhttps://github.com/leuthier/pbd_ufrpe\n")
            esc2 = input("Deseja acessar o repositorio? (S/N) ")
            esc2 = esc2.lower()
            if esc2 == "s":
                webbrowser.open_new("https://github.com/leuthier/pbd_ufrpe")
            elif esc2 == "n":
                print("Obrigado")
        elif esc == "2":
            if buscar_locais() != None:
                nums = []
                for i in range(len(cidades)):
                    print(i,"-", cidades[i])
                    nums.append(str(i))
                esc_local = input("Escolha o numero da cidade a ser analisada: ")
                if str(esc_local) in nums:
                    cidade_query = cidades[int(esc_local)]
                    esc_local = input("Qual marca vc deseja analisar em "+cidade_query+" ?\n1 - Uber\n2 - Cabify\n3 - 99pop\n4 - Comparar sentimento bom")
                    resultado = buscar_tweets_local(cidade_query)
                    if esc_local == "1":
                        pos_uber = resultado[0][0]
                        neg_uber = resultado[0][1]
                        neu_uber = resultado[0][2]
                        total_uber = pos_uber + neg_uber + neu_uber
                        if (total_uber != 0):
                            sizes = [pos_uber/total_bom, pos_cabify/total_bom, pos_pop/total_bom]
                            fig1, ax1 = plt.subplots()
                            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
                            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                            plt.show()
                        else:
                            print("** Erro ** Dados insuficientes")
                    
                    elif esc_local == "2":
                        resultado[1]
                    elif esc_local == "3":
                        resultado[2]
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
            # lista2 = buscar_tweets_data(data)
            # data = "2017-07-18"
            print()
            
    return
    

menu()
lis = buscar_tweets()
print(lis)

print("pos_uber:", pos_uber)



# while(True):
#
#
#     inpt = input("\nOpÃ§Ãµes:\n 1 - Escolher por cidade\n 2 - Escolher por data\n 3 - Escolher por ambos\n 4 - Sair\n >>>>> ")
#     if(inpt == 4):

