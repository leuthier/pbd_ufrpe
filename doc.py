import persistencia.DataBase as dao
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Yuri Alves', 'yurialvesgoiano', 'yurialvesgoiano');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Yuri Alves';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887822641662488576, '#uber #uberx #ubernata borá borá', '2017-07-19 23:53:07', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887822641662488576, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberx', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubernata', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('👽 bea', 'beamuaah', 'beamuaah');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '👽 bea';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887810081487818752, 'Meu código  do UBER DESCONTO DE 20 REIS! !!!  Código : tcwnc994ue #Uber #código uber #desconto', '2017-07-19 23:03:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887810081487818752, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887806677390635008, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @Thiagodabaia: #timbeta - A alegria é contagiante. Passe adiante.', '2017-07-19 22:49:41', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887806677390635008, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Hélder G (Tim Beta)', 'helder2011', 'helder2011');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Hélder G (Tim Beta)';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887804121771900928, 'Desconto de R$10 em cada uma de suas primeiras 2 viagens com a Uber. Cadastre-se clicando no link https://t.co/7YdksZR8GY #TimBeta #Uber', '2017-07-19 22:39:31', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887804121771900928, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Marcelo D. Ferreira', '_MDFerreira', '_MDFerreira');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Marcelo D. Ferreira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887803124781633537, '@marchezan_ Ilusão #Uber , hoje são duas  categorias passando fome, como estes coitados vão sustentar suas famílias? cc @ozirismg , @bandrs', '2017-07-19 22:35:34', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887803124781633537, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Lorhayne Costa', 'braz_lorhayne');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lorhayne Costa';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887802326504886272, 'RT @costa_kevelin: @braz_lorhayne @_Twittei_ 😂😂😂 ih eu aqui rezando por esse dia 👐 #Uber 😉😏', '2017-07-19 22:32:23', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887802326504886272, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ramon Macedo', 'ramonmacedois', 'ramonmacedois');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ramon Macedo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887800474191224832, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @lidiany_leal: Bom dia migos betas 😴  #missaobetalab  #TimBeta', '2017-07-19 22:25:02', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887800474191224832, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('missaobetalab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Kevelin Costa', 'costa_kevelin', 'costa_kevelin');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Kevelin Costa';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887799570721329152, '@braz_lorhayne @_Twittei_ 😂😂😂 ih eu aqui rezando por esse dia 👐 #Uber 😉😏', '2017-07-19 22:21:26', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887799570721329152, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-22.814792', '-43.410273', 'nilópolis');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'nilópolis' and latitude = '-22.814792'and longitude = '-43.410273';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet_local(id_tweet, id_local) values(887799570721329152, " + str(id_lugar) + ");")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Uber da Depressão', 'uberdepressivo', 'uberdepressivo');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Uber da Depressão';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887798205613821952, 'Já viuuu😂😂😂😂##Uber #Uberdepressivo #Uberlover #Uberx https://t.co/GJDcnlJhSj', '2017-07-19 22:16:01', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887798205613821952, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberdepressivo', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberlover', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberx', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MarceloTV', 'MarceloTV', 'MarceloTV');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MarceloTV';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887797103283646464, '@UberEATS_br #uber dá $50 te chama de vip por usar muito e depois cobra a mais por algo q te deu oi?!  #ubereats te foides çei', '2017-07-19 22:11:38', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887797103283646464, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Leandro Alves', 'leandroesportes', 'leandroesportes');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Leandro Alves';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887791471377743872, '#Uber dando um monte de B.O Daqui a pouco ninguém mais acredita nesse serviço. ..', '2017-07-19 21:49:15', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887791471377743872, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887790451440451585, 'Use meu cupom de desconto da uber (15 REAIS) 6duun #UBER', '2017-07-19 21:45:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887790451440451585, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887779598053900288, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/MYfx4kve2v', '2017-07-19 21:02:04', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779598053900288, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887779591657594888, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/kOY7djekmY', '2017-07-19 21:02:03', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779591657594888, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vitória Silva', 'masoqVih', 'masoqVih');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vitória Silva';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887777548008075264, 'Quer andar de graça no Uber em Manaus?  Utilize o seguinte código: EmpregosEmManaus https://t.co/mTz43ayAmt #uber… https://t.co/jGtzWGyTSg', '2017-07-19 20:53:56', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887777548008075264, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887775352793247745, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-19 20:45:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887775352793247745, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887774517124149248, '#DESCONTO #UBER 69r4uv5hue RT @RahulTayde9: Não foi dessa vez mas na próxima dará certo !! 😎 #TimBeta #BetaAjudaBeta https://t.co/Y09iP7O3hX', '2017-07-19 20:41:53', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887774517124149248, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887771557052940289, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 20:30:07', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887771557052940289, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jose', 'Jose25873018');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jose';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887765746444644353, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-19 20:07:02', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887765746444644353, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Daniel Alves', 'alves929_alves');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Daniel Alves';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887764581761810433, 'Aproveite a promoção para você implantar o aplicativo de táxi estilo uber https://t.co/F9lt7T8jZr #uber #ubereats #ifood #ifoodsalva #tbt', '2017-07-19 20:02:24', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887764581761810433, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifood');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifoodsalva');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tbt');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Salomão   🙈', 'TremJaofe', 'TremJaofe');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Salomão   🙈';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887755279173079041, 'só esse cineminha e um lanche do mac haha rs 😍❤️ #vamos  #de #Uber', '2017-07-19 19:25:26', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887755279173079041, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('vamos');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('de');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Van', 'VanilseUeda', 'VanilseUeda');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Van';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887740861865504768, 'Meu app do #Uber nunca mostra placa do carro.    Mas que caralha 😔', '2017-07-19 18:28:09', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887740861865504768, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Campo Grande News', 'cgrnews', 'cgrnews');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Campo Grande News';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887733579899449344, 'Decreto prevê cassação imediata do alvará de licenciamento, interdição parcial ou total das empresas. #CGNews #Uber https://t.co/V741UsBIYX', '2017-07-19 17:59:13', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887733579899449344, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cgnews');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Uber da Depressão', 'uberdepressivo', 'uberdepressivo');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Uber da Depressão';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887725161402839046, 'Novo serviço...Ubermula...#Uber #Uberblack #Uberislife #Uberdepressivo #Uberlover #Uberx https://t.co/4WjhfAet1h', '2017-07-19 17:25:46', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887725161402839046, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberblack', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberislife', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberdepressivo', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberlover', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberx', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vic on Ice trash', 'Vic_Walker', 'Vic_Walker');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vic on Ice trash';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887722504244125696, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/nevaKiBg03', '2017-07-19 17:15:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887722504244125696, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('heverton carvalho', 'hetocarvalho1', 'hetocarvalho1');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'heverton carvalho';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699695262474241, 'voucher pra trem fantasma #Uber', '2017-07-19 15:44:34', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699695262474241, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699029211131904, '#DESCONTO #UBER 69r4uv5hue RT @titapeace: Cuidado com o destino, ele brinca com as pessoas... #TimBeta #timbetalab', '2017-07-19 15:41:55', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699029211131904, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetalab');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'havanalab');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887690847638216705, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-19 15:09:25', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887690847638216705, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688997299945472, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/2znvKCpMEj', '2017-07-19 15:02:04', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688997299945472, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
try:
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688991436398595, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg', '2017-07-19 15:02:02', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688991436398595, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
