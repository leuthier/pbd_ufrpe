from twitter import *
#import json
import webbrowser

OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

def fav_tweet(tweet):
    try:
##        print ("tweet: \n")
##        print (tweet)
##        print ("depois tt")
        result = t.favorites.create(_id=tweet['id'])
##        print("len result: "+str(len(result)))
##        get_info(result)
##        print(result)
        return result
    except TwitterHTTPError as e:
        print ("Error: ", e)
    
        return None


##def get_info(result):
##    for i in range (0,int(num)-1):
##        user = result['statuses'][i]['user']
##        user_location = user['location']
##        user_id_str = user['id_str']
##        user_name = user['name']
##        user_timezone = user['timezone']
##        user_lang = result['statuses'][i]['lang']
##
##        tweet_text = result['statuses'][i]['text']
##        tweet_date_created = result['statuses'][i]['created_at']
##        tweet_hashtag = result['statuses'][i]['entities']['hashtags']
##        tweet_hashtag = result['statuses'][i]['entities']['urls']
##        if "Android" in result['statuses'][i]['source']:
##            tweet_source = "Android"
##        if "iPhone" in result['statuses'][i]['source']:
##            tweet_source = "iPhone"
##        
##        print ("Tweet favoritado: "+ (result['text']))
##        print ("Usuario: @" + user['screen_name'])
##        print ("Localização User: " + location)
##    return
        
def auto_fav(q, count=100):
    result = search_tweets(q, count)
##    print ("result statuses", result['statuses'])
    
    #se fizer len(result)+1 ele so pega o ultimo username
    for i in range (0, len(result)):
        user = result['statuses'][i]['user']
        user_location = user['location']
        user_timezone = user['time_zone']
        user_id_str = user['id_str']
##        user_name = user['name_screen']
##        user_timezone = user['timezone']
        user_lang = result['statuses'][i]['lang']

        tweet_text = result['statuses'][i]['text']
        index_arroba = tweet_text.find("@")
        index_dois_pontos = tweet_text.find(":")
        user_name = tweet_text[index_arroba:index_dois_pontos]
        tweet_text_only = tweet_text.replace("RT " + user_name + ": ", "")
        
        tweet_date_created = result['statuses'][i]['created_at']
        
        tweet_hashtag = result['statuses'][i]['entities']['hashtags']
##        hashtag retorna um dicionario
        tweet_url = result['statuses'][i]['entities']['urls']
        
        if "Android" in result['statuses'][i]['source']:
            tweet_source = "android"
        elif "iPhone" in result['statuses'][i]['source']:
            tweet_source = "iphone"
        elif "Web Client" in result['statuses'][i]['source']:
            tweet_source = "web"
        elif "Twitter Lite" in result['statuses'][i]['source']:
            tweet_source = "lite"
        else:
            tweet_source = "desconhecido"
            
        if 'place' in result.keys():
            place_name = result['place']['full_name']
            place_country = result['place']['country']
            place_lat = result['place']['bounding_box']['coordinates'][0][0][1]
            place_long = result['place']['bounding_box']['coordinates'][0][0][0]
        else:
            place_name = ""
            place_country = ""
            place_lat = ""
            
            place_long = ""

        
        print ("\nUsuario: " + user_name)
        print ("Tweet favoritado: \""+ tweet_text_only +"\"")
        print ("Localização do User: " + user_location)
        print ("De onde foi twittado: " + place_name)
        print ("Coordenadas:\nLAT: " + place_lat + "\nLONG: " + place_long)
##        print ("Time zone: "+ user_timezone)
##        print ("Hashtags utilizadas: " + tweet_hashtag[?])
        print ("Dispositivo de origem do tweet: "+ tweet_source)
    
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
        
    print ("\nFavoritamos um total de " + str(success) + " tweets. \n")

    
while True:  
    esc = input ("O que vc deseja fazer?\n1- Favoritar \n2- Tweetar \n3- Stalkear \n4- Enviar DM \n5- Sair\n>>> " ) 
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
        num = input("Numeros de tweets para ser analisados e/ou favoritados ")
        if num.isdigit():
            if int(num) > 0:
                auto_fav(twt,num)
        else:
            print("\n[ERRO]Insira um numero\n")
    elif esc == "2":
        tweetnow = input("Escreva seu tweet.\nTweet (ate 140 caracteres)\n")
        t.statuses.update(status=tweetnow)
        print ("Tweet postado com sucesso!\n")
    elif esc == "3":
        stalk = input("Digite o username q deseja stalkear.\n@")
        t.statuses.friends_timeline(id=stalk)
    elif esc == "4":
        userdm = input("Digite o username q deseja enviar a msg. \n@")
        dmtext = input("Digite a msg direta q deseja enviar a @"+userdm+".\nMensagem: ")
        t.direct_messages.new(user=userdm,text=dmtext)
        print ("Mensagem direta enviada para @"+ userdm +" com sucesso!\n")
    else:
        print ("Escolha uma opcao valida!\n")
    
