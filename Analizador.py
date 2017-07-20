# -*- coding: utf-8 -*-
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import persistencia.DataBase as dao
import time
import tweepy
from geopy.geocoders import Nominatim

BUSCAR_TEXTO_TWEETS = "select texto,classe from voudeque.tweet,voudeque.sentimento where voudeque.tweet.id_sentimento=voudeque.sentimento.id;"
BUSCA_HASHTAGS_UBER = "select texto from voudeque.hashtag,voudeque.marca where hashtag.id_marca = marca.id and marca.nome = 'Uber';"
BUSCA_HASHTAGS_CABIFY = "select texto from voudeque.hashtag,voudeque.marca where hashtag.id_marca = marca.id and marca.nome = 'Cabify';"
BUSCA_HASHTAGS_99POP = "select texto from voudeque.hashtag,voudeque.marca where hashtag.id_marca = marca.id and marca.nome = '99pop';"


OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)
geolocator = Nominatim()

listaTweet = []
listaClassificacao = []
modelo = MultinomialNB()
vectorizer = CountVectorizer(analyzer="word")


def treinar(model,vector):
    resposta = dao.Busca_SQL(BUSCAR_TEXTO_TWEETS)
    tweets=[]
    sentimentos=[]
    for i in resposta:
        tweets.append(i[0])
        sentimentos.append(i[1])
    freq_tweets = vector.fit_transform(tweets)
    model.fit(freq_tweets, sentimentos)

def buscarHashtags():
    reUber = dao.Busca_SQL(BUSCA_HASHTAGS_UBER)
    reCab = dao.Busca_SQL(BUSCA_HASHTAGS_CABIFY)
    re99 = dao.Busca_SQL(BUSCA_HASHTAGS_99POP)
    lista = []
    listaUber = []
    lista99 = []
    listaCab =[]
    for i in reUber:
        listaUber.append(i[0])
    lista.append(listaUber)
    for i in reCab:
        listaCab.append(i[0])
    lista.append(listaCab)
    for i in re99:
        lista99.append(i[0])
    lista.append(lista99)
    return lista



def pegarTweetsNovos():
    hashtags = buscarHashtags()
    id_marca = 0
    for i in hashtags:
        id_marca += 1
        if (id_marca == 1 ):
            marca = "uber"
        elif id_marca == 2:
            marca = "cabify"
        elif id_marca == 3:
            marca = "99pop"
        elif id_marca == 4:
            marca = "uber"
            id_marca = 1
        for j in i:
            tweet = tweepy.Cursor(api.search, q=str(j), lang="pt").items(5)
            for twe in tweet:
                try:
                    nome_usuario = str(twe.user.name).replace("\n", " ").replace('"', '')
                    screen_name_usuario = str(twe.user.screen_name).replace("\n", " ").replace('"', '')
                    lugar_usuario = twe.user.location.replace("\n", " ").replace('"', '')
                    id_tweet = twe.id
                    texto_tweet = str(twe.text).replace("\n", " ").replace('"', '')
                    freq_testes = vectorizer.transform([texto_tweet])
                    sent = modelo.predict(freq_testes)[0]
                    if(sent == "Positivo"):
                        sentimento = 1
                    elif(sent == "Negativo"):
                        sentimento = 2
                    else:
                        sentimento = 3
                    created_at_tweet = twe.created_at
                    hashtags = twe.entities.get('hashtags')

                    if(lugar_usuario != ""):
                        dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('" + str(nome_usuario) + "', '" + str(screen_name_usuario) + "', '" + str(lugar_usuario) + "');")
                    else:
                        dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('" + str(nome_usuario) + "', '" + str(screen_name_usuario) + "');")
                    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '"+ str(nome_usuario) +"';")[0][0]
                    dao.Executa_SQL(
                            "insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values('" + str(id_tweet) + "', '" + str(texto_tweet) + "', '" + str(created_at_tweet) + "', '" + str(sentimento)
                            + "', '" + str(id_usuario) +  "');")
                    dao.Executa_SQL(
                            "insert into voudeque.tweet_marca(id_tweet, id_marca) values('" + str(id_tweet) + "', '" + str(marca) + "');")
                    for j1 in hashtags:
                        if marca in j1.get("text").lower():
                            dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('" + str(j.get("text").lower()) + "', '" + str(id_marca) + "');")
                        else:
                            dao.Executa_SQL("insert into voudeque.hashtag(texto) values('" + str(j.get("text").lower()) + "');")
                    if (twe.place != None):
                        coordenadas = twe.place.bounding_box.coordinates[0][0]
                        local = geolocator.reverse(query=str(coordenadas[1]) + ", " + str(coordenadas[0]),
                                                   language="pt")
                        cidade = local.raw["address"]["city"]

                        dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('" + str(coordenadas[1]) + "', '" + str(coordenadas[0]) + "', '" + str(
                            cidade).lower() + "');")

                        id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = '" + str(cidade).lower() + "'" + " and latitude = " + "'" + str(
                            coordenadas[1]) + "'" + "and longitude = " + "'" + str(coordenadas[0]) + "';")[0][0]

                        dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values('" + str(id_tweet) + ", " + str(id_lugar) + "');")
                except:
                    print("Exception")




def iniciar(tempo):
    while True:
        treinar(modelo,vectorizer)
        pegarTweetsNovos()
        time.sleep(tempo)




iniciar(20)





