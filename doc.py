import persistencia.DataBase as dao
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891969231801241601, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-31 10:30:11', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891969231801241601, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vitor Santos', 'jornalistavitor', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vitor Santos';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891967347048796162, 'RT @diariodegoias: Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/1y7a…', '2017-07-31 10:22:42', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891967347048796162, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891947056360804353, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/BxuBSXtSq1', '2017-07-31 09:02:04', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891947056360804353, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891947049620582400, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/1y7aVg5u2e', '2017-07-31 09:02:02', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891947049620582400, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Denis Godoy', 'denisgodoy', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Denis Godoy';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891930332555083776, 'Inscreva-se na Uber usando este link e ganhe 5€ para a primeira viagem https://t.co/M4r4q86x6O &gt; g3e8o4 #uber #portugal #porto #lisboa', '2017-07-31 07:55:37', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891930332555083776, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portugal');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('porto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('lisboa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('KevlarOk', 'kevlarok');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'KevlarOk';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891904941295628288, 'Código uber #Argentina para 2 viajes gratis de $100 en total:  5nm2quddue  😎🎉🚗👏💟💳📍🏙️  #Codigo #Uber #codigouber #Arg #Gratis #UberArgentina', '2017-07-31 06:14:43', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891904941295628288, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('argentina');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('codigo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('codigouber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('arg');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberargentina', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MARLON BRANDO', 'MARLONOFICCIAL', 'Los Angeles - USA');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MARLON BRANDO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891898829242609664, 'RT @OTuitterEumCU: Acabei de Pegar um #UBER prá ir para o Rio de Janeiro e Já estou #Chegando em Manaus! https://t.co/iebIQVuQjP', '2017-07-31 05:50:26', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891898829242609664, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('chegando');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Caio Cesar', 'caiocgo', 'Belo Horizonte, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Caio Cesar';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891866765986336769, 'Ninguém tem que trabalhar mais de 12h por dia para tentar conseguir pagar as contas. Isso é desumano, não é parceria. #uber #cabify', '2017-07-31 03:43:01', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891866765986336769, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891856463538376704, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/HZ5xJaaxNg', '2017-07-31 03:02:05', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891856463538376704, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891856457175642113, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/57ruJWQfFx', '2017-07-31 03:02:03', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891856457175642113, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Hardy Polansky', 'HardyPolansky');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Hardy Polansky';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891851008665673729, 'RT @OTuitterEumCU: Acabei de Pegar um #UBER prá ir para o Rio de Janeiro e Já estou #Chegando em Manaus! https://t.co/iebIQVuQjP', '2017-07-31 02:40:24', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891851008665673729, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('chegando');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Angélica Elmescany', 'elmescania');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Angélica Elmescany';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891845031820242945, 'Motorista do uber só sabe pedir estrelinha. Mas num sabe retribuir com elas! #uberbelem #uber', '2017-07-31 02:16:39', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891845031820242945, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberbelem', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Buteco 512', 'Buteco512');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Buteco 512';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891830796780269573, 'Luciana...eu te entendo😂😂😂#crazy #very #verycrazy #luciana #uber #buteco512 https://t.co/V4nf8Xrgww', '2017-07-31 01:20:06', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891830796780269573, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('crazy');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('very');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('verycrazy');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('luciana');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('buteco512');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DJ SANDER TEODORO', 'DJSANDERTEODORO', 'CURITIBA');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DJ SANDER TEODORO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891825954653450241, 'Destesto com todas minhas forças, motorista tagarela. #Uber — se sentindo desconfortável', '2017-07-31 01:00:51', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891825954653450241, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Diego Leal', 'Eu2Di');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diego Leal';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891790469256159232, '#Uber ... Função...Levar a melhor parte do meu fds embora...', '2017-07-30 22:39:51', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891790469256159232, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Renan Moratto', 'remorato', 'São Paulo - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renan Moratto';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891774607031664640, 'a 99 tem o serviço alternativo ao #uber e também tem #cupom no 99pop usa lá o código RENANMORATTO https://t.co/oDlJwUQES4 #desconto #99taxi', '2017-07-30 21:36:49', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891774607031664640, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('99taxi');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Renan Moratto', 'remorato', 'São Paulo - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renan Moratto';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891773817592459266, 'Pra primeira viagem da #cabify #desconto #taxi #uber usa o #cupom renanm96 &gt;&gt; R$15 #cupomcabify #cupomuber #desconto', '2017-07-30 21:33:41', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891773817592459266, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('taxi');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupomcabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cupomuber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891772981298552832, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-30 21:30:21', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891772981298552832, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('LUCIANA CARVALHO', 'JonBonROCKJR');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'LUCIANA CARVALHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891770848864071682, 'RT @OTuitterEumCU: Acabei de Pegar um #UBER prá ir para o Rio de Janeiro e Já estou #Chegando em Manaus! https://t.co/iebIQVuQjP', '2017-07-30 21:21:53', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891770848864071682, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('chegando');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rodrigo Gomes', 'rgomesbr', 'Santo André, SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rodrigo Gomes';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.815924', '-46.567276', 'são bernardo do campo');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'são bernardo do campo' and latitude = '-23.815924'and longitude = '-46.567276';")[0][0]
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = 'são bernardo do campo';")[0][0]
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891770237183569920, 'Meu cupom :uberrgomes: te dá R$ 20 de desconto em suas primeiras viagens (10 cada) com @Uber_Brasil @Uber #uber #desconto #cupom #promocao', '2017-07-30 21:19:27', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891770237183569920, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promocao');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891765870548144128, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/iLwWtpb5rN', '2017-07-30 21:02:06', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891765870548144128, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891765864793595905, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/8mRJDR1QUx', '2017-07-30 21:02:05', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891765864793595905, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891761623492329473, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-30 20:45:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891761623492329473, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Danrley Barbosa', 'SandyDanrley', 'Porteirinha, Minas Gerais');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Danrley Barbosa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732881671954432, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasild', '2017-07-30 18:51:01', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891732881671954432, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubersurvivor', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubermg', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('linda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('lindo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cute');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('br');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('twitter');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('brasild');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Danrley Barbosa', 'SandyDanrley', 'Porteirinha, Minas Gerais');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Danrley Barbosa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732856946524161, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasie', '2017-07-30 18:50:55', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891732856946524161, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubersurvivor', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubermg', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('linda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('lindo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cute');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('br');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('twitter');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('brasie');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Danrley Barbosa', 'SandyDanrley', 'Porteirinha, Minas Gerais');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Danrley Barbosa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732792178089984, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasil', '2017-07-30 18:50:39', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891732792178089984, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubersurvivor', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubermg', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('linda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('lindo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cute');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('br');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('twitter');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('brasil');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Gabriela', 'GabGeminiana', 'Rio Grande do Sul, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Gabriela';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891724424931680256, 'to com um certo nojo da #Uber', '2017-07-30 18:17:24', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891724424931680256, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Táxi Rio', 'taxinorio', 'Brasil - Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Táxi Rio';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891723792761991168, 'Carro da UBER com Kit de gás vencido explode em posto de gasolina no Rio de Janeiro. #explosão #UBER #fiscalização… https://t.co/uQo8acV13O', '2017-07-30 18:14:54', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891723792761991168, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('explosão');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('fiscalização');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Empregos Em Manaus', 'EmpregosEmMAO');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Empregos Em Manaus';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891715475100577792, 'Já utilizou o #Uber em Manaus? Ainda não? Aproveite,  já estão aceitando pagamento em dinheiro! Use o código: EmpregosEmManaus  #UberManaus', '2017-07-30 17:41:51', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891715475100577792, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubermanaus', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891708772447596547, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/fax8WQUWyr', '2017-07-30 17:15:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891708772447596547, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891676904880840704, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #uBER #cÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-30 15:08:35', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891676904880840704, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891675264647917568, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/9qXP54bzYd', '2017-07-30 15:02:04', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891675264647917568, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891675259006586880, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/b5n3hUmo6e', '2017-07-30 15:02:02', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891675259006586880, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('cleberson fla', 'fla_cleberson');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'cleberson fla';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891669948711481344, 'RT @OficialAvioes: Esse é o som do grito dos #Aviãozeiros de #PastosBons!😻🔝 #FazOXis do Comandante pra voar alto hoje #DeMãosAtadas e #Uber…', '2017-07-30 14:40:56', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891669948711481344, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('aviãozeiros');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pastosbons');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('fazoxis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('demãosatadas');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Niamh Robertson', 'oneclebo1972');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Niamh Robertson';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891666702483824641, 'RT @marioasato: Galera, 20 reais de desconto nas duas primeiras viagens de #uber usando esse cupom de desconto. z15y4xc8ue', '2017-07-30 14:28:02', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891666702483824641, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Alexandre Souza ♎️', 'AleSoouza23', 'Duque de Caxias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Alexandre Souza ♎️';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.08302', '-43.795449', 'itaguaí');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'itaguaí' and latitude = '-23.08302'and longitude = '-43.795449';")[0][0]
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = 'itaguaí';")[0][0]
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891665592918429696, 'Vem ser Feliz !!! #uber #bomdia #uberbrasil #motorista #cadastro #indicação  Eu uso a uber para… https://t.co/XuKwzHbg02', '2017-07-30 14:23:38', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891665592918429696, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('bomdia');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberbrasil', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('motorista');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cadastro');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('indicação');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891648371257204736, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-07-30 13:15:12', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891648371257204736, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lucas Montilla', 'Lucasms87', 'Curitiba-PR');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lucas Montilla';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-27.8389356', '-48.6103127', 'florianópolis');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'florianópolis' and latitude = '-27.8389356'and longitude = '-48.6103127';")[0][0]
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = 'florianópolis';")[0][0]
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891635384387547136, 'Pra começar bem o domingo.  #NoFilter #Uber #5estrelas #Floripa… https://t.co/0ZIfGspEKa', '2017-07-30 12:23:36', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891635384387547136, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('nofilter');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('5estrelas');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('floripa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Vidadeuber', 'vidadeuber');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vidadeuber';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891635270201856000, 'Bom dia galera.  Mas conversas com passageiros sempre pode sair algo de bom. #uber #vidadeuber #saopaulo https://t.co/vx504TEhNB', '2017-07-30 12:23:08', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891635270201856000, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('vidadeuber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('saopaulo');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vinicius Soares', 'cantorvinicius_', 'Rio de Janeiro, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vinicius Soares';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891608821226975232, 'Agradecer a #UBER por evitar um homicídio doloso, sim, que tem intenção de matar mesmo... kkkkkkkk que medo! 😱😂', '2017-07-30 10:38:02', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891608821226975232, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Verbena Ash', 'verbenash', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Verbena Ash';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891604490499088384, 'Por esse e outros motivos parei de andar de táxi depois que aplicativos como o #uber foram lançados! Táxi virou a... https://t.co/zlHfFhEZSZ', '2017-07-30 10:20:50', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891604490499088384, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891591778058555392, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-30 09:30:19', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891591778058555392, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891584667241127936, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/y4Ye2aALMw', '2017-07-30 09:02:04', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891584667241127936, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891584662279270401, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/7i6PGCuHR2', '2017-07-30 09:02:02', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891584662279270401, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lloyd', 'Lloyd9611', 'PH ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lloyd';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891567466542809088, '#UBERPROMO #UBERCODE #UBER #UBERPH #OFF50 arons1102ui &lt;---PROMO CODE 50 PESOS OFF', '2017-07-30 07:53:43', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891567466542809088, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberpromo', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberph', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('off50');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Kend ❄️', 'beabeables', 'Santos, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Kend ❄️';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891551645766758400, 'Mano, tudo bem ter medo de subir no morro, mas é só n aceitar a corrida, do q ficar a viagem toda falando merda #uber', '2017-07-30 06:50:51', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891551645766758400, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Thalles Luiz', 'tallesluiz2', 'Canguaretama, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Thalles Luiz';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891522725243703296, 'RT @pirulitodemacho: Acho que o meu #Uber acabou de chegar #PLDM🍭 RT🔁 FAV❤ https://t.co/2ryL1UARX6', '2017-07-30 04:55:56', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891522725243703296, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pldm');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Garotinho', 'GarotiinhoBA');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Garotinho';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891517002740899840, 'RT @pirulitodemacho: Acho que o meu #Uber acabou de chegar #PLDM🍭 RT🔁 FAV❤ https://t.co/2ryL1UARX6', '2017-07-30 04:33:11', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891517002740899840, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pldm');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Fernando Souza', 'Fernando348', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Fernando Souza';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891509236357836800, 'Eu não tô acreditando... #Uber https://t.co/tPFzV9qhq6', '2017-07-30 04:02:20', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891509236357836800, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Denis Godoy', 'denisgodoy', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Denis Godoy';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891495308441661440, 'Viagem Uber grátis! Para resgatar sua viagem, inscreva-se usando este link: https://t.co/jglT1392Ff &gt; g3e8o4 #uber #portugal #porto #lisboa', '2017-07-30 03:06:59', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891495308441661440, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portugal');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('porto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('lisboa');")
except:
    print('Erro')
import persistencia.DataBase as dao
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tom de Vasconcelos', 'TOM_BETA_', 'Betim-MG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tom de Vasconcelos';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892161609828896769, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @MFilaretti: #timbeta - Durma com ideias. Acorde com atitudes. #u…', '2017-07-31 23:14:38', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892161609828896769, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tom de Vasconcelos', 'TOM_BETA_', 'Betim-MG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tom de Vasconcelos';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892161470435393536, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @pauloadriano47: RT @TiagoBeta2015: #timbeta - Valorize-se. É grá…', '2017-07-31 23:14:04', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892161470435393536, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892155335238197253, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @pauloadriano47: RT @TiagoBeta2015: #timbeta - Valorize-se. É grátis. #umRei', '2017-07-31 22:49:42', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892155335238197253, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('umrei');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('FabiMoreira.', 'fah_moreira', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'FabiMoreira.';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892152718848131073, 'Vovó agora só quer andar de #uber, Braseeel !!!!', '2017-07-31 22:39:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892152718848131073, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892150469379973121, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-31 22:30:21', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892150469379973121, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('piriguete', 'HannierMiranda', 'Porto Velho, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'piriguete';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892138509808566272, 'Oi?? #uber nera barato? https://t.co/K8aYPh2R4J', '2017-07-31 21:42:50', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892138509808566272, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('GIVALDO JUNIOR', 'givajunior23', 'Recife-PE, ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'GIVALDO JUNIOR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892132293837557760, 'Mais uma vez pego um #uber que vem com o ar desligado,nota baixíssima e mesmo assim tá rodando.@Uber_Brasil já foi bom. agora é1 táxi barato', '2017-07-31 21:18:08', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892132293837557760, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892128251023380482, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/pHmlrWHunG', '2017-07-31 21:02:04', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892128251023380482, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892128244585164800, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/ey6a0a72eA', '2017-07-31 21:02:03', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892128244585164800, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892124010682691585, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-31 20:45:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892124010682691585, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rodrigo Gonçalves', 'rodrigorodz_', 'Cuiabá, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rodrigo Gonçalves';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892116586022227970, '#CuiabaSemVivo parabens @TelefonicaBr por deixar Cuiaba sem internet nos celulares! E os motoristas #uber como ficam?', '2017-07-31 20:15:43', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892116586022227970, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cuiabasemvivo');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Belit', 'belzboo', 'São Paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Belit';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892110984889892868, 'Acabei de ver uma denúncia de um motorista de #Uber, acho que os apps deviam pegar os dados desses motoristas e bloquear no app tmb.', '2017-07-31 19:53:28', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892110984889892868, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892071154952884227, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/E0US2Lisxb', '2017-07-31 17:15:11', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892071154952884227, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Artur', 'arturjunior', 'to');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Artur';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892069406573985793, 'Usa esse código e ganhe 10 de desconto na corrida run6aue #uber', '2017-07-31 17:08:15', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892069406573985793, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('rony.matos', 'rony_matos');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'rony.matos';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892068550311129088, 'RT @rony_matos: #motoG5S com o #uber  + o GPS não funciona. Quando uso o Uber x #waze  (dá falta de sinal GPS) o maps não da erro.  #motoro…', '2017-07-31 17:04:50', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892068550311129088, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('motog5s');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('waze');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892064732617863168, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @MFilaretti: #timbeta - Durma com ideias. Acorde com atitudes. #umRei', '2017-07-31 16:49:40', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892064732617863168, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('umrei');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Cleber J Coimbra Jr', 'cleberjr67');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cleber J Coimbra Jr';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892053907194753028, '#VouDeUber #NãoaoDecreto #Uber #CampoGrande #MS #MatoGrossodoSul FORA POLÍTICOS SAFADOS QUE SÓ QUEREM LEVAR VANTAGEM E PROPINA.', '2017-07-31 16:06:39', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892053907194753028, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('voudeuber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('nãoaodecreto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('campogrande');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ms');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('matogrossodosul');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Uber Dicas', 'uberdicas', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Uber Dicas';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892053502826090497, 'Levar marmita no carro, nóis #PorQueNao  #Uber', '2017-07-31 16:05:03', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892053502826090497, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('porquenao');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jornal do Tocantins', 'jornaltocantins', 'Tocantins, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jornal do Tocantins';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892052247957225474, 'Justiça derruba questionamento sobre fiscalização do #Uber https://t.co/lCvGColnnp (cont. aberto) https://t.co/lmj8dQXZL2', '2017-07-31 16:00:04', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892052247957225474, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('MBA Jobs', 'mbajobpostings');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MBA Jobs';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892041879260364800, 'RT @MBA_Jobs_USA_3: Senior Operations #manager, #business Intelligence - Chicago: #Uber, USA (Illinois). https://t.co/zPwX4mVaI6 #MBA #jobs…', '2017-07-31 15:18:52', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892041879260364800, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('manager');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('business');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mba');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('jobs');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MBA Jobs in USA', 'MBA_Jobs_USA_3', 'Geneva, Switzerland');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MBA Jobs in USA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892041877008076802, 'Senior Operations #manager, #business Intelligence - Chicago: #Uber, USA (Illinois). https://t.co/zPwX4mVaI6 #MBA #jobs #USA', '2017-07-31 15:18:51', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892041877008076802, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('manager');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('business');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mba');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('jobs');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('usa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892038950185050112, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-31 15:07:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892038950185050112, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892037656032546820, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/YRhYlP2lNc', '2017-07-31 15:02:05', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892037656032546820, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'Goiânia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892037650504454144, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/kn2pB6LsBR', '2017-07-31 15:02:03', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892037650504454144, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mosby', 'porra_feh', 'Maceió');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mosby';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892018511366762497, 'Código de desconto #UBER qg833cvpue aproveitemm', '2017-07-31 13:46:00', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892018511366762497, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
