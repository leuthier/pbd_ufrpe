import persistencia.DataBase as dao
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MarceloTV', 'MarceloTV', 'MarceloTV');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MarceloTV';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887786640063832064, '#uber dá $50 te chama de vip por usar muito e depois cobra a mais por algo q te deu oi?!  #ubereats te foides?!@ubeareats_br', '2017-07-19 21:30:03', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887786640063832064, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887779598053900288, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/MYfx4kve2v', '2017-07-19 21:02:04', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779598053900288, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887779591657594888, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/kOY7djekmY', '2017-07-19 21:02:03', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887779591657594888, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vitória Silva', 'masoqVih', 'masoqVih');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vitória Silva';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887777548008075264, 'Quer andar de graça no Uber em Manaus?  Utilize o seguinte código: EmpregosEmManaus https://t.co/mTz43ayAmt #uber… https://t.co/jGtzWGyTSg', '2017-07-19 20:53:56', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887777548008075264, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887775352793247745, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-19 20:45:12', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887775352793247745, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887774517124149248, '#DESCONTO #UBER 69r4uv5hue RT @RahulTayde9: Não foi dessa vez mas na próxima dará certo !! 😎 #TimBeta #BetaAjudaBeta https://t.co/Y09iP7O3hX', '2017-07-19 20:41:53', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887774517124149248, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887771557052940289, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 20:30:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887771557052940289, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Jose', 'Jose25873018');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jose';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887765746444644353, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-19 20:07:02', '1', "  + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887765746444644353, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
except:
    print('Erro')


try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Daniel Alves', 'alves929_alves');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Daniel Alves';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887764581761810433, 'Aproveite a promoção para você implantar o aplicativo de táxi estilo uber https://t.co/F9lt7T8jZr #uber #ubereats #ifood #ifoodsalva #tbt', '2017-07-19 20:02:24', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887764581761810433, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifood');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ifoodsalva');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tbt');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Van', 'VanilseUeda', 'VanilseUeda');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Van';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887740861865504768, 'Meu app do #Uber nunca mostra placa do carro.    Mas que caralha 😔', '2017-07-19 18:28:09', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887740861865504768, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Campo Grande News', 'cgrnews', 'cgrnews');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Campo Grande News';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887733579899449344, 'Decreto prevê cassação imediata do alvará de licenciamento, interdição parcial ou total das empresas. #CGNews #Uber https://t.co/V741UsBIYX', '2017-07-19 17:59:13', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887733579899449344, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cgnews');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vic on Ice trash', 'Vic_Walker', 'Vic_Walker');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vic on Ice trash';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887722504244125696, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/nevaKiBg03', '2017-07-19 17:15:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887722504244125696, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('heverton carvalho', 'hetocarvalho1', 'hetocarvalho1');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'heverton carvalho';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699695262474241, 'voucher pra trem fantasma #Uber', '2017-07-19 15:44:34', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699695262474241, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887699029211131904, '#DESCONTO #UBER 69r4uv5hue RT @titapeace: Cuidado com o destino, ele brinca com as pessoas... #TimBeta #timbetalab', '2017-07-19 15:41:55', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887699029211131904, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetalab');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'havanalab');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887690847638216705, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-19 15:09:25', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887690847638216705, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688997299945472, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/2znvKCpMEj', '2017-07-19 15:02:04', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688997299945472, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887688991436398595, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg', '2017-07-19 15:02:02', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887688991436398595, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('André Luis Urel', 'andre_urel', 'andre_urel');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'André Luis Urel';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887687582653575173, '#Wolverine virou #Uber #Logan Putz o desemprego afetou até os super heróis', '2017-07-19 14:56:26', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887687582653575173, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('wolverine');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('logan');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887680999252873217, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 14:30:17', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887680999252873217, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carol', 'c4rou', 'c4rou');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carol';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-8.157554', '-35.019805', 'jaboatão dos guararapes');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'jaboatão dos guararapes' and latitude = '-8.157554'and longitude = '-35.019805';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario,id_lugar) values(887671491751538689, '#uber em Recife é mara! Tem até Wi-Fi :)', '2017-07-19 13:52:30', '1', " + str(id_usuario) + ", " + str(id_lugar) +");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887671491751538689, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")

except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887662128487776256, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-07-19 13:15:18', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887662128487776256, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ângelo Rodrigues', 'angeloOmusic', 'angeloOmusic');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ângelo Rodrigues';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887659711365042176, 'Vai uma boleia?  #uber #uberportugal #uberpool https://t.co/bxuTxq6Pej', '2017-07-19 13:05:41', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887659711365042176, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberportugal', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberpool', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Albertina D Dias', 'AlbertinaDDias', 'AlbertinaDDias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Albertina D Dias';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887647043283329024, 'O que podemos aprender da #Uber sobre transformação #digital? #FutureofWork #MercerDigital https://t.co/190rowN1TF https://t.co/Ri9vqdOuGH', '2017-07-19 12:15:21', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887647043283329024, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('digital');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('futureofwork');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('mercerdigital');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887609246199816193, 'Use meu cupom de desconto da uber (15 REAIS) 6duun #UBER', '2017-07-19 09:45:09', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887609246199816193, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887598404918005760, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/KWUbpf4uxL', '2017-07-19 09:02:05', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887598404918005760, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887598399696056320, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/vv8C7Htqoa', '2017-07-19 09:02:03', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887598399696056320, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887507805913174016, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/gSYATvLg4N', '2017-07-19 03:02:04', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887507805913174016, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887507799600750592, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/GkgXOTHDCX', '2017-07-19 03:02:03', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887507799600750592, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887499887063035904, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-19 02:30:36', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887499887063035904, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Bob Cuspe', 'rgommez', 'rgommez');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Bob Cuspe';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887494555649667073, 'RT @portaluai: #Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5…', '2017-07-19 02:09:25', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887494555649667073, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('TEXTOS NO FIXADO', 'ThomHipolito', 'ThomHipolito');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'TEXTOS NO FIXADO';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887479159831883776, 'Uma garota pegou um #uber vindo na nove de junho comigo, não peguei o contato dela, talvez seríamos grandes amigos', '2017-07-19 01:08:14', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887479159831883776, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.08302', '-43.795449', 'itaguaí');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'itaguaí' and latitude = '-23.08302'and longitude = '-43.795449';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887474501163917314, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Eu realmente me importo com você #timbeta', '2017-07-19 00:49:44', '3', " + str(id_usuario) +", " + str(id_lugar) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887474501163917314, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.08302', '-43.795449', 'itaguaí');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('@Renata', 'Re_mcd', 'Re_mcd');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '@Renata';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887469258715934724, 'Em plena porta de metrô e não tem 1 #uber disponível!!! Que horror! https://t.co/frZ6KcYLwP', '2017-07-19 00:28:54', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887469258715934724, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Anderson_ce', 'AndersonLima_ce', 'AndersonLima_ce');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Anderson_ce';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887463183358840832, 'Estou enviando um desconto de R$6 em cada uma de suas primeiras 2 viagens com a Uber. Para aceitar, use o código zn35nw  #Uber #UberCode', '2017-07-19 00:04:45', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887463183358840832, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercode', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lucas', 'UnCaraQualquer', 'UnCaraQualquer');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lucas';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887436724384800768, '#Uber Black é muito bom', '2017-07-18 22:19:37', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887436724384800768, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jazz', 'Jaaaaaziel', 'Jaaaaaziel');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jazz';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887433252310585346, '@sophiacabraal @Wmelomedeiros #uber não caridade kkkk já viram o preço da gasolina?', '2017-07-18 22:05:49', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887433252310585346, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rogerio08 #TimBeta', 'RogerioBeta08', 'RogerioBeta08');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rogerio08 #TimBeta';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887425109815959552, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @CMS_Chagas: Boa noite para os que ficam. #BetaQuerLab  #TimBeta', '2017-07-18 21:33:28', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887425109815959552, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887417209567543297, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/X19KFr7Le4', '2017-07-18 21:02:04', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887417209567543297, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887417203037016069, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/WfyKBWD2FN', '2017-07-18 21:02:03', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887417203037016069, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887412971848314881, 'Use meu cupom de desconto da uber (15 REAIS) 6duun #UBER', '2017-07-18 20:45:14', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887412971848314881, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887412952839708672, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-07-18 20:45:09', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887412952839708672, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'diegoocastilhoo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887409160710737920, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-07-18 20:30:05', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887409160710737920, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Pretty hate machine', 'feeh_withlasers', 'feeh_withlasers');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Pretty hate machine';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887402140704141314, 'an9vy4wmue desconto de R$20,00 no uber e 25,00 no ubereats #uber #cupomuber #ubercupom', '2017-07-18 20:02:12', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887402140704141314, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cupomuber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubercupom', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('TREVISAN', 'trevisan_marcos', 'trevisan_marcos');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'TREVISAN';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887401712952250368, '#Uber use o código promocional UBERGANHEI20UE e ganhe duas corridas com R$ 10 de desconto. #vaideUber', '2017-07-18 20:00:30', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887401712952250368, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('vaideuber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BRIAN MENDES', 'BrianMend', 'BrianMend');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BRIAN MENDES';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887400813383094273, 'Quer ganhar #DescontoUber? #uber #CodigoUber  Use o código:     watlrk', '2017-07-18 19:56:55', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887400813383094273, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('descontouber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('codigouber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Dux', 'DuxCoelho', 'DuxCoelho');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Dux';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887395079060692992, 'Chateado. Não tem #Uber em Penedo. https://t.co/SsszsJ00iW', '2017-07-18 19:34:08', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887395079060692992, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('MOVITAXI BRASIL', 'MOVITAXIBRASIL', 'MOVITAXIBRASIL');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'MOVITAXI BRASIL';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887391616599826432, '@eduardoamorimse Parabéns pela coerência, a sociedade hipócrita ainda há de entender um dia o mal que o #uber causa...', '2017-07-18 19:20:22', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887391616599826432, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Elisa Travalloni', 'Travalloni', 'Travalloni');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Elisa Travalloni';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887384730794065920, 'E #uber cada vez mais lambão', '2017-07-18 18:53:01', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887384730794065920, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Julien Jay', 'Julien_Jay', 'Julien_Jay');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Julien Jay';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887382627723997184, '@romainturkowiak Des fadas je te jure ! #Uber', '2017-07-18 18:44:39', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887382627723997184, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('covfefe', 'ewertonleaoK');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'covfefe';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887379842827792389, '@maltzsama coloca na ponta do lapis se n é melhor #uber', '2017-07-18 18:33:35', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887379842827792389, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Renato Marinho', 'renato_marinho');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renato Marinho';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887379367231455233, 'Contas #Uber em alta no mercado ilegal. Phishing e reuso de senhas são as principais ameaças. Não reuse senhas. Stay tuned. #morphuslabs', '2017-07-18 18:31:42', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887379367231455233, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('morphuslabs');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vic on Ice trash', 'Vic_Walker', 'Vic_Walker');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vic on Ice trash';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887360105234214912, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/hAxQ8xpSAm', '2017-07-18 17:15:10', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887360105234214912, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Paulo Anderson', '_pauloanderson', '_pauloanderson');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Paulo Anderson';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887330438360031232, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 15:17:16', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887330438360031232, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'havanalab');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887328328709013504, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-07-18 15:08:53', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887328328709013504, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887326856931889152, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/IrbatKl7jI', '2017-07-18 15:03:03', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887326856931889152, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Diário de Goiás', 'diariodegoias', 'diariodegoias');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Diário de Goiás';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887326636013760516, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/TuPW7ESTFg https://t.co/rmPrn95SWd', '2017-07-18 15:02:10', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887326636013760516, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Eevee son', 'iwyson', 'iwyson');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Eevee son';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-3.88818', '-38.638212', 'maracanaú');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'maracanaú' and latitude = '-3.88818'and longitude = '-38.638212';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887325676143087616, 'Só eu que acho a #uber extremamente organizada? Nunca tive um resquício de problema.', '2017-07-18 14:58:21', '1', " + str(id_usuario) + ", " + str(id_lugar) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887325676143087616, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ronilson Geraldo', 'ronilsonsalg', 'ronilsonsalg');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ronilson Geraldo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887311531888791553, 'RT @portaluai: #Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5…', '2017-07-18 14:02:09', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887311531888791553, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Portal UAI', 'portaluai', 'portaluai');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Portal UAI';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887311012008939520, '#Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/uzw1b2WXZG https://t.co/GK2j5qCzzg', '2017-07-18 14:00:05', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887311012008939520, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Gugagustavo', 'Gugagustavo13');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Gugagustavo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887310554402099200, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 13:58:16', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887310554402099200, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Estado de Minas', 'em_com', 'em_com');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Estado de Minas';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887307222929244161, '#Uber consegue mais uma vitória em ação de vínculo empregatício em Belo Horizonte https://t.co/2KgjPneUNC https://t.co/8OoqFH4n8C', '2017-07-18 13:45:01', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887307222929244161, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'aventureiros');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887299742388060161, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-07-18 13:15:18', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887299742388060161, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jonas Filho', 'fjfcf', 'fjfcf');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jonas Filho';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887294517640134657, 'RT @OficialAvioes: #Uber fazendo a #NaçãoAviãozeira de #Sergipe quebrar tudo! Mostra pro teu amigo que AINDA não se rendeu ao suíngue do @x…', '2017-07-18 12:54:32', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887294517640134657, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('naçãoaviãozeira');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sergipe');")
except:
    print('Erro')

try:
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
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tyson Costa', 'Tyson_Costa', 'Tyson_Costa');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tyson Costa';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.06071', '-47.2450492', 'indaiatuba');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'indaiatuba' and latitude = '-23.06071'and longitude = '-47.2450492';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(887293668671008768, 'Peguei um uber gostozzo pra caralho, dei 5 estrelas e comentei...kkk #uber #boy #gostoso #sexy #pago #quero https://t.co/z5VEz3IVUt', '2017-07-18 12:51:10', '1', " + str(id_usuario) +", " + str(id_lugar)+ ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887293668671008768, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('boy');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gostoso');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sexy');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pago');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('quero');")


except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Vanessa Meira', 'vanessarmeira', 'vanessarmeira');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Vanessa Meira';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887293130529284096, 'E entrar no carro apressada, dando boa tarde e só se tocar que não é o uber qdo olhar pra cara assustada do motorista? #Uber', '2017-07-18 12:49:02', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887293130529284096, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Giulia DAngelo', 'giuliadangello', 'giuliadangello');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Giulia DAngelo';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887281412822454272, 'Sobre minha primeira experiência com @cabifybrasil : Adeus @Uber_Brasil 💁🏻 #Cabify #Uber #Vádecabify #PisamenosCabify', '2017-07-18 12:02:28', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887281412822454272, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('vádecabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pisamenoscabify');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Emmanuel Denaui', 'emmadenaui', 'emmadenaui');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Emmanuel Denaui';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887280358122827777, 'Bom dia p/ vc que, igual a mim, pegou um #Uber sem maçanetas internas.  A explicação? Pro passageiro não fugir sem pagar. #bizarro #issoéBR', '2017-07-18 11:58:16', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887280358122827777, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('bizarro');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('issoébr');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Doritaum', 'SRdoritao', 'SRdoritao');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Doritaum';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887277138931535872, 'RT @DoritaoTV: Use meu cupom de desconto da uber (15 REAIS) s0h034 #UBER', '2017-07-18 11:45:29', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887277138931535872, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Arroba guardado', 'DoritaoTV', 'DoritaoTV');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Arroba guardado';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887277057675333634, 'Use meu cupom de desconto da uber (15 REAIS) s0h034 #UBER', '2017-07-18 11:45:10', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887277057675333634, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'betabrazzz');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887276239437926400, '#DESCONTO #UBER 69r4uv5hue RT @CMS_Chagas: Boa noite para os que ficam. #BetaQuerLab  #TimBeta', '2017-07-18 11:41:54', '3', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887276239437926400, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rodrigo Gomes', 'rgomesbr', 'rgomesbr');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rodrigo Gomes';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.815924', '-46.567276', 'são bernardo do campo');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'são bernardo do campo' and latitude = '-23.815924'and longitude = '-46.567276';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887275843088732160, 'Meu cupom 'uberrgomes' te dá R$ 20 de desconto em suas primeiras viagens (10 cada) com @Uber_Brasil @Uber #uber #desconto #cupom #promocao', '2017-07-18 11:40:20', '1', " + str(id_usuario) +", " + str(id_lugar)+ ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887275843088732160, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promocao');")


except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ruiva', 'porra_feh', 'porra_feh');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ruiva';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887260997760757760, 'CÓDIGO DE DESCONTO #UBER qg833cvpue aproveitemm', '2017-07-18 10:41:21', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887260997760757760, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('daniel monteiro rosa', 'danielmrosa', 'danielmrosa');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'daniel monteiro rosa';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887253255079817220, '@eduardoamorimse Que tal pensar em diminuir a burocracia do táxi? Também não foi JUSTO para os fabricantes de VELA… https://t.co/POvHTDuY5Y', '2017-07-18 10:10:35', '1', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887253255079817220, 1);")
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Carlos Bueno Moraes', 'carlosbuenoDG', 'carlosbuenoDG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Carlos Bueno Moraes';")[0][0]
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario) values(887236014233853953, 'Iris afirma que regulamentação do @Uber em Goiânia será enviada à Câmara #Uber https://t.co/wxbSJmekZ3 https://t.co/vhj5qt4MDS', '2017-07-18 09:02:04', '2', " + str(id_usuario) + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(887236014233853953, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')

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

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('armindoferreira', 'armindoferreira', 'Vale do Paraíba-SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'armindoferreira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(893060417681010688, 'Quanto eu gastei de casa até a Rodoviária usando 99Pop @voude99 ?  😱😱😱😱 https://t.co/PhF31VhI0X', '2017-08-03 10:46:10', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(893060417681010688, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Maiara Nogueira', 'MaiaraNogueira_', 'São José dos Campos - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Maiara Nogueira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(893048729493794817, 'Você ganhou um desconto do 99POP! Ma oe, muito bom dia 😘 https://t.co/9V2UDFr0vF https://t.co/QVxzDR8IRa', '2017-08-03 09:59:43', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(893048729493794817, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Olenna Tyrell', 'VENISUC0', 'SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Olenna Tyrell';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892966786358022144, '@victorvercillas @cabifybrasil Usa o 99pop q é sucesso, to viciado', '2017-08-03 04:34:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892966786358022144, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Dani Marzola', 'danimarzola23');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Dani Marzola';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892916933745664000, 'Andei tipo Uber, só que o 99pop, caramba, que medão!!!  Descobri que sou bicho do mato!!! :O', '2017-08-03 01:16:01', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892916933745664000, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('sapata mortifera', 'camuflavia', 'presidenta da sapaçonaria');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'sapata mortifera';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892873190745272320, '@voude99 tanto pedindo 99pop qnt 99táxi tive esse problema. todos estavam indo na mesma direção. reiniciei o aplica… https://t.co/tdGkG5l88p', '2017-08-02 22:22:12', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892873190745272320, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Maxlimpezaestofados', 'maxlimpezadeest', 'Vicente de Carvalho, Rio de Ja');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Maxlimpezaestofados';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892847404784902144, 'Algum amigo que roda no 99pop? que possa dizer se vale a pena.', '2017-08-02 20:39:44', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892847404784902144, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('OldMonkey', '_mrc10', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'OldMonkey';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892837437088649216, 'Ontem eu usei 3 99Pop para ir no seguintes trajetos! Augusta&gt;Frei Caneca Frei Caneca&gt;Augusta Estação Capão&gt; Casa Com $21 EU SOU A UNIVERSAL', '2017-08-02 20:00:07', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892837437088649216, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Gabriel Dias', 'gabBFR', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Gabriel Dias';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892447363926720513, 'Agora o motorista do 99Pop pode te mandar áudio para, por exemplo, falar que já está chegando.… https://t.co/6cme3ryjgP', '2017-08-01 18:10:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892447363926720513, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Tãmbler bói', 'ImTooNormal');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tãmbler bói';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892383951825887232, 'Bem, mas não vou ficar dando muita moral. O Uber começou bem também, pra depois decair. O 99POP tem pouco mais de 1 ano.', '2017-08-01 13:58:08', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892383951825887232, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Tãmbler bói', 'ImTooNormal');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tãmbler bói';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892383615442616320, 'No 99POP só peguei motoristas gentis, educados e aparentemente de grande caráter.', '2017-08-01 13:56:48', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892383615442616320, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Tãmbler bói', 'ImTooNormal');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tãmbler bói';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892382869510922240, 'Por que o 99POP é melhor que o Uber?', '2017-08-01 13:53:50', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892382869510922240, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('cesarspo', 'cesarspo', 'São Paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'cesarspo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892377504962445312, 'Pesquisa furada da @voude99 dizendo q o 99pop é +barato. Eles n levam em consideração as promos e @easytaxi SEMPRE… https://t.co/COa5bj4Dbf', '2017-08-01 13:32:31', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892377504962445312, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('INVICTO', 'allan__f', 'Arena Corinthians, SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'INVICTO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892369652726288386, 'Não aguento mais esse 99POP no YouTube.', '2017-08-01 13:01:19', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892369652726288386, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Hugo Adescenco', 'hugoadescenco', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Hugo Adescenco';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892162764260745217, 'RT @voude99: 🎵 Se você não vem, eu vou botar pressão        Não vou te esperar, tô cheia de opção 🎵 - Posso ir de 99POP, 99Táxi, 99TOP... 😘…', '2017-07-31 23:19:13', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892162764260745217, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Cath fortalece', 'Cathbenicio');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cath fortalece';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892132068578209793, 'RT @voude99: 🎵 Se você não vem, eu vou botar pressão        Não vou te esperar, tô cheia de opção 🎵 - Posso ir de 99POP, 99Táxi, 99TOP... 😘…', '2017-07-31 21:17:14', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892132068578209793, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('vitin', 'vitinhofranco13');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'vitin';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892126626145763329, 'Algm tem código de desconto daql 99pop aí?', '2017-07-31 20:55:37', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892126626145763329, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tiffany', 'tiifffany', 'São Paulo, Brazil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tiffany';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892124954938007559, 'RT @voude99: 🎵 Se você não vem, eu vou botar pressão        Não vou te esperar, tô cheia de opção 🎵 - Posso ir de 99POP, 99Táxi, 99TOP... 😘…', '2017-07-31 20:48:58', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892124954938007559, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Ronaldo Nunez', 'ronaldo_nunez');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ronaldo Nunez';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892108443410206721, 'Oi! Te mandei um desconto do 99POP! https://t.co/fdU5tH7QrD', '2017-07-31 19:43:22', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892108443410206721, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('➰', 'eoqanirer');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '➰';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892056684763525120, 'RT @voude99: 🎵 Se você não vem, eu vou botar pressão        Não vou te esperar, tô cheia de opção 🎵 - Posso ir de 99POP, 99Táxi, 99TOP... 😘…', '2017-07-31 16:17:41', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892056684763525120, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('99', 'voude99', 'Onde tiver carros');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = '99';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892052516665524230, '🎵 Se você não vem, eu vou botar pressão        Não vou te esperar, tô cheia de opção 🎵 - Posso ir de 99POP, 99Táxi,… https://t.co/OJNM7oxwb4', '2017-07-31 16:01:08', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892052516665524230, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('alex bodoh', 'bodohx', 'Rio de Janeiro, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'alex bodoh';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892040806047076353, '@voude99 ganhei 20% mas não habilitou aqui nomeu app https://t.co/7canqon7JT', '2017-07-31 15:14:36', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892040806047076353, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Nina Bamberg', 'ninabamberg', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Nina Bamberg';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892026654809350145, '@umasalvadepaula amiga, uber não dá. usa promos da 99, 99pop e cabify.', '2017-07-31 14:18:22', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892026654809350145, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Ronaldo Nunez', 'ronaldo_nunez');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ronaldo Nunez';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892020797262397440, 'Quer ganhar R$  15  de desconto no 99POP? Você ganhou R$15 de desconto na sua 1ª corrida para experimentar o 99POP.… https://t.co/yOkhmfI4Br', '2017-07-31 13:55:05', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892020797262397440, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tcherere Tchê Tchê', 'SemPijama', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tcherere Tchê Tchê';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892013517066436609, 'O 99POP é tudo: Um app bonitinho, serviço de qualidade, preço supimpa e suporte de qualidade. Obrigado @voude99 já é queridinha aqui', '2017-07-31 13:26:09', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892013517066436609, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Maiara Nogueira', 'MaiaraNogueira_', 'São José dos Campos - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Maiara Nogueira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891963137896927232, 'Vim trabalhar de 99pop hoje 😌🍃#maisbaratoqueuber #99pop https://t.co/ThdSUYRhbx https://t.co/rKjE0983Eb', '2017-07-31 10:05:58', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891963137896927232, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('maisbaratoqueuber');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('99pop', '3');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('debz', 'essadebora', 'Satandré ABC SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'debz';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891864336544780289, '@__nana @voude99 outro dia uma motorista do 99pop continuou a corrida por mais 15km e eu n notei que ela não tinha… https://t.co/9FL9O8kHAk', '2017-07-31 03:33:22', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891864336544780289, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('emilia 🦋', 'susiebarbosa_', 'Kidrauhl ❤️ Ágata  ❤️ ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'emilia 🦋';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891854465145425920, 'Desconto no 99POP pra vc! https://t.co/ShyXT6yxcE https://t.co/Msa6YObp1j', '2017-07-31 02:54:09', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891854465145425920, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Caio Cesar', 'caioectofit', 'São Jose dos Campos, SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Caio Cesar';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891832062705094656, 'Atenção! Viagem de GRAÇA pelo novo app 99POP em SJC e Jacarei!!!   Concorrente do UBER!  Quer ganhar R$ 15 de... https://t.co/9imxy9wpY7', '2017-07-31 01:25:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891832062705094656, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Sharashiva', 'Brunagrj', 'SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Sharashiva';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891806511684628483, 'Mano ontem teve de tudo,festa num microônibus do 99POP,Máscara dentro de limusine', '2017-07-30 23:43:36', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891806511684628483, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Renan Moratto', 'remorato', 'São Paulo - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Renan Moratto';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891774607031664640, 'a 99 tem o serviço alternativo ao #uber e também tem #cupom no 99pop usa lá o código RENANMORATTO https://t.co/oDlJwUQES4 #desconto #99taxi', '2017-07-30 21:36:49', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891774607031664640, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('uber');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('99taxi');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cursinera', 'Luuck7', 'São José dos Campos, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cursinera';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891772003400724480, 'Esse 99pop nem achar motorista acha', '2017-07-30 21:26:28', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891772003400724480, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('hota$hell', 'jessfrncis');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'hota$hell';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891762047763042304, 'Quer ganhar R$ 15 de desconto no 99POP? Clique no link e veja como ativar seu desconto na sua 1ª corrida!  https://t.co/YJjlKbgrgQ', '2017-07-30 20:46:54', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891762047763042304, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('le', 'Lena_campoy', 'sanja');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'le';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891711357548191744, 'alguém ja usou esse 99pop?', '2017-07-30 17:25:29', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891711357548191744, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Banda Benção', 'BandaBencao', 'itapevi');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Banda Benção';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891677105255305216, 'Adicionei um vídeo a uma playlist @YouTube https://t.co/6QLv6GQ6rIádio 99POP #20', '2017-07-30 15:09:23', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891677105255305216, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('vital', 'pam_vital');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'vital';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891675943609274368, 'alguem tem codigo de desconto no 99pop ai????', '2017-07-30 15:04:46', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891675943609274368, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Herlon Feliciano', 'HerlonFeliciano', 'Rio de Janeiro, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Herlon Feliciano';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-23.08302', '-43.795449', 'itaguaí');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'itaguaí' and latitude = '-23.08302'and longitude = '-43.795449';")[0][0]
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = 'itaguaí';")[0][0]
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891657679697006592, 'Usem este código Herlon Feliciano no aplicativo da 99taxi ou 99pop e ganhe 20 reais de desconto. 😉 https://t.co/lDyFYzAWHL', '2017-07-30 13:52:11', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891657679697006592, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cria da ZL', '_luiizfelipeesb', 'São José dos Campos, São Paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cria da ZL';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891656835740073986, '@arianeluizaf 99pop é o jeito kk', '2017-07-30 13:48:50', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891656835740073986, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Raphael Renó', 'RaphaelReno', 'Sao José dos Campos - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Raphael Renó';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891616356872880128, 'Compartilhar 99POP - São José dos Campos APK https://t.co/OguvpdTYXa', '2017-07-30 11:07:59', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891616356872880128, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ge', 'clockworkoge', '012 ♒️');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ge';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891581195842199553, 'RT @mlrgarcia: qq adianta esse 99pop se nunca tem carro quando eu preciso', '2017-07-30 08:48:16', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891581195842199553, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('luíza', 'mlrgarcia');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'luíza';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891540642215714816, 'qq adianta esse 99pop se nunca tem carro quando eu preciso', '2017-07-30 06:07:07', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891540642215714816, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('sams', 'sahlada', 'sjcê ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'sams';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891464690890670081, 'essa bosta de 99pop não cadastra meu cartão vai se ferrar @voude99', '2017-07-30 01:05:19', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891464690890670081, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('John Ortolanni', 'Mccaintimes', 'São Paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'John Ortolanni';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891442127233843200, 'Gostei de um vídeo @YouTube https://t.co/ptXoI5L0LLádio 99POP #20', '2017-07-29 23:35:39', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891442127233843200, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Camisetas Flex', 'contato05334849', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camisetas Flex';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891436488197537794, 'Gostei de um vídeo @YouTube https://t.co/jrcx4WCHknádio 99POP #20', '2017-07-29 23:13:15', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891436488197537794, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('b', 'orphandale');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'b';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891396917195943936, 'baixei o 99pop pq tem mais descontos que a uber', '2017-07-29 20:36:01', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891396917195943936, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Ananias Jr', 'bananias_', 'São José dos Campos - SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ananias Jr';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891340758808133632, '99Pop me parece melhor que o Uber, mas o app é bem bugadinho', '2017-07-29 16:52:51', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891340758808133632, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lenise Medeiros', 'lenisesays', 'São José dos Campos, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lenise Medeiros';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891318633615511553, '99POP é muito legal, já baixei, cadastrei, te da 50% desconto na viagem só não tem: motoristas.', '2017-07-29 15:24:56', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891318633615511553, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Luís Guilherme', 'guilermemoraess', 'Brazil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Luís Guilherme';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891284247264153600, 'Quer ganhar R$  15  de desconto no 99POP? https://t.co/2LWS0SBVWt https://t.co/jxI76WYtBz', '2017-07-29 13:08:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891284247264153600, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('weirdo', 'fefoguima', 'perdido');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'weirdo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891281529107861505, 'A motorista da 99pop que eu to tem a voz do gru no waze hauahauahauahauaha', '2017-07-29 12:57:30', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891281529107861505, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Reinaldo Moura', 'ReinaldoMoura3', 'Rio de Janeiro, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Reinaldo Moura';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891281431506423808, 'Qual é o aplicativo #99pop  (certo) para passageiros?', '2017-07-29 12:57:07', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891281431506423808, 3);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('99pop', '3');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Coxa', 'Mateus_Megda');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Coxa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891150813325819909, 'MANO EU ODEIO O 99POP', '2017-07-29 04:18:05', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891150813325819909, 3);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Du Passos de Moraes', 'DuPassosdeMora1');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Du Passos de Moraes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892942135875555332, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @giselecato: Mais alguém com o #Pinterest zerado? 😢  #tim #TimBeta  #BetaAjudaBeta  #betasegu…', '2017-08-03 02:56:09', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892942135875555332, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pinterest');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tim');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892938561707802624, '#DESCONTO #UBER 69r4uv5hue RT @giselecato: Mais alguém com o #Pinterest zerado? 😢  #tim #TimBeta  #BetaAjudaBeta  #betaseguebeta  #BetaLab', '2017-08-03 02:41:57', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892938561707802624, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('pinterest');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tim');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaseguebeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betalab');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ISRAEL SOUZA TIMBETA', 'timbetalabfoco', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ISRAEL SOUZA TIMBETA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892933745484980224, 'RT @timbetalabfoco: Ajuda #BetaQuerLab #uber #uberhelp https://t.co/bqDJTJx8tn', '2017-08-03 02:22:49', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892933745484980224, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberhelp', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('ISRAEL SOUZA TIMBETA', 'timbetalabfoco', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'ISRAEL SOUZA TIMBETA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892931467407482880, 'Ajuda #BetaQuerLab #uber #uberhelp https://t.co/bqDJTJx8tn', '2017-08-03 02:13:46', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892931467407482880, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberhelp', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('david c', 'dwwid', 'natal | brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'david c';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892930560598970369, '@RadioLaWeb Use o código uvl67a pra ganhar R$20 de desconto #uber', '2017-08-03 02:10:10', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892930560598970369, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('G33k_Gamer', 'jon_micael', 'Brazil - SSP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'G33k_Gamer';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892928679663341568, 'Nada como ir pra casa depois de um dia produtivo... #Uber #home #tired https://t.co/k8iZsWBIpT https://t.co/BgpXQd9NbW', '2017-08-03 02:02:41', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892928679663341568, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('home');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tired');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('G33k_Gamer', 'jon_micael', 'Brazil - SSP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'G33k_Gamer';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892928662047268865, 'Nada como ir pra casa depois de um dia produtivo...   #Uber #home… https://t.co/L2UnYTAZoZ', '2017-08-03 02:02:37', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892928662047268865, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('home');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892920601790345217, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-08-03 01:30:35', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892920601790345217, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Filipe Hickmann 🌈', 'Filipe_Hickmann', 'EUA  ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Filipe Hickmann 🌈';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892919444938338304, 'o que vocês acha de ter #UBER em Mogi Guaçu ?', '2017-08-03 01:25:59', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892919444938338304, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('david c', 'dwwid', 'natal | brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'david c';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892917283915538432, '@oisarahh Use o código uvl67a pra ganhar R$20 de desconto #uber', '2017-08-03 01:17:24', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892917283915538432, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Praia do Pepê', 'Praiadopepe', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Praia do Pepê';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892915496248627201, 'Concorrente do #Uber, #Cabify promete briga acirrada. https://t.co/anlrh4obBO', '2017-08-03 01:10:18', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892915496248627201, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Luiz G. Melo', 'luiz__guilherme', 'Manaus - AM');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Luiz G. Melo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892896953075478529, 'Mandei foto do meu CPF ao suporte do app e eles pediram 10 DIAS pra resolver o problema. Pelos comentários do google store,vão demorar #Uber', '2017-08-02 23:56:37', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892896953075478529, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Luiz G. Melo', 'luiz__guilherme', 'Manaus - AM');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Luiz G. Melo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892895995733962752, 'Praticamente sigo bloqueado, sem poder pedir carro, pois meu ''CPF foi digitado errado várias vezes'', sendo que digitei certo, enfim #Uber', '2017-08-02 23:52:49', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892895995733962752, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Luiz G. Melo', 'luiz__guilherme', 'Manaus - AM');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Luiz G. Melo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892895676123762689, 'A #Uber segue desapontando. Passada rápida nos comentários do google play store, percebo q tem muita gente com o documento barrado pelo app.', '2017-08-02 23:51:33', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892895676123762689, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892893296128921600, '#DESCONTO #UBER 69r4uv5hue RT @betahomer: Eu vi o tempo passar, e tanta coisa mudar. #TimBeta #BetaHomer©', '2017-08-02 23:42:05', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892893296128921600, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betahomer');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892893256987668480, '#DESCONTO #UBER 69r4uv5hue RT @betahomer: Futuramente você entenderá porque Deus permitiu certas coisas em sua vida. #TimBeta #BetaHomer©', '2017-08-02 23:41:56', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892893256987668480, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betahomer');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892893243188412416, '#DESCONTO #UBER 69r4uv5hue RT @betahomer: É, de uns tempos pra cá, muita coisa mudou. #TimBeta #BetaHomer©', '2017-08-02 23:41:52', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892893243188412416, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betahomer');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Grazielle Caldeira', 'grazy_aloka', 'Montes Claros, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Grazielle Caldeira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892889576817250304, 'NAO ESPERAVA SER DEMITIDO? TÁ DESEMPREGADO?  CONHECE ALGUÉM QUE PRECISA?  BORA GANHAR DINHEIRO NA #UBER  CLIQUE... https://t.co/cFRl3QG5Im', '2017-08-02 23:27:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892889576817250304, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Bitous', 'girlfromurano', 'Rio de Janeiro, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Bitous';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892884042940641280, 'Não basta o motorista do #Uber ser lindo,simpático,voz grossa e tricolor,tem que ser cheiroso e ter acabado de sair do barbeiro. #Obrigada', '2017-08-02 23:05:19', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892884042940641280, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('obrigada');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Daniel  Leonardo', 'djleonardofilho');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Daniel  Leonardo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892881755572666368, '#Cabify oferece viagens de helicóptero em SP, um ano após testes do #Uber    Itaim Bibi a Guarulhos: R$ 500 reais.… https://t.co/K6oWxBTtsU', '2017-08-02 22:56:14', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892881755572666368, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cabify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('M A H', 'Hallecram', 'BH/MG/Brazil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'M A H';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892879787877965825, 'Código #uber: fe7nry  vai que... 😂', '2017-08-02 22:48:24', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892879787877965825, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892878145522675713, '#DESCONTO #UBER 69r4uv5hue RT @ThaisSilvaBeta: Quando o gato é firmeza... #TimBeta #BetaQuerLab https://t.co/xHWZtxwwxG', '2017-08-02 22:41:53', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892878145522675713, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('O coisinho', 'rhsantoz', 'Mafra, Portugal');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'O coisinho';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892875936248549376, 'Coragem é perguntar numa praça de táxis onde se apanha um #uber 😅😅😅', '2017-08-02 22:33:06', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892875936248549376, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892848764125421569, 'Ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Use e compartilhe o código: uber20pramim', '2017-08-02 20:45:08', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892848764125421569, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Selma Gimenes', 'selmagimenes', 'Curitiba, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Selma Gimenes';")[0][0]
    dao.Executa_SQL("insert into voudeque.lugar(latitude, longitude, nome_lugar) values('-25.6447517', '-49.3916434', 'araucária');")
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where nome_lugar = 'araucária' and latitude = '-25.6447517'and longitude = '-49.3916434';")[0][0]
    id_lugar = dao.Busca_SQL("select id from voudeque.lugar where lugar.nome_lugar = 'araucária';")[0][0]
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892847900245581824, '#Uber adorei a opção mensagem. Dá pra acrescentar a cor do carro? Ajuda e muito! Obrigada 🙏🏻 #passageira', '2017-08-02 20:41:42', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892847900245581824, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('passageira');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Silvia', 'silvysmdo', 'San Jose, Costa Rica');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Silvia';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892845415208558593, 'Gana 3 viajes de C.2000 gratis con este código krn6axyyue 💸💸💸💸💸💸💸💸💸💸💸💸💸💸 🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 @Uber @Uber_CR #uberpromo… https://t.co/VSD5oKEzZQ', '2017-08-02 20:31:49', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892845415208558593, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uberpromo', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Everton Santana', 'Evertonlolalozo', 'Itapecerica da Serra, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Everton Santana';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892835299755208704, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Dançar aumenta a felicidade. #TimBeta #BetaHomer©', '2017-08-02 19:51:38', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892835299755208704, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betahomer');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892834813383766016, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @betahomer: Dançar aumenta a felicidade. #TimBeta #BetaHomer©', '2017-08-02 19:49:42', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892834813383766016, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betahomer');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Tudo Sobre Floripa', 'tdsobrefloripa', 'Florianópolis - SC - Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Tudo Sobre Floripa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892817637918552066, 'Rapaz que vinha cometendo crimes desde a adolescência fez 18 anos em julho #TSF #Floripa #PolíciaCivil #Uber https://t.co/GZL9eAV0rl', '2017-08-02 18:41:27', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892817637918552066, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('tsf');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('floripa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('políciacivil');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Thamires Rodrigues', 'Thamie_th', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Thamires Rodrigues';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892815391646461964, 'Sobre o #uber  agora ter a corzinha do carro ♡♡♡♡♡♡ adorei!', '2017-08-02 18:32:31', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892815391646461964, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Rayssa', 'rayssaprates', 'Uberlândia - MG');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Rayssa';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892805638375559168, 'Fui olhar o perfil do motorista do #Uber que eu chamei e olha esse comentário kkkk ai gente. https://t.co/o95NGD5cQW', '2017-08-02 17:53:46', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892805638375559168, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892795939534123008, 'Precisa de uma carona? Usa #Uber com o código UBERVICWALKER e ganhe 2 viagens de até R$10! https://t.co/BMjMR7JPhE https://t.co/NMP14QwxZP', '2017-08-02 17:15:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892795939534123008, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Jefferson CS#timbeta', 'JeffeCSilva', 'São Vicente, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Jefferson CS#timbeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892791779979907073, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @JeffeCSilva: Ajuda aí #timbeta #TimBetaSegueTimBeta https://t.co…', '2017-08-02 16:58:42', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892791779979907073, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaseguetimbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('SupplyChainToday.com', 'SupplyChainBlog', 'Arizona');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'SupplyChainToday.com';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892790597479653376, '#DeepLearning #ArtificialIntelligence #Uber #machinelearning #bigdata #supplychain VIDEO: Uber Conference https://t.co/Vhs7vF9iLY', '2017-08-02 16:54:00', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892790597479653376, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('deeplearning');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('artificialintelligence');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('machinelearning');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('bigdata');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('supplychain');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Machos ao Natural', 'machosaonatural', 'São paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Machos ao Natural';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892777784799625216, 'Uber Frot Mlkão Estudante Capa – Videos curtos Do motorista ao nego Uber https://t.co/FYWKeucFex #capa4 #estudante #frottage #negão #uber', '2017-08-02 16:03:05', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892777784799625216, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('capa4');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('estudante');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('frottage');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('negão');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892774416257605633, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @eupauloph: Dando mamadeira 🍼 pra quem precisa #TimBeta https://t.co/EkA7HG1r1r', '2017-08-02 15:49:42', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892774416257605633, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892772456615882752, '#DESCONTO #UBER 69r4uv5hue RT @titapeace: a palavra amizade já teve mais valor... #timbetalab #timbeta', '2017-08-02 15:41:55', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892772456615882752, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetalab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('HAVANA Lab', 'havanalab', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'HAVANA Lab';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892763858292670464, 'PROMOÇÃO - Ganhe desconto nas suas viagens de Uber com o nosso código 8st93a9fue - #UBER #CÓDIGO #PROMOÇÃO #DESCONTO', '2017-08-02 15:07:45', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892763858292670464, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('código');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('promoção');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Felipe Silva (Japa)', 'FelipeMittal', 'Minas Gerais');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Felipe Silva (Japa)';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892759509944455169, 'Estou indignado! Eu cadastrei 1 cartão de crédito no #UberEATS e a informação migrou p/ o #uber, agora eu n consigo desvincular esse cartão', '2017-08-02 14:50:28', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892759509944455169, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('ubereats', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892757356857131008, '#DESCONTO #UBER 69r4uv5hue RT @willas_moreira: Bom dia ☀️  #BetaQuerlab  #BetaAjudaBeta  #TimBeta', '2017-08-02 14:41:55', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892757356857131008, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaquerlab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('betaajudabeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('bugada', 'mandylory');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'bugada';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892745119509729280, '#uber R$10 de desconto em cada uma de suas primeiras 2 viagens com a uber &gt;&gt; moc9e1', '2017-08-02 13:53:17', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892745119509729280, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('jeanotero', 'jeanotero6');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'jeanotero';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892742512426844161, 'RT @jean_je: Pensa em uma pessoa hoje que andou de #Uber até umas horas hen, passei o dia andando nisso!', '2017-08-02 13:42:55', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892742512426844161, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('DiEGO CASTILHO', 'diegoocastilhoo', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'DiEGO CASTILHO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892739320720875520, 'Já usou o #UBER? Crie sua conta com o código UBERVALEDESCONTO e ganhe um descontão na sua primeira viagem ✅', '2017-08-02 13:30:15', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892739320720875520, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Valdo Lôbo', 'lobo_bro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Valdo Lôbo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892737706136043520, 'Um desconto de R$14 em cada uma de suas primeiras 2 viagens com a Uber. Para aceitar, use o código 2se8w2tku  https://t.co/yR7lau2KGB #uber', '2017-08-02 13:23:50', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892737706136043520, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Liziane Berrocal', 'licaberrocal', 'Campo Grande');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Liziane Berrocal';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892737234377613313, 'Caro Marquinhos Trad, vou dar meu depoimento sobre o #UBER  O UBER me trouxe liberdade. Fim!  PS: Então, por... https://t.co/FQbGC0Dbd4', '2017-08-02 13:21:57', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892737234377613313, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892735536330412032, 'Use o código uber20pramim e ganhe R$20 de #desconto em cada uma de suas próximas 2 viagens no #Uber! Compartilhe.', '2017-08-02 13:15:12', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892735536330412032, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lucildo#PARCEIROSBET', 'LucildoC', 'Ceara Fortaleza');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lucildo#PARCEIROSBET';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892731633807314945, 'RT @betabrazzz: #DESCONTO #UBER 69r4uv5hue RT @RahulTayde9: Bom dia betas!! #TimBeta  #OperacaoBetaLab  #ParceirosBeta https://t.co/IFI0YpE…', '2017-08-02 12:59:42', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892731633807314945, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('operacaobetalab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('parceirosbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('BetaBR', 'betabrazzz', 'Campo Grande, Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'BetaBR';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892727175820062721, '#DESCONTO #UBER 69r4uv5hue RT @RahulTayde9: Bom dia betas!! #TimBeta  #OperacaoBetaLab  #ParceirosBeta https://t.co/IFI0YpEfu5', '2017-08-02 12:41:59', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892727175820062721, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('desconto');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('operacaobetalab');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('parceirosbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('W souza', '92wga');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'W souza';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892720276621996037, 'RT @CamilaTIMBeta17: #SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @GabrielSoligo: #MissaoBeta #TimBeta - Toda conquista começa com…', '2017-08-02 12:14:34', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892720276621996037, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('missaobeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Camila TIMBeta', 'CamilaTIMBeta17');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Camila TIMBeta';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892714025339015169, '#SDV HDRXB4JWUE #Uber #Gratis #Free #TimBetaAjuda RT @JeffeCSilva: Ajuda aí #timbeta #TimBetaSegueTimBeta https://t.co/4Vo72djWTU', '2017-08-02 11:49:44', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892714025339015169, 1);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('sdv');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('uber', '1');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('gratis');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('free');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaajuda');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbeta');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('timbetaseguetimbeta');")
except:
    print('Erro')
dao.Executa_SQL('DELETE FROM voudeque.usuario WHERE (id) IN (select * from(select usuario.id from voudeque.usuario left join voudeque.tweet on voudeque.usuario.id = voudeque.tweet.id_usuario where voudeque.tweet.id_usuario is null) as p);')
dao.Executa_SQL('DELETE FROM voudeque.lugar WHERE (id) IN (select * from(select lugar.id from voudeque.lugar left join voudeque.tweet on voudeque.lugar.id = voudeque.tweet.id_lugar where voudeque.tweet.id_lugar is null) as p);')
