# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
import tweepy

OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)


geolocator = Nominatim()

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
    arq = open("doc.py", "w",encoding="utf8")
    arq.write("import persistencia.DataBase as dao\n")
    for i in tweet:
        nome_usuario = str(i.user.name).replace("\n", " ").replace('"','')
        screen_name_usuario = str(i.user.screen_name).replace("\n", " ").replace('"','')
        lugar_usuario = i.user.location
        id_tweet = i.id
        texto_tweet = str(i.text).replace("\n", " ").replace('"','')
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
        if i.text != None:
            printTexto = i.text.replace("\n"," ")
            try:
                print(printTexto)
            except:
                print(printTexto.encode("utf8"))
        sentimento = 5
        while (sentimento not in (1,2,3)):
            sentimento = int(input("Qual o sentimento deste tweet?\n 1 - Positivo\n 2 - Negativo \n 3 - Neutro >>>>> "))
            if sentimento not in(1,2,3):
                print("[*ERRO*]Sentimento Inexistente")
        if texto_tweet.find("'") != -1:
            texto_tweet.replace("'",":")
            print("houve troca")
        texto_correto = texto_tweet
        nome_correto = nome_usuario
        screen_name_correto = screen_name_usuario
        lugar_correto = lugar_usuario
        arq.write("try:\n")
        if lugar_usuario != "":

            arq.write('    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values(')
            arq.write("'" + str(nome_correto) + "', '" + str(screen_name_correto) + "', '" + str(lugar_correto) + "'")
            arq.write(');")\n')
        else:
            arq.write('    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values(')
            arq.write("'" + str(nome_correto) + "', '" + str(screen_name_correto) + "'")
            arq.write(');")\n')


        arq.write('    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = ')
        arq.write("'" + str(nome_correto) + "'")
        arq.write(';")[0][0]\n')

        if (i.place != None):
            coordenadas = i.place.bounding_box.coordinates[0][0]
            local = geolocator.reverse(query=str(coordenadas[1]) + ", " + str(coordenadas[0]), language="pt")
            try:
                cidade = local.raw["address"]["city"]

                arq.write('    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values(')
                arq.write("'" + str(coordenadas[1]) + "', '" + str(coordenadas[0]) + "', '" + str(cidade).lower() + "'")
                arq.write(');")\n')

                arq.write('    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = ')
                arq.write("'" + str(cidade).lower() + "'" + " and latitude = " + "'" + str(
                    coordenadas[1]) + "'" + "and longitude = " + "'" + str(coordenadas[0]) + "'")
                arq.write(';")[0][0]\n')

                arq.write('    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = ')
                arq.write("'" + str(cidade).lower() + "'")
                arq.write(';")[0][0]\n')

            except:
                print("local sem cidade")
                arq.write("    id_lugar = 'null' \n")
        else:
            arq.write("    id_lugar = 'null' \n")

        arq.write('    str_id_usuario = str(id_usuario)\n')
        arq.write('    str_id_lugar = str(id_lugar)\n')

        arq.write('    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(')
        arq.write(str(id_tweet) + ", '" + str(texto_correto) + "', '" + str(created_at_tweet) + "', '" + str(sentimento) + "', ")
        arq.write('" + str_id_usuario + ", " + str_id_lugar + ')
        arq.write('");")\n')

        arq.write('    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(')
        arq.write(str(id_tweet) + ", " + str(id_marca))
        arq.write(');")\n')

        for j in i.entities.get("hashtags"):
            if marca in j.get("text").lower():
                arq.write('    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values(')
                arq.write("'" + str(j.get("text").lower()) + "', '" + str(id_marca) + "'")
                arq.write(');")\n')
            else:
                arq.write('    dao.Executa_SQL("insert into voudeque.hashtag(texto) values(')
                arq.write("'" + str(j.get("text").lower()) + "'")
                arq.write(');")\n')

        arq.write("except:\n    print('Erro')\n")
    arq.close()

buscarTweets("#cabify",5)


def buscarNovasHashtags(hashtag,listaDeMarcas):
    for i in listaDeMarcas:
        if hashtag.lower.contain(i):
            id = "select id from voudeque.marca where nome = '" + str(i) + "'"
            return id
