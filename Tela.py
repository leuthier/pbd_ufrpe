# -*- coding: utf-8 -*-
import persistencia.DataBase as dao

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

###código para testar
# local = "jaboatão dos guararapes"
# data = "2017-07-18"
#
# lista1 = buscar_tweets()
# lista2 = buscar_tweets_data(data)
# lista3 = buscar_tweets_local(local)
# lista4 = buscar_tweets_data_lugar(data,local)
#
# print("tweets genéricos" + str(lista1))
# print("tweets data" + str(lista2))
# print("tweeets local" + str(lista3))
# print("tweets local e data" + str(lista4))


lis = buscar_tweets()
print(lis)



# while(True):
#
#
#     inpt = input("\nOpções:\n 1 - Escolher por cidade\n 2 - Escolher por data\n 3 - Escolher por ambos\n 4 - Sair\n >>>>> ")
#     if(inpt == 4):

