import persistencia.DataBase as dao
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889183421695750144, 'Desconto 25% no Cabify PoA 🚘 Código 👉 POTTERCON . Desconto: Origem/destino Barra Shopping. Válidade até: 23/07 🎫 .… https://t.co/n8XdBlJcft', '2017-07-23 18:00:22', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889183421695750144, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889168386701307905, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/rrjJfjwWZJ', '2017-07-23 17:00:37', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889168386701307905, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889153358128459776, 'Desconto 50% no Cabify PoA 🚘 Código 👉 PISAMENOS . Válido entre: 10h-12h / 14h-17h. Válidade até: 23/07 🎫 . #Cabify… https://t.co/X0xtwiu7sY', '2017-07-23 16:00:54', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889153358128459776, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889138163981201408, '#mixcloud | Ouça agora o Setlist Cabify PoA: Músicas p/ embalar seu finde!  🎧 https://t.co/sQpNpwyYku  #Cabify #PoA… https://t.co/4LzDZUzDio', '2017-07-23 15:00:32', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889138163981201408, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mixcloud');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vinícius de Camargo', 'DCVinnie', 'São Leopoldo, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vinícius de Camargo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889125399271178240, 'PARTIU POTTERCON #pottercon #cabify #sunday #sunnyday #girlfriend #gryffindor https://t.co/2DRF1pRsGR', '2017-07-23 14:09:48', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889125399271178240, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pottercon');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sunday');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sunnyday');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('girlfriend');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gryffindor');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889123078097207300, '#Spotify | Playlist Cabify PoA: Curtindo a Vida! . 🎶 https://t.co/VIU793T23u . #Cabify #PoA #PortoAlegre #Spotify… https://t.co/5gq818I9QH', '2017-07-23 14:00:35', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889123078097207300, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portoalegre');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889122980697178114, 'Ganhe R$20,00 na sua primeira corrida de #Cabify usando o código mauricioo322', '2017-07-23 14:00:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889122980697178114, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889108025298087936, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/debEtT29d8', '2017-07-23 13:00:46', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889108025298087936, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889092896170930178, 'Desconto 25% no Cabify PoA 🚘 Código 👉 POTTERCON . Desconto: Origem/destino Barra Shopping. Válidade até: 23/07 🎫 .… https://t.co/LPjcNrswQH', '2017-07-23 12:00:39', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889092896170930178, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889077774048256000, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/spyny2lVwt', '2017-07-23 11:00:34', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889077774048256000, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889062676101558273, 'Desconto 50% no Cabify PoA 🚘 Código 👉 PISAMENOS . Válido entre: 10h-12h / 14h-17h. Válidade até: 23/07 🎫 . #Cabify… https://t.co/LIwJiWMLcw', '2017-07-23 10:00:34', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889062676101558273, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(889047564510781441, '#mixcloud | Ouça agora o Setlist Cabify PoA: Músicas p/ embalar seu finde!  🎧 https://t.co/sQpNpwyYku  #Cabify #PoA… https://t.co/ZSEcV9xzmU', '2017-07-23 09:00:31', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(889047564510781441, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mixcloud');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('André de M. Rocha', 'amrocha78');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'André de M. Rocha';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888984833090875392, 'Foi só o #Flamengo terminar o patrocínio da #uber que se vestiu de #taxi . #adidas #prontofalei #cabify #rumoaohepta', '2017-07-23 04:51:15', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888984833090875392, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('flamengo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('uber');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('taxi');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('adidas');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('prontofalei');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('rumoaohepta');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Tío Cabify', 'TioCabify');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tío Cabify';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888975597933821953, '$3.000 para #Cabify en #Santiago #Valparaiso #Viñadelmar #ConCon #Concepcion #Talcahuano #Reñaca #Quillota #Calera… https://t.co/1D7D2l4Q2h', '2017-07-23 04:14:33', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888975597933821953, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('santiago');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('valparaiso');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('viñadelmar');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('concon');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('concepcion');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('talcahuano');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('reñaca');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('quillota');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('calera');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888941785606705152, 'Desconto 25% no Cabify PoA 🚘 Código 👉 POTTERCON . Desconto: Origem/destino Barra Shopping. Válidade até: 23/07 🎫 .… https://t.co/xQ6w3WvLDE', '2017-07-23 02:00:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888941785606705152, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888926738713104384, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/EZ9LflpkWS', '2017-07-23 01:00:24', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888926738713104384, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888911638111408128, 'Desconto 50% no Cabify PoA 🚘 Código 👉 PISAMENOS . Válido entre: 10h-12h / 14h-17h. Válidade até: 23/07 🎫 . #Cabify… https://t.co/4synxvH9MY', '2017-07-23 00:00:24', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888911638111408128, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888896521609109506, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/DPTTggVRMO', '2017-07-22 23:00:20', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888896521609109506, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888885175379210240, 'Precisa ir a algum lugar e está sem dinheiro? Vai de #Cabify com código VICTORIAM124 e ganhe R$15 pra usar!… https://t.co/LIB1Q6MPNh', '2017-07-22 22:15:15', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888885175379210240, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888881432407535616, '#mixcloud | Ouça agora o Setlist Cabify PoA: Músicas p/ embalar seu finde!  🎧 https://t.co/sQpNpwyYku  #Cabify #PoA… https://t.co/7S64FBsByh', '2017-07-22 22:00:22', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888881432407535616, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mixcloud');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888866397790633989, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/ZYascJ85P5', '2017-07-22 21:00:38', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888866397790633989, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888858748588093440, 'Assim como eu, use #Cabify e ganhe R$20,00 na sua primeira viagem . Registre-se aqui: https://t.co/MKGgKWexbD', '2017-07-22 20:30:14', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888858748588093440, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888851273944006656, 'Desconto 25% no Cabify PoA 🚘 Código 👉 POTTERCON . Desconto: Origem/destino Barra Shopping. Válidade até: 23/07 🎫 .… https://t.co/lcCGPaf07T', '2017-07-22 20:00:32', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888851273944006656, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('André Costa', 'ragazzo_04', 'Aveiro, Portugal');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'André Costa';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888839584708218881, 'Primeira experiência #cabify logo BMW ride 😂#weareallmadhere @ Lisbon, Portugal https://t.co/xyZgXlbwJ1', '2017-07-22 19:14:05', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888839584708218881, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('weareallmadhere');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888836145043427328, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/u4HGrs8h1j', '2017-07-22 19:00:25', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888836145043427328, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888821134166306817, 'Desconto 50% no Cabify PoA 🚘 Código 👉 PISAMENOS . Válido entre: 10h-12h / 14h-17h. Válidade até: 23/07 🎫 . #Cabify… https://t.co/zjrv0NXmEa', '2017-07-22 18:00:46', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888821134166306817, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888806031744225281, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/DzFDsb3nVx', '2017-07-22 17:00:45', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888806031744225281, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888790885068099584, '#mixcloud | Ouça agora o Setlist Cabify PoA: Músicas p/ embalar seu finde!  🎧 https://t.co/sQpNpwyYku  #Cabify #PoA… https://t.co/ANwmHa5Zev', '2017-07-22 16:00:34', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888790885068099584, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mixcloud');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888775887700852736, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/7TyhyaubSr', '2017-07-22 15:00:58', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888775887700852736, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(888760779209572352, 'Desconto 25% no Cabify PoA 🚘 Código 👉 POTTERCON . Desconto: Origem/destino Barra Shopping. Válidade até: 23/07 🎫 .… https://t.co/lxJuvwvcI3', '2017-07-22 14:00:56', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(888760779209572352, 3);")
except:
    print('Erro')
