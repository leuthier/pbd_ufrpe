# -*- coding: utf-8 -*-
from twitter import *
#import json
import webbrowser
import sys

OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
#     return t.search.tweets(q=q, result_type='recent', count=count)
    return t.search.tweets(q=q, result_type='recent', count=100)
#     until="2017-06-01"
#     return t.search.tweets(q=q, count=count)

# def fav_tweet(tweet):
#     try:
#         result = t.favorites.create(_id=tweet['id'])
#         return result
#     except TwitterHTTPError as e:
#         print ("Error: ", e)
#     
#         return None

# def get_info(result):
#    for i in range (0,int(num)-1):
#        user = result['statuses'][i]['user']
#        user_location = user['location']
#        user_id_str = user['id_str']
#        user_name = user['name']
#        user_timezone = user['timezone']
#        user_lang = result['statuses'][i]['lang']
#
#        tweet_text = result['statuses'][i]['text']
#        tweet_date_created = result['statuses'][i]['created_at']
#        tweet_hashtag = result['statuses'][i]['entities']['hashtags']
#        tweet_hashtag = result['statuses'][i]['entities']['urls']
#        if "Android" in result['statuses'][i]['source']:
#            tweet_source = "Android"
#        if "iPhone" in result['statuses'][i]['source']:
#            tweet_source = "iPhone"
#        
#        print ("Tweet favoritado: "+ (result['text']))
#        print ("Usuario: @" + user['screen_name'])
#        print ("Localização User: " + location)
#    return
        
def auto_fav(q, count):
    result = search_tweets(q, count)
    arqQuery = open('query.txt','w')
    #print ("result statuses", result).encode(sys.stdout.encoding, errors='replace')
   
    #se fizer len(result)+1 ele so pega o ultimo username
    for i in range (0, len(result['statuses'])):
        tweet = result['statuses'][i]
        global mostrarHashtags
     
        #pegar as listaHashtags
        listaHashtags = tweet['entities']['hashtags']
        mostrarHashtags = "Hashtags encontradas: "
        index = 0
        for hashtag in listaHashtags:
            texto = hashtag['text']
            mostrarHashtags += texto
            if listaHashtags[index]['text'] != listaHashtags[-1]['text']:
                mostrarHashtags += ", "
                
            #criacao de query para novas listaHashtags
            arqQuery.write("insert into hashtag(nome) value('%s');\n" %str(hashtag['text']))
            index += 1
        #informacoes usuario
        user = tweet['user']
        #print(user)
        nomeUsuario = user['name']
        #print(nomeUsuario)
        screenNameUsuario = user['screen_name']
        #print(screenNameUsuario)
        usuarioLocal = user['location']
        #print(usuarioLocal)
        
        #informacoes do tweet
        textoTweet = tweet['text']
        #print(textoTweet)
        dataTweet = tweet['created_at']
        #print(dataTweet)
        urlsTweet = tweet['entities']['urls']
         #print(urlsTweet)
        
        
        
        if(tweet['place'] != None ):
            tipoLugarTweet = tweet['place']['place_type']
            coordinatePlace = tweet['place']['bounding_box']
            if (tipoLugarTweet == None):
                print("tipo lugar = None")
            elif(coordinatePlace['type'] == 'Point'):
                pLongitude = coordinatePlace['coordinates'][0]                
                #print('longitude do place = '+ str(pLongitude))
                pLatitude = coordinatePlace['coordinates'][1]
                #print('Latitude do place = '+ str(pLatitude))
            elif(coordinatePlace['type'] == 'Polygon'):
                pLongitude = coordinatePlace['coordinates'][0][0][0]                
                #print('longitude do place = '+ str(pLongitude))
                pLatitude = coordinatePlace['coordinates'][0][0][1]
                #print('Latitude do place = '+ str(pLatitude))
        
        coordinate = tweet['coordinates']
        if(coordinate == None):
            print ("coordinates == null")
        elif (coordinate['type'] == 'Point'):
            cLongitude = coordinate['coordinates'][0]                
            #print('longitude do coordinate = '+ cLongitude)
            cLatitude = coordinate['coordinates'][1]
            #print('Latitude do coordinate = '+ cLatitude)
        elif(coordinate['type'] == 'Polygon'):
            cLongitude = coordinate['coordinates'][0][0][0]                
            #print('longitude do coordinate = '+ cLongitude)
            cLatitude = coordinate['coordinates'][0][0][1]
            #print('Latitude do coordinate = '+ cLatitude)
            
        
        
        #pegar de onde o usuario twittou
        if "Android" in result['statuses'][i]['source']:
            tweet_source = "android"
        elif "iPhone" in result['statuses'][i]['source']:
            tweet_source = "iphone"
        elif "Web Client" in result['statuses'][i]['source']:
            tweet_source = "web"
        elif "Twitter Lite" in result['statuses'][i]['source']:
            tweet_source = "twitter lite"
        else:
            tweet_source = "desconhecido"
    
        print ("\nUsuario: " + screenNameUsuario)
        print ("Localizacao do Usuario (perfil dele): " + usuarioLocal)
    #     print ("Time zone: "+ user_timezone)
        
        print ("Texto do tweet: "+ textoTweet)
        print ("Data do tweet: "+ dataTweet)
        print (mostrarHashtags)
        
        print ("Tipo lugar: " + tipoLugarTweet)
#         print ("LONGitude do Coordinate: "+ cLongitude)
#         print("LATitude do Coordinate: "+ cLatitude)
        print('longitude do place = '+ str(pLongitude))
        print('Latitude do place = '+ str(pLatitude))
    
        print ("Dispositivo de origem do tweet: "+ tweet_source)
        print("------------------------------------------------------------\n")
            
    
    arqQuery.close()    
                        
#         tweet_text = result['statuses'][i]['text']
#         index_arroba = tweet_text.find("@")
#         index_dois_pontos = tweet_text.find(":")
#         user_name = tweet_text[index_arroba:index_dois_pontos]
#         tweet_text_only = tweet_text.replace("RT " + user_name + ": ", "")
#          
#         tweet_date_created = result['statuses'][i]['created_at']
#          
#         tweet_hashtag = result['statuses'][i]['entities']['listaHashtags']
# ##        hashtag retorna um dicionario
#             
#         if 'place' in result.keys():
#             place_name = result['place']['full_name']
#             place_country = result['place']['country']
#             place_lat = result['place']['bounding_box']['coordinates'][0][0][1]
#             place_long = result['place']['bounding_box']['coordinates'][0][0][0]
#         else:
#             place_name = ""
#             place_country = ""
#             place_lat = ""
#             
#             place_long = ""

        
   
    
    print('\n** Quantidade de tweets buscados: '+str(len(result['statuses']))+"\n") 
    

while True:  
    esc = input ("O que vc deseja fazer?\n1- Pesquisar\n5- Sair\n>>> " ) 
    if esc == "5":
        print ("Saiba mais do nosso projeto em:\n\nhttps://github.com/leuthier/pbd_ufrpe\n")
        esc2 = input("Deseja acessar o repositorio? (S/N) ")
        esc2 = esc2.lower()
        if esc2 == "s":
            webbrowser.open_new("https://github.com/leuthier/pbd_ufrpe")
        elif esc2 == "n":
            print("Obrigado")
        else:
            print("[ERROR]")
        break
    elif esc == "1":
        twt = input("Palavra chave? ")
        num = input("Quantidade de tweets para ser analisados? ")
        #data1 = input("PADRÃO ANO-MES-DIA EX: 2017-05-04. INICIAL: ")
        #data2 = input("PADRÃO ANO-MES-DIA EX: 2017-05-04. FINAL: ")
        if num.isdigit():
            if int(num) > 0:
#                 data ="since:"+str(data1)+ ' until:'+str(data2)+' '+str(twt)
                auto_fav(twt,num)
#                 print("since:"+str(data1)+ ' until:'+str(data2)+' '+str(twt))
        else:
            print("\n[ERRO] Insira um numero\n")
    else:
        print ("[ERRO] Escolha uma opcao valida!\n")