import persistencia.DataBase as dao
# -*- coding: utf-8 -*-

#UBER#
#------------------------------------
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MarceloTV', 'MarceloTV', 'MarceloTV');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MarceloTV';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887786640063832064, '#uber dá $50 te chama de vip por usar muito e depois cobra a mais por algo q te deu oi?!  #ubereats te foides?!@ubeareats_br', '2017-07-19 21:30:03', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887786640063832064, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887779598053900288, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/MYfx4kve2v', '2017-07-19 21:02:04', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779598053900288, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887779591657594888, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/kOY7djekmY', '2017-07-19 21:02:03', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779591657594888, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vitória Silva', 'masoqVih', 'masoqVih');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vitória Silva';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887777548008075264, 'Quer andar de graça no Uber em Manaus?  Utilize o seguinte código: EmpregosEmManaus https://t.co/mTz43ayAmt #uber… https://t.co/jGtzWGyTSg', '2017-07-19 20:53:56', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887777548008075264, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887775352793247745, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-19 20:45:12', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887775352793247745, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887774517124149248, '#DESCONTO #UBER 69r4uv5hue RT @RahulTayde9: Não foi dessa vez mas na próxima dará certo !! 😎 #TimBeta #BetaAjudaBeta https://t.co/Y09iP7O3hX', '2017-07-19 20:41:53', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887774517124149248, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887771557052940289, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 20:30:07', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887771557052940289, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jose', 'Jose25873018');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jose';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887765746444644353, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-19 20:07:02', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887765746444644353, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Daniel Alves', 'alves929_alves');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Daniel Alves';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887764581761810433, 'Aproveite a promoção para você implantar o aplicativo de táxi estilo uber https://t.co/F9lt7T8jZr #uber #ubereats #ifood #ifoodsalva #tbt', '2017-07-19 20:02:24', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887764581761810433, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifood');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifoodsalva');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tbt');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Van', 'VanilseUeda', 'VanilseUeda');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Van';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887740861865504768, 'Meu app do #Uber nunca mostra placa do carro.    Mas que caralha 😔', '2017-07-19 18:28:09', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887740861865504768, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Campo Grande News', 'cgrnews', 'cgrnews');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Campo Grande News';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887733579899449344, 'Decreto prevê cassação imediata do alvará de licenciamento, interdição parcial ou total das empresas. #CGNews #Uber https://t.co/V741UsBIYX', '2017-07-19 17:59:13', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887733579899449344, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cgnews');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Uber da Depressão', 'uberdepressivo', 'uberdepressivo');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Uber da Depressão';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887725161402839046, 'Novo serviço...Ubermula...#Uber #Uberblack #Uberislife #Uberdepressivo #Uberlover #Uberx https://t.co/4WjhfAet1h', '2017-07-19 17:25:46', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887725161402839046, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberblack', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberislife', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberdepressivo', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberlover', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberx', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vic on Ice trash', 'Vic_Walker', 'Vic_Walker');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vic on Ice trash';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887722504244125696, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/nevaKiBg03', '2017-07-19 17:15:12', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887722504244125696, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('heverton carvalho', 'hetocarvalho1', 'hetocarvalho1');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'heverton carvalho';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699695262474241, 'voucher pra trem fantasma #Uber', '2017-07-19 15:44:34', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699695262474241, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699029211131904, '#DESCONTO #UBER 69r4uv5hue RT @titapeace: Cuidado com o destino, ele brinca com as pessoas... #TimBeta #timbetalab', '2017-07-19 15:41:55', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699029211131904, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetalab');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'havanalab');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887690847638216705, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-19 15:09:25', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887690847638216705, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688997299945472, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/2znvKCpMEj', '2017-07-19 15:02:04', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688997299945472, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688991436398595, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg', '2017-07-19 15:02:02', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688991436398595, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('André Luis Urel', 'andre_urel', 'andre_urel');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'André Luis Urel';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887687582653575173, '#Wolverine virou #Uber #Logan Putz o desemprego afetou até os super heróis', '2017-07-19 14:56:26', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887687582653575173, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('wolverine');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('logan');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887680999252873217, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 14:30:17', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887680999252873217, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cristina #timbeta', 'cristinamfcris', 'cristinamfcris');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cristina #timbeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887674731960336385, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @tthaisandrade18: Beta ajuda beta? #timbeta #betaajudabeta #OperacaoBetaLab #RT https://t.co/…', '2017-07-19 14:05:22', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887674731960336385, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('operacaobetalab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('rt');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carol', 'c4rou', 'c4rou');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carol';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887671491751538689, '#uber em Recife é mara! Tem até Wi-Fi :)', '2017-07-19 13:52:30', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887671491751538689, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-8.157554', '-35.019805', 'jaboatão dos guararapes');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'jaboatão dos guararapes' and latitude = '-8.157554'and longitude = '-35.019805';")

dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887671491751538689, " + str(id_lugar[0][0]) + ");")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mamãe Compara', 'mamaecompara', 'mamaecompara');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mamãe Compara';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887669598279127040, 'Pessoal, alguém tem algum contato do marketing nas empresas: #Airbnb, #Uber, #A99, #Cabify, #UOL, #Sugar,... https://t.co/9mJclaaWkU', '2017-07-19 13:44:58', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887669598279127040, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('airbnb');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('a99');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('uol');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sugar');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887662128487776256, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-07-19 13:15:18', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887662128487776256, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ângelo Rodrigues', 'angeloOmusic', 'angeloOmusic');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ângelo Rodrigues';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887659711365042176, 'Vai uma boleia?  #uber #uberportugal #uberpool https://t.co/bxuTxq6Pej', '2017-07-19 13:05:41', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887659711365042176, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberportugal', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberpool', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887653741884841984, '#DESCONTO #UBER 69r4uv5hue RT @tthaisandrade18: Vamos família! #timbeta  #OperacaoBetaLab #BetaAjudaBeta #RT https://t.co/Yx25C3kCQh', '2017-07-19 12:41:58', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887653741884841984, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('operacaobetalab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('rt');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887653719235600384, '#DESCONTO #UBER 69r4uv5hue RT @tthaisandrade18: Beta ajuda beta? #timbeta #betaajudabeta #OperacaoBetaLab #RT https://t.co/Yb3fNDz7TZ', '2017-07-19 12:41:53', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887653719235600384, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('operacaobetalab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('rt');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Albertina D Dias', 'AlbertinaDDias', 'AlbertinaDDias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Albertina D Dias';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887647043283329024, 'O que podemos aprender da #Uber sobre transformação #digital? #FutureofWork #MercerDigital https://t.co/190rowN1TF https://t.co/Ri9vqdOuGH', '2017-07-19 12:15:21', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887647043283329024, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('digital');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('futureofwork');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mercerdigital');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887610390611464193, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @Mikelle_milena: Bom dia família #TimBeta https://t.co/NdBJksAdPx', '2017-07-19 09:49:42', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887610390611464193, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887609246199816193, 'Use meu cupom de desconto da uber (15 REAIS) 6duun #UBER', '2017-07-19 09:45:09', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887609246199816193, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887598404918005760, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/KWUbpf4uxL', '2017-07-19 09:02:05', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887598404918005760, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887598399696056320, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/vv8C7Htqoa', '2017-07-19 09:02:03', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887598399696056320, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887507805913174016, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/gSYATvLg4N', '2017-07-19 03:02:04', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887507805913174016, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887507799600750592, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/GkgXOTHDCX', '2017-07-19 03:02:03', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887507799600750592, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887499887063035904, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 02:30:36', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887499887063035904, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Bob Cuspe', 'rgommez', 'rgommez');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Bob Cuspe';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887494555649667073, 'RT @portaluai: #Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5…', '2017-07-19 02:09:25', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887494555649667073, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887489584791158784, '#SDV HD✨RXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @Wolf_Light__: dias de luta e dias de glória  #TimBeta #TimBetaAjudaTimBeta   #grato', '2017-07-19 01:49:40', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887489584791158784, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajudatimbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('grato');")

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('TEXTOS NO FIXADO', 'ThomHipolito', 'ThomHipolito');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'TEXTOS NO FIXADO';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887479159831883776, 'Uma garota pegou um #uber vindo na nove de junho comigo, não peguei o contato dela, talvez seríamos grandes amigos', '2017-07-19 01:08:14', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887479159831883776, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887474510643036161, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Você me bagunça. E ao mesmo tempo me ajeita, me completa #timbeta', '2017-07-19 00:49:46', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887474510643036161, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887474501163917314, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Eu realmente me importo com você #timbeta', '2017-07-19 00:49:44', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887474501163917314, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")

dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.08302', '-43.795449', 'itaguaí');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'itaguaí' and latitude = '-23.08302'and longitude = '-43.795449';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887472633993981952, " + str(id_lugar) + ");")

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('@Renata', 'Re_mcd', 'Re_mcd');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '@Renata';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887469258715934724, 'Em plena porta de metrô e não tem 1 #uber disponível!!! Que horror! https://t.co/frZ6KcYLwP', '2017-07-19 00:28:54', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887469258715934724, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Anderson_ce', 'AndersonLima_ce', 'AndersonLima_ce');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Anderson_ce';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887463183358840832, 'Estou enviando um desconto de R$6 em cada uma de suas primeiras 2 viagens com a Uber. Para aceitar, use o código zn35nw  #Uber #UberCode', '2017-07-19 00:04:45', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887463183358840832, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887459441318268928, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Me apeguei a algo que nunca me pertenceu #timbeta', '2017-07-18 23:49:53', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887459441318268928, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887459405247262720, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Eu preciso de você, nem que seja para brigar #timbeta', '2017-07-18 23:49:45', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887459405247262720, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887444297200611328, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Porque quando tu ama, ser fiel é um prazer, e não um sacrifício #timbeta', '2017-07-18 22:49:43', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887444297200611328, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887442328058814464, '#DESCONTO #UBER 69r4uv5hue RT @AnaVergueiro86: Gente, cadê a ajuda no RT? #BetaQuerLab #BetaAjudaBeta #timbetaajudatimbeta #sdv #timbeta', '2017-07-18 22:41:53', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887442328058814464, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajudatimbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lucas', 'UnCaraQualquer', 'UnCaraQualquer');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lucas';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887436724384800768, '#Uber Black é muito bom', '2017-07-18 22:19:37', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887436724384800768, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jazz', 'Jaaaaaziel', 'Jaaaaaziel');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jazz';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887433252310585346, '@sophiacabraal @Wmelomedeiros #uber não caridade kkkk já viram o preço da gasolina?', '2017-07-18 22:05:49', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887433252310585346, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rogerio08 #TimBeta', 'RogerioBeta08', 'RogerioBeta08');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rogerio08 #TimBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887425109815959552, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @CMS_Chagas: Boa noite para os que ficam. #BetaQuerLab  #TimBeta', '2017-07-18 21:33:28', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887425109815959552, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rogerio08 #TimBeta', 'RogerioBeta08', 'RogerioBeta08');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rogerio08 #TimBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887425101389602817, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @Rodrigolopeswar: segue o plano pessoal !   #TimBeta  #BetaQuerLab  #betaseguebeta  #betalab', '2017-07-18 21:33:26', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887425101389602817, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaseguebeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betalab');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887417209567543297, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/X19KFr7Le4', '2017-07-18 21:02:04', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887417209567543297, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887417203037016069, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/WfyKBWD2FN', '2017-07-18 21:02:03', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887417203037016069, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887412971848314881, 'Use meu cupom de desconto da uber (15 REAIS) 6duun #UBER', '2017-07-18 20:45:14', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887412971848314881, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887412952839708672, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-18 20:45:09', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887412952839708672, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887409160710737920, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-18 20:30:05', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887409160710737920, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Pretty hate machine', 'feeh_withlasers', 'feeh_withlasers');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Pretty hate machine';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887402140704141314, 'an9vy4wmue desconto de R$20,00 no uber e 25,00 no ubereats #uber #cupomuber #ubercupom', '2017-07-18 20:02:12', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887402140704141314, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cupomuber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercupom', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('TREVISAN', 'trevisan_marcos', 'trevisan_marcos');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'TREVISAN';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887401712952250368, '#Uber use o código promocional UBERGANHEI20UE e ganhe duas corridas com R$ 10 de desconto. #vaideUber', '2017-07-18 20:00:30', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887401712952250368, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('vaideuber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BRIAN MENDES', 'BrianMend', 'BrianMend');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BRIAN MENDES';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887400813383094273, 'Quer ganhar #DescontoUber? #uber #CodigoUber  Use o código:     watlrk', '2017-07-18 19:56:55', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887400813383094273, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('descontouber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('codigouber', '1');")
dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-3.88818', '-38.638212', 'maracanaú');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'maracanaú' and latitude = '-3.88818'and longitude = '-38.638212';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887400813383094273, " + str(id_lugar) + ");")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887398995064221697, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @Lima1Cludio: RT @CROSKM: Bom dia pessoa. Segue que eu te sigo, #TimBeta.', '2017-07-18 19:49:42', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887398995064221697, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Dux', 'DuxCoelho', 'DuxCoelho');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Dux';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887395079060692992, 'Chateado. Não tem #Uber em Penedo. https://t.co/SsszsJ00iW', '2017-07-18 19:34:08', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887395079060692992, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MOVITAXI BRASIL', 'MOVITAXIBRASIL', 'MOVITAXIBRASIL');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MOVITAXI BRASIL';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887391616599826432, '@eduardoamorimse Parabéns pela coerência, a sociedade hipócrita ainda há de entender um dia o mal que o #uber causa...', '2017-07-18 19:20:22', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887391616599826432, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Elisa Travalloni', 'Travalloni', 'Travalloni');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Elisa Travalloni';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887384730794065920, 'E #uber cada vez mais lambão', '2017-07-18 18:53:01', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887384730794065920, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Eduardo Almeida', 'eoalmeida', 'eoalmeida');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Eduardo Almeida';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887384100843253761, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Meu pior defeito é criar expectativas demais #timbeta', '2017-07-18 18:50:31', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887384100843253761, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Julien Jay', 'Julien_Jay', 'Julien_Jay');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Julien Jay';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887382627723997184, '@romainturkowiak Des fadas je te jure ! #Uber', '2017-07-18 18:44:39', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887382627723997184, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('covfefe', 'ewertonleaoK');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'covfefe';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887379842827792389, '@maltzsama coloca na ponta do lapis se n é melhor #uber', '2017-07-18 18:33:35', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887379842827792389, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Renato Marinho', 'renato_marinho');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renato Marinho';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887379367231455233, 'Contas #Uber em alta no mercado ilegal. Phishing e reuso de senhas são as principais ameaças. Não reuse senhas. Stay tuned. #morphuslabs', '2017-07-18 18:31:42', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887379367231455233, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('morphuslabs');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('LUIZ COSTA', 'luizcosta76', 'luizcosta76');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'LUIZ COSTA';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887369990822920193, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Meu pior defeito é criar expectativas demais #timbeta', '2017-07-18 17:54:27', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887369990822920193, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887368804564701185, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Meu pior defeito é criar expectativas demais #timbeta', '2017-07-18 17:49:44', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887368804564701185, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vic on Ice trash', 'Vic_Walker', 'Vic_Walker');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vic on Ice trash';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887360105234214912, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/hAxQ8xpSAm', '2017-07-18 17:15:10', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887360105234214912, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887336641437761536, '#DESCONTO #UBER 69r4uv5hue RT @Rodrigolopeswar: segue o plano pessoal !   #TimBeta  #BetaQuerLab  #betaseguebeta  #betalab', '2017-07-18 15:41:55', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887336641437761536, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaseguebeta');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betalab');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Paulo Anderson', '_pauloanderson', '_pauloanderson');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Paulo Anderson';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887330438360031232, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 15:17:16', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887330438360031232, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'havanalab');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887328328709013504, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-18 15:08:53', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887328328709013504, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887326856931889152, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/IrbatKl7jI', '2017-07-18 15:03:03', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887326856931889152, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887326636013760516, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/rmPrn95SWd', '2017-07-18 15:02:10', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887326636013760516, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Eevee son', 'iwyson', 'iwyson');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Eevee son';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887325676143087616, 'Só eu que acho a #uber extremamente organizada? Nunca tive um resquício de problema.', '2017-07-18 14:58:21', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887325676143087616, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-3.88818', '-38.638212', 'maracanaú');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'maracanaú' and latitude = '-3.88818'and longitude = '-38.638212';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887325676143087616, " + str(id_lugar) + ");")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ronilson Geraldo', 'ronilsonsalg', 'ronilsonsalg');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ronilson Geraldo';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887311531888791553, 'RT @portaluai: #Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5…', '2017-07-18 14:02:09', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887311531888791553, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Portal UAI', 'portaluai', 'portaluai');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Portal UAI';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887311012008939520, '#Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5qCzzg', '2017-07-18 14:00:05', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887311012008939520, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Gugagustavo', 'Gugagustavo13');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Gugagustavo';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887310554402099200, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 13:58:16', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887310554402099200, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Estado de Minas', 'em_com', 'em_com');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Estado de Minas';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887307222929244161, '#Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/2KgjPneUNC https://t.co/8OoqFH4n8C', '2017-07-18 13:45:01', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887307222929244161, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887299742388060161, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-07-18 13:15:18', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887299742388060161, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jonas Filho', 'fjfcf', 'fjfcf');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jonas Filho';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887294517640134657, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 12:54:32', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887294517640134657, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Sidney Assuncao', 'SidneyAssuncao4');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Sidney Assuncao';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887294019243520000, 'RT @Tyson_Costa: Peguei um uber gostozzo pra caralho, dei 5 estrelas e comentei...kkk #uber #boy #gostoso #sexy #pago #quero https://t.co/z…', '2017-07-18 12:52:33', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887294019243520000, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('boy');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gostoso');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sexy');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pago');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('quero');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tyson Costa', 'Tyson_Costa', 'Tyson_Costa');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tyson Costa';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887293668671008768, 'Peguei um uber gostozzo pra caralho, dei 5 estrelas e comentei...kkk #uber #boy #gostoso #sexy #pago #quero https://t.co/z5VEz3IVUt', '2017-07-18 12:51:10', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887293668671008768, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('boy');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gostoso');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sexy');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pago');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('quero');")
dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.06071', '-47.2450492', 'indaiatuba');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'indaiatuba' and latitude = '-23.06071'and longitude = '-47.2450492';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887293668671008768, " + str(id_lugar) + ");")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vanessa Meira', 'vanessarmeira', 'vanessarmeira');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vanessa Meira';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887293130529284096, 'E entrar no carro apressada, dando boa tarde e só se tocar que não é o uber qdo olhar pra cara assustada do motorista? #Uber', '2017-07-18 12:49:02', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887293130529284096, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Giulia DAngelo', 'giuliadangello', 'giuliadangello');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Giulia DAngelo';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887281412822454272, 'Sobre minha primeira experiência com @cabifybrasil : Adeus @Uber_Brasil 💁🏻 #Cabify #Uber #Vádecabify #PisamenosCabify', '2017-07-18 12:02:28', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887281412822454272, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('vádecabify');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pisamenoscabify');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Emmanuel Denaui', 'emmadenaui', 'emmadenaui');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Emmanuel Denaui';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887280358122827777, 'Bom dia p/ vc que, igual a mim, pegou um #Uber sem maçanetas internas.  A explicação? Pro passageiro não fugir sem pagar. #bizarro #issoéBR', '2017-07-18 11:58:16', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887280358122827777, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('bizarro');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('issoébr');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Doritaum', 'SRdoritao', 'SRdoritao');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Doritaum';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887277138931535872, 'RT @DoritaoTV: Use meu cupom de desconto da uber (15 REAIS) s0h034 #UBER', '2017-07-18 11:45:29', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887277138931535872, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887277057675333634, 'Use meu cupom de desconto da uber (15 REAIS) s0h034 #UBER', '2017-07-18 11:45:10', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887277057675333634, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887276239437926400, '#DESCONTO #UBER 69r4uv5hue RT @CMS_Chagas: Boa noite para os que ficam. #BetaQuerLab  #TimBeta', '2017-07-18 11:41:54', '3', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887276239437926400, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rodrigo Gomes', 'rgomesbr', 'rgomesbr');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rodrigo Gomes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887275843088732160, 'Meu cupom 'uberrgomes' te dá R$ 20 de desconto em suas primeiras viagens (10 cada) com @Uber_Brasil @Uber #uber #desconto #cupom #promocao', '2017-07-18 11:40:20', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887275843088732160, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promocao');")
dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.815924', '-46.567276', 'são bernardo do campo');")
id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'são bernardo do campo' and latitude = '-23.815924'and longitude = '-46.567276';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887275843088732160, " + str(id_lugar) + ");")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ruiva', 'porra_feh', 'porra_feh');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ruiva';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887260997760757760, 'CÓDIGO DE DESCONTO #UBER qg833cvpue aproveitemm', '2017-07-18 10:41:21', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887260997760757760, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('daniel monteiro rosa', 'danielmrosa', 'danielmrosa');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'daniel monteiro rosa';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887253255079817220, '@eduardoamorimse Que tal pensar em diminuir a burocracia do táxi? Também não foi JUSTO para os fabricantes de VELA… https://t.co/POvHTDuY5Y', '2017-07-18 10:10:35', '1', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887253255079817220, 1);")
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887236014233853953, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/vhj5qt4MDS', '2017-07-18 09:02:04', '2', " + str(id_usuario) + ");")
dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887236014233853953, 1);")
dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")

#---------------------------------------------------

#99POP

dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Henrique Brazão', 'minerobrazao', 'minerobrazao');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Henrique Brazão';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887859232527310848, '- Haddad fez sim. Regularizou o Uber e o 99Pop pra vc trabalhar. - Ah, mas prejudicou os taxistas, né?  Aí eu desisti.', '2017-07-20 02:18:31', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887859232527310848, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Henrique Brazão', 'minerobrazao', 'minerobrazao');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Henrique Brazão';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887858236233220100, 'Entro no 99Pop (não uso Uber) - Opa! Vai pro CEU? - Vou. Ali no Paz. - Trabalho. - Legal. - mas tão construindo CEU? Parou, né?', '2017-07-20 02:14:33', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887858236233220100, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Martinstutors.com', 'martinstutors');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Martinstutors.com';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887793221962653696, 'Como conseguir códigos de descontos no Cabify – 99POP – Uber Grátis https://t.co/Pi8dTCwCPt https://t.co/oUdJNK1DxH', '2017-07-19 21:56:13', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887793221962653696, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('andrezza detona', 'andrezzadovalle', 'andrezzadovalle');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'andrezza detona';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887725693433524224, 'aí você pede um 99pop e vem uma Santa Fe kkkk vamo que vamo ?????????', '2017-07-19 17:27:53', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887725693433524224, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cristovão Lima', 'cristovaolimaa', 'cristovaolimaa');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cristovão Lima';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887691893454319616, 'Gostei de um vídeo @YouTube https://t.co/fQBvJDIy3T conseguir códigos de descontos no Uber, Cabify e 99POP', '2017-07-19 15:13:34', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887691893454319616, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ygor Stegen', 'YgorNeriSantos', 'YgorNeriSantos');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ygor Stegen';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887644343561052160, 'Gostei de um vídeo @YouTube https://t.co/sxw3BRQO3T conseguir códigos de descontos no Uber, Cabify e 99POP', '2017-07-19 12:04:37', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887644343561052160, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('catóaba', 'Ricksfranca', 'Ricksfranca');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'catóaba';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887453049765154816, '99pop tb tem desconto de 20$ na primeira viagem?', '2017-07-18 23:24:29', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887453049765154816, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Evelyn Gibson', 'Evelyn40239623');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Evelyn Gibson';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887419210552311808, 'RT @EvaldodaSilva16: Boa tarde Fiz o cadastro no 99pop já vai vaze aniversário e ainda estou pendente   disse que a doc está OK Só aguardan…', '2017-07-18 21:10:01', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887419210552311808, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('?? Creio que não ??', 'FranklyMyDearLi', 'FranklyMyDearLi');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '?? Creio que não ??';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887308089443188736, 'Moço do 99POP obrigada por me convencer a levar uma bala juquinha pra comer depois! Adoçou a minha manhã! ??', '2017-07-18 13:48:28', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887308089443188736, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('M?NU', 'manufordinner', 'manufordinner');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'M?NU';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887119795556102148, '99Pop é melhor do que Uber. Repassem.', '2017-07-18 01:20:15', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887119795556102148, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('natlaia', 'natsscosta', 'natsscosta');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'natlaia';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887103343809753088, 'RT @anaguadalupe: só de pensar na música de ed sheeran me teletransporto para um 99POP com cheiro de cachorro molhado em pleno verão da far…', '2017-07-18 00:14:53', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887103343809753088, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ana guadaloopy', 'anaguadalupe', 'anaguadalupe');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ana guadaloopy';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887066484488515587, 'só de pensar na música de ed sheeran me teletransporto para um 99POP com cheiro de cachorro molhado em pleno verão da faria lima engarrafada', '2017-07-17 21:48:25', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887066484488515587, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jiffy', 'Jiffy20850280');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jiffy';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886847362638913536, 'Quer ganhar R$  15  de desconto no 99POP? https://t.co/fjOhKO0fkz https://t.co/1PfWsrc39t', '2017-07-17 07:17:42', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886847362638913536, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Renan Antunes', 'AntunuesRenan');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renan Antunes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886765083606515712, 'Já peguei motorista lerdo/ruim nesses aplicativos, mas de hoje do 99pop foi o pior da história. Lerdo pra caramba e ñ parava de falar!', '2017-07-17 01:50:45', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886765083606515712, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Bernardo Magalhães', 'belobato', 'belobato');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Bernardo Magalhães';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886604495291068416, '@MeliuzOficial boa tarde! Realizei 2 corridas de 99Pop na última sexta e não obtive cashback. Podem me ajudar a entender o que aconteceu?', '2017-07-16 15:12:38', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886604495291068416, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Anna Carolina', 'carolprds', 'carolprds');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Anna Carolina';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886532071027609600, 'Obrigada 99pop por disponibilizar o número de seus motoristas rerere', '2017-07-16 10:24:51', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886532071027609600, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Curso Sensualidade', 'isisahava', 'isisahava');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Curso Sensualidade';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886456763792445440, 'O 99pop da 99taxi tá mil vezes melhor do que o uber. Agora numa corrida do bairro Saúde para a Lapa paguei apenas... https://t.co/t2q7F4oVDJ', '2017-07-16 05:25:36', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886456763792445440, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Raul Nicacio', 'RaulNicacio', 'RaulNicacio');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Raul Nicacio';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886022509165989888, 'Entro no 99pop e já coloco na @maniadobrasil', '2017-07-15 00:40:02', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886022509165989888, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victor Greif', 'victorgreif', 'victorgreif');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victor Greif';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886017400046571520, 'Ganhei 20% de desconto na 99 https://t.co/Xuo5LTuMUY', '2017-07-15 00:19:44', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886017400046571520, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('mr 305 dale', 'darthvanner', 'darthvanner');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'mr 305 dale';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(886001010371682305, '@alephunk se tu ainda tiver em sp abandona o uber e usa o 99pop', '2017-07-14 23:14:36', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(886001010371682305, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('?? Alda Rocha', 'mjcoffeeholick', 'mjcoffeeholick');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '?? Alda Rocha';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885893604551655424, 'Hoje eu peguei AQUELE táxi! Aquele que vc se lembra pq usa Uber/99pop/cabify', '2017-07-14 16:07:49', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885893604551655424, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('???', 'liwenhua_im');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '???';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885840914941227009, 'Você ganhou um desconto do 99POP! https://t.co/eBYFAMHGpt https://t.co/GZ2ab2i0q5', '2017-07-14 12:38:26', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885840914941227009, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('???', 'liwenhua_im');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '???';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885840914219810816, 'Você ganhou um desconto do 99POP! https://t.co/eBYFAMHGpt https://t.co/FOXQipU3qz', '2017-07-14 12:38:26', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885840914219810816, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Thiago Araújo', 'todearaujo', 'todearaujo');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Thiago Araújo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885828032774144000, 'Ganhei 20% de desconto na 99 https://t.co/MIxpb2R5bX', '2017-07-14 11:47:15', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885828032774144000, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('lyão do proerd', 'regionalseis', 'regionalseis');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'lyão do proerd';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885700729163395072, '@cacaverdolin eu fico sempre comparando entre uber e 99pop. tem mais barato que esses 2? :O', '2017-07-14 03:21:24', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885700729163395072, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('O Motorista', 'OMotorista1', 'OMotorista1');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'O Motorista';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885272574212657152, '99 POP Chamas e Dicas - Final Veja como é uma chamada pela 99 pop #OMotorista #99pop #99 https://t.co/ZJufCEKwXJ', '2017-07-12 23:00:03', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885272574212657152, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('omotorista');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('99pop', '3');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Snap:ernando.galdino', 'ErnandoGaldino', 'ErnandoGaldino');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Snap:ernando.galdino';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885096024070553600, 'https://t.co/6aqAMCBvB7 viagem grátis na 99pop https://t.co/OxMBsdrbVA', '2017-07-12 11:18:31', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885096024070553600, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Snap:ernando.galdino', 'ErnandoGaldino', 'ErnandoGaldino');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Snap:ernando.galdino';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885095919192084481, 'https://t.co/6aqAMCBvB7 viagem grátis na 99pop', '2017-07-12 11:18:06', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885095919192084481, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jiffy', 'Jiffy20850280');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jiffy';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885087326984175620, 'Quer ganhar R$  15  de desconto no 99POP? https://t.co/Q40wEYAZUJ https://t.co/n5ZQietvJr', '2017-07-12 10:43:57', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885087326984175620, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jiffy', 'Jiffy20850280');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jiffy';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885035723044401156, 'Quer ganhar R$  15  de desconto no 99POP? https://t.co/BBEPOzrsIp https://t.co/itgRJk0kNp', '2017-07-12 07:18:54', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885035723044401156, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jiffy', 'Jiffy20850280');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jiffy';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885035481926389761, 'Quer ganhar R$  15  de desconto no 99POP? https://t.co/BBEPOzrsIp https://t.co/zUw0Pgrd9H', '2017-07-12 07:17:56', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885035481926389761, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('lyão do proerd', 'regionalseis', 'regionalseis');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'lyão do proerd';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(885001534827835393, '@kaleydioscope amiga fui embora daí em 2010 mas uber é a melhor coisa &lt;3 aí nao tem 99pop? é tipo o uber da 99taxis, bem barato', '2017-07-12 05:03:03', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(885001534827835393, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('leticia.', 'benalet_', 'benalet_');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'leticia.';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(884989324277764097, 'que nervousor quando entro em taxi uber 99pop cabify que prende a porcaria do cinto por detrás do banco', '2017-07-12 04:14:31', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(884989324277764097, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rita Lima', 'ritalimak', 'ritalimak');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rita Lima';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(884837136847040512, 'Ganhei esta medalhinha de São Bento, de um motorista da #99pop, qdo estava descendo do carro!… https://t.co/qTLXYA1Q9F', '2017-07-11 18:09:47', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(884837136847040512, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('99pop', '3');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Lihuiqing', 'Lihuiqing1');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lihuiqing';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(884666445715578881, 'Você ganhou um desconto do 99POP! https://t.co/4DGuj8Sl5f https://t.co/5HziZ0S50r', '2017-07-11 06:51:31', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(884666445715578881, 3);")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Sonia Grolla', 'Soniagrolla');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Sonia Grolla';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(884597743490084865, 'RT @voude99: E esse frio logo no início da semana? Mais #UmOtimoMotivoPara você pedir um 99POP. :) https://t.co/sw0gXHkTmU', '2017-07-11 02:18:31', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(884597743490084865, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('umotimomotivopara');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('clecio lucio', 'cleciolucio', 'cleciolucio');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'clecio lucio';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(884570840595128320, 'Gostei de um vídeo @YouTube https://t.co/gy3mG8UaEZ alugado para trabalhar com Uber, Cabify ou 99pop, vale a pena?', '2017-07-11 00:31:37', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(884570840595128320, 3);")
except:
    print('Erro')


#------------------------------

#cabify

