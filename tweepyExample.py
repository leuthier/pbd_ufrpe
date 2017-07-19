# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
import nltk
import re
import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import tweepy

OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)


geolocator = Nominatim()
# dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8')
#
# tweets = dataset['Text'].values
# classes = dataset['Classificacao'].values
#
# vectorizer = CountVectorizer(analyzer="word")
#
# freq_tweets = vectorizer.fit_transform(tweets)
# modelo = MultinomialNB()
# modelo.fit(freq_tweets,classes)


# -- APARTIR DAQUI COMEÇA O NOSSO CÓDIGO



#x1 = buscarTweets(query='since:2017-07-08 until:2017-07-13 #uber', quantidade = 10)
# cricTweet = tweepy.Cursor(api.search, q='victorleuthier', lang="pt").items(50)
# lista = []
#
#
# for twe in cricTweet:
#     print("ID -- " + str(twe.id))
#     x = str(twe.text).replace("\n", " ")
#     if x != None:
#         print("TEXO -- "+str(x))
#     print("NAME -- "+str(twe.user.name))
#     print("SCREEN NAME -- " + str(twe.user.screen_name))
#     print("LOCATION -- "+str(twe.user.location))
#     if(twe.coordinates != None):
#         print("COORDENADA -- "+str(twe.coordinates[0]))
#         print(twe.coordinates)
#     else:
#         print("COORDENADA -- Sem cordenadas")
#     if(twe.place != None):
#         print("PLACE -- " + str(twe.place))
#         print(twe.place.name)
#         l = twe.place.bounding_box.coordinates[0][0]
#         #location = geolocator.geocode(twe.place.full_name)
#         #print(location.latitude)
#         #print(location.longitude)
#         #print(geolocator.reverse(query=str(location.latitude) + ", " + str(location.longitude),language="pt"))
#         kk = geolocator.reverse(query=str(l[1]) + ", " + str(l[0]), language="pt")
#         print(kk.raw["address"]["city"])
#         print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         print("PLACE -- Sem place")
#     print("CREATED AT -- "+ str(twe.created_at))
#     print("HASHTAGS -- " + str(twe.entities.get('hashtags')))
#     for i in twe.entities.get("hashtags"):
#         print("--------",i.get("text"))
#         if "tim" in i.get("text").lower():
#             print("da tim -----------")
#     print("SOURCE -- " + str(twe.source))
#
#     print("---------------------------------------------------------------")

# freq_testes = vectorizer.transform(lista)
# print(modelo.predict(freq_testes))
# listaa = modelo.predict(freq_testes).tolist()
# print (listaa.count('Positivo'))

def buscarTweets(query, quantidade):
    input_marca = input("Qual a marca?\n 1 - Uber\n 2 - Cabify \n 3 - 99pop >>>>> ")
    if (input_marca == "1"):
        id_marca = 1
        marca = "uber"
    elif (input_marca == "2"):
        id_marca = 2
        marca = "cabify"
    elif (input_marca == "3"):
        id_marca = 3
        marca = "99pop"
    else:
        print("MARCA INCORRETA")
        return None
    tweet = tweepy.Cursor(api.search, q=query, lang="pt").items(quantidade)
    arq = open("doc.txt", "w")
    arq.write("import persistencia.DataBase as dao\n")
    for i in tweet:
        nome_usuario = i.user.name
        screen_name_usuario = i.user.screen_name
        lugar_usuario = i.user.location
        id_tweet = i.id
        texto_tweet = str(i.text).replace("\n", " ")
        created_at_tweet = i.created_at
        hashtags = i.entities.get('hashtags')
        source_tweet = i.source
        coordinate = ""
        nome_lugar = ""
        location = ""
        if (i.place != None):
            if (i.place.place_type == "city"):
                nome_lugar = i.place.name
                location = geolocator.geocode(i.place.full_name)
        print(i.text)
        sentimento = 5
        while (sentimento not in (1,2,3)):
            sentimento = int(input("Qual o sentimento deste tweet?\n 1 - Positivo\n 2 - Negativo \n 3 - Neutro >>>>> "))
        texto_correto = texto_tweet
        nome_correto = nome_usuario
        screen_name_correto = screen_name_usuario
        lugar_correto = lugar_usuario
        if lugar_usuario != "":
            arq.write('dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values(')
            arq.write("'" + str(nome_correto) + "', '" + str(screen_name_correto) + "', '" + str(screen_name_correto) + "'")
            arq.write(');")\n')
        else:
            arq.write('dao.Executa_SQL("insert into voudeque.usuario(nome, username) values(')
            arq.write("'" + str(nome_correto) + "', '" + str(screen_name_correto) + "'")
            arq.write(');")\n')
        arq.write('id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = ')
        arq.write("'" + str(nome_correto) + "'")
        arq.write(';")\n')

        arq.write('dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(')
        arq.write(str(id_tweet) + ", '" + str(texto_correto) + "', '" + str(created_at_tweet) + "', '" + str(sentimento) + "', ")
        arq.write('" + str(id_usuario[0][0]) + ')
        arq.write('");")\n')

        arq.write('dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(')
        arq.write(str(id_tweet) + ", " + str(id_marca))
        arq.write(');")\n')

        for j in i.entities.get("hashtags"):
            if marca in j.get("text").lower():
                arq.write('dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values(')
                arq.write("'" + str(j.get("text").lower()) + "', '" + str(id_marca) + "'")
                arq.write(');")\n')
            else:
                arq.write('dao.Executa_SQL("insert into voudeque.hashtag(texto) values(')
                arq.write("'" + str(j.get("text").lower()) + "'")
                arq.write(');")\n')
        if (i.place != None):
            coordenadas = i.place.bounding_box.coordinates[0][0]
            local = geolocator.reverse(query=str(coordenadas[1]) + ", " + str(coordenadas[0]), language="pt")
            cidade= local.raw["address"]["city"]

            arq.write('dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values(')
            arq.write("'" + str(coordenadas[1]) + "', '" + str(coordenadas[0]) + "', '" + str(cidade).lower() + "'")
            arq.write(');")\n')

            arq.write('id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = ')
            arq.write("'" + str(cidade).lower() + "'" + " and latitude = " + "'" + str(coordenadas[1]) + "'" + "and longitude = " + "'" + str(coordenadas[0]) + "'")
            arq.write(';")\n')

            arq.write('dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(')
            arq.write(str(id_tweet) +  ", ")
            arq.write('" + str(id_lugar[0][0]) + ')
            arq.write('");")\n')
    arq.close()

buscarTweets("victorleuthier",2)




def buscarNovasHashtags(hashtag,listaDeMarcas):
    for i in listaDeMarcas:
        if hashtag.lower.contain(i):
            id = "select id from voudeque.marca where nome = '" + str(i) + "'"
            return id















