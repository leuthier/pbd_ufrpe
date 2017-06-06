
import nltk
import re
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

dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8')

tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

vectorizer = CountVectorizer(analyzer="word")

freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)


# -- APARTIR DAQUI COMEÇA O NOSSO CÓDIGO





cricTweet = tweepy.Cursor(api.search, q='#foratemer').items(10)

lista = []
for twe in cricTweet:
    lista.append(twe.text)
    print(twe.text)
print(lista)

freq_testes = vectorizer.transform(lista)
print(modelo.predict(freq_testes))
listaa = modelo.predict(freq_testes).tolist()
print (listaa.count('Positivo'))












