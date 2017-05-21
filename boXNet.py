#favorita palavras-chave em um twitter automaticamente.
#deve ter conta desenvolvedor pra ter acesso aos tokens
from twitter import *

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
        result = t.favorites.create(_id=tweet['id'])
        print ("Tweet favoritado: "+ (result['text']))
        return result
    #qd ja tiver favoritado o twitter
    except TwitterHTTPError as e:
        print ("Error: ", e)
        return None
    
def auto_fav(q, count=100):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print ("Usuario: @%s"% (a))
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
    print ("Favoritamos um total de %i de %i tweets" % (success,
          len(result['statuses']))+"\n")
    
while True:
    esc = input ("O que vc deseja fazer?\n1- Favoritar \n2- Tweetar \n3- Stalkear \n4- Enviar DM \n5- Sair\n>>> " ) 
    if esc == "5":
        print ("Saiba mais do nosso projeto em\n\nhttps://github.com/leuthier/pbd_ufrpe\n")
        break
    elif esc == "1":
        twt = input("Palavra chave? ")
        num = input("Numeros de tweets para ser analisados e/ou favoritados ")
        auto_fav(twt,num)
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
    
