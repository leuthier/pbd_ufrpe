import persistencia.DataBase as dao
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
