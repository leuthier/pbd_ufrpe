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
        listaUber.append(i[0][0])
    lista.append(listaUber)
    for i in reCab:
        listaCab.append(i[0][0])
    lista.append(listaCab)
    for i in re99:
        lista99.append(i[0][0])
    lista.append(lista99)
    return lista



def pegarTweetsNovos():
    hashtags = buscarHashtags()
    marca = 0
    for i in hashtags:
        marca += 1
        if marca == 4:
            marca = 1
        for j in i:
            tweet = tweepy.Cursor(api.search, q=str(i), lang="pt").items(50)
            for twe in tweet:
                try:
                    nome_usuario = str(twe.user.name).replace("\n", " ").replace('"', '')
                    screen_name_usuario = str(twe.user.screen_name).replace("\n", " ").replace('"', '')
                    lugar_usuario = twe.user.location.replace("\n", " ").replace('"', '')
                    id_tweet = twe.id
                    texto_tweet = str(twe.text).replace("\n", " ").replace('"', '')
                    created_at_tweet = twe.created_at
                    hashtags = i.entities.get('hashtags')
                    source_tweet = i.source
                    coordinate = ""
                    nome_lugar = ""
                    location = ""
                    if (i.place != None):
                        if (i.place.place_type == "city"):
                            nome_lugar = i.place.name
                            location = geolocator.geocode(i.place.full_name)
                    if(lugar_usuario != ""):
                        dao.Executa_SQL(
                        "insert into voudeque.usuario(nome, username, nome_lugar) values('" + str(nome_usuario) + "', '" + str(screen_name_usuario) + "', '" + str(lugar_usuario) + "');")
                    try:
                        id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '"+ str(nome_usuario) +"';")[0][0]
                        dao.Executa_SQL(
                            "insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(" + str(id_tweet) + ", '" + str(screen_name_usuario) + "', '" + str(lugar_usuario) + "');")
                        dao.Executa_SQL(
                            "insert into voudeque.tweet_marca(id_tweet, id_marca) values(887822641662488576, 1);")
                        dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
                        dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberx', '1');")
                        dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubernata', '1');")
                except:
                    print("Exception")




def iniciar():
    while True:
        treinar(modelo,vectorizer)
        time.sleep(1200)




l=['Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/2znvKCpMEj']
freq_testes = vectorizer.transform(l)
print(modelo.predict(freq_testes))





