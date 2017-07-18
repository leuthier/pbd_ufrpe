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
dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8')

tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

vectorizer = CountVectorizer(analyzer="word")

freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)


# -- APARTIR DAQUI COMEÇA O NOSSO CÓDIGO



#x1 = buscarTweets(query='since:2017-07-08 until:2017-07-13 #uber', quantidade = 10)
# cricTweet = tweepy.Cursor(api.search, q='victorleuthier', lang="pt").items(1)
# lista = []
#
#
# for twe in cricTweet:
#     lista.append(twe.text)
#     print("ID -- " + str(twe.id))
#     print("TEXO -- "+str(twe.text))
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
#         print(geolocator.reverse(query=str(l[1]) + ", " + str(l[0]), language="pt"))
#     else:
#         print("PLACE -- Sem place")
#     print("CREATED AT -- "+ str(twe.created_at))
#     print("HASHTAGS -- " + str(twe.entities.get('hashtags')))
#     print("SOURCE -- " + str(twe.source))
#
#     print("---------------------------------------------------------------")
#
# freq_testes = vectorizer.transform(lista)
# print(modelo.predict(freq_testes))
# listaa = modelo.predict(freq_testes).tolist()
# print (listaa.count('Positivo'))

def buscarTweets(query, quantidade):
    marca = input("Qual a marca?\n 1 - Uber\n 2 - Cabify \n 3 - 99pop >>>>> ")
    if (marca == "1"):
        id_marca = 1
    elif (marca == "2"):
        id_marca = 2
    elif (marca == "3"):
        id_marca = 3
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
        texto_tweet = i.text
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
        arq.write("dao.Executa_SQL('insert into voudeque.usuario(nome, username, nome_lugar) values(" + str(nome_correto) + ", " + str(screen_name_correto) + ", " + str(lugar_correto) + ");')\n")
        arq.write("id_usuario = dao.Busca_SQL('select id from voudeque.usuario where usuario.nome = " + str(nome_correto) +";')\n")
        arq.write("dao.Executa_SQL('insert into voudeque.tweet(id, texto, tipo, dataHora, id_sentimento, id_usuario) values("
                  + str(id_tweet) + ", " + str(texto_correto) + ", " + str(created_at_tweet) + ", " + str(sentimento) + ", " + "str(id_usuario)" +");')\n")
        arq.write("dao.Executa_SQL('insert into voudeque.tweet_marca(id_tweet, id_marca) values(" + str(id_tweet) + ", " + str(id_marca)  + ");')\n")

    arq.close()

buscarTweets("victorleuthier",10)




def buscarNovasHashtags(hashtag,listaDeMarcas):
    for i in listaDeMarcas:
        if hashtag.lower.contain(i):
            id = "select id from voudeque.marca where nome = '" + str(i) + "'"
            return id















