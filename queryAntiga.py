import persistencia.DataBase as dao

try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892928104133513216, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/xFfMxUty69', '2017-08-03 02:00:24', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892928104133513216, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Praia do Pepê', 'Praiadopepe', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Praia do Pepê';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892915496248627201, 'Concorrente do #Uber, #Cabify promete briga acirrada. https://t.co/anlrh4obBO', '2017-08-03 01:10:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892915496248627201, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('uber');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892913042958286849, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/COpNhesZYQ', '2017-08-03 01:00:33', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892913042958286849, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892897893287428097, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/wfRwFOKxqD', '2017-08-03 00:00:21', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892897893287428097, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892882761790443524, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/fbKv1C10qu', '2017-08-02 23:00:14', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892882761790443524, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Daniel  Leonardo', 'djleonardofilho');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Daniel  Leonardo';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892881755572666368, '#Cabify oferece viagens de helicóptero em SP, um ano após testes do #Uber    Itaim Bibi a Guarulhos: R$ 500 reais.… https://t.co/K6oWxBTtsU', '2017-08-02 22:56:14', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892881755572666368, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('uber');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892871415845842945, 'Precisa ir a algum lugar e está sem dinheiro? Vai de #Cabify com código VICTORIAM124 e ganhe R$15 pra usar!… https://t.co/UNnzRiFGAZ', '2017-08-02 22:15:08', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892871415845842945, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892867681149476865, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/ANtPK1aXz5', '2017-08-02 22:00:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892867681149476865, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892852619085045761, 'Desconto 15% no Cabify #PoA 🚘 Código 👉 CABIBR1425 . ⚠️ Pra quem ainda não usou 📌 Válido: 31/12 . #Cabify https://t.co/mRvhhqUNZ5', '2017-08-02 21:00:27', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892852619085045761, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892845079962034176, 'Assim como eu, use #Cabify e ganhe R$20,00 na sua primeira viagem . Registre-se aqui: https://t.co/MKGgKWexbD', '2017-08-02 20:30:29', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892845079962034176, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892837620363014144, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/EK93hoq8KF', '2017-08-02 20:00:51', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892837620363014144, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892822605723561984, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/fexQ7O9NEM', '2017-08-02 19:01:11', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892822605723561984, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892807325421056010, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/3T0lezGyOg', '2017-08-02 18:00:28', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892807325421056010, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Transponster', 'alvaroleme', 'São Paulo, SP');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Transponster';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892805771959906310, 'quer uma água? quer bala? ar tá bom? rádio de preferência?   Me sinto no De Frente com Gabi #Cabify', '2017-08-02 17:54:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892805771959906310, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892792200454692864, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/5uC5kyXOn0', '2017-08-02 17:00:22', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892792200454692864, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Hená Deslandes', 'henadeslandes', 'São Paulo');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Hená Deslandes';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892791636270489600, 'Uma delícia chamada entrar no #Cabify e a #kissfm estar mandando um #ramones 🤘', '2017-08-02 16:58:08', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892791636270489600, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('kissfm');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('ramones');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892777137102622720, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/k1RMw5mLTH', '2017-08-02 16:00:31', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892777137102622720, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892761995174457344, 'Desconto 15% no Cabify #PoA 🚘 Código 👉 CABIBR1425 . ⚠️ Pra quem ainda não usou 📌 Válido: 31/12 . #Cabify https://t.co/y4kV1mMq5L', '2017-08-02 15:00:21', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892761995174457344, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892747140027625472, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/LmLTKQbu2G', '2017-08-02 14:01:19', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892747140027625472, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892746866181500929, 'Ganhe R$20,00 na sua primeira corrida de #Cabify usando o código mauricioo322', '2017-08-02 14:00:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892746866181500929, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892732068010094592, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/6FKeoUFNc3', '2017-08-02 13:01:25', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892732068010094592, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892716679343599616, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/XkPSLln6i3', '2017-08-02 12:00:16', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892716679343599616, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Fabio Bobbio', 'fabiobob', 'Vitória-ES');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Fabio Bobbio';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892712571584860160, '#Cabify permite agendar voos de helicóptero pelo seu aplicativo - https://t.co/57j9VKJD9g', '2017-08-02 11:43:57', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892712571584860160, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892701749798219777, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/fJm39AQ2gK', '2017-08-02 11:00:57', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892701749798219777, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892686463955087368, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/OHTSTtdzAL', '2017-08-02 10:00:12', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892686463955087368, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892671440251748352, 'Desconto 15% no Cabify #PoA 🚘 Código 👉 CABIBR1425 . ⚠️ Pra quem ainda não usou 📌 Válido: 31/12 . #Cabify https://t.co/MHbbBv51t5', '2017-08-02 09:00:31', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892671440251748352, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892555946731483136, 'Desconto 15% no Cabify #PoA 🚘 Código 👉 CABIBR1425 . ⚠️ Pra quem ainda não usou 📌 Válido: 31/12 . #Cabify https://t.co/Wx0fmeUf1G', '2017-08-02 01:21:35', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892555946731483136, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892550572695539713, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/BtdLxjfzEf', '2017-08-02 01:00:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892550572695539713, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892509059563343873, 'Precisa ir a algum lugar e está sem dinheiro? Vai de #Cabify com código VICTORIAM124 e ganhe R$15 pra usar!… https://t.co/c8ASU2aB7W', '2017-08-01 22:15:16', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892509059563343873, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892490340720103425, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/bCfmoirbPx', '2017-08-01 21:00:53', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892490340720103425, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892482624094183424, 'Assim como eu, use #Cabify e ganhe R$20,00 na sua primeira viagem . Registre-se aqui: https://t.co/MKGgKWexbD', '2017-08-01 20:30:13', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892482624094183424, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892460038681493507, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/qnEcnBFZG0', '2017-08-01 19:00:28', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892460038681493507, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Maurício#BetaquerLab', 'MauricioArauj01', 'Maceió, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Maurício#BetaquerLab';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892449842173272064, 'RT @thathaocosta: Usem #Cabify amoressss.. Meu código é THAMYRESC15  e  ganha desconto ai', '2017-08-01 18:19:57', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892449842173272064, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892429926338637825, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/ArAA29lCIL', '2017-08-01 17:00:49', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892429926338637825, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892399845469716480, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/nutZPFSVdk', '2017-08-01 15:01:17', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892399845469716480, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892384562155794432, 'Ganhe R$20,00 na sua primeira corrida de #Cabify usando o código mauricioo322', '2017-08-01 14:00:33', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892384562155794432, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892369510426189824, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/VSKMQ9pZY9', '2017-08-01 13:00:45', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892369510426189824, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Orkut.br.com', 'orkut_li');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Orkut.br.com';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892369166363176960, 'RT @lihzamith: Nessa promo Do Cabify - orkut consegui DEPOIMENTO, SCRAP, COMUNIDADE, SORTEDEHOJE. Mais alguma gente? #Cabify #Orkut https:/…', '2017-08-01 12:59:23', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892369166363176960, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('orkut');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892339352122077184, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/PfyeAX98sp', '2017-08-01 11:00:55', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892339352122077184, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892309077287686145, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/VePkNuIRqV', '2017-08-01 09:00:36', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892309077287686145, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Lívia Zamith', 'lihzamith', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Lívia Zamith';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892217422018641920, 'Nessa promo Do Cabify - orkut consegui DEPOIMENTO, SCRAP, COMUNIDADE, SORTEDEHOJE. Mais alguma gente? #Cabify #Orkut https://t.co/SeUZwvFada', '2017-08-01 02:56:24', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892217422018641920, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('orkut');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892203270638366720, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/HPqGEqzbfr', '2017-08-01 02:00:10', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892203270638366720, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Alice Herrera', 'herreralice');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Alice Herrera';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892198566801940481, '@cabifybrasil  Códigos do orkut: comunidade, depoimento, scrap, sortedehoje #cabify #orkut', '2017-08-01 01:41:29', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892198566801940481, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('orkut');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('JOÃO', 'joaomagagnin', 'BRASIL');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'JOÃO';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892189027377569793, 'Meu povo, segura esses códigos do cabify: scrap, comunidade e depoimento #cabify', '2017-08-01 01:03:34', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892189027377569793, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892188250596659201, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/Q1ppwLrZFv', '2017-08-01 01:00:29', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892188250596659201, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892173130239803393, '#Spotify | Playlist Cabify PoA: Curtindo a Vida! . 🎶 https://t.co/VIU793T23u . #Cabify #PoA #PortoAlegre #Spotify… https://t.co/6SWnhHvNgu', '2017-08-01 00:00:24', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892173130239803393, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portoalegre');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Bruno Rodrigues', 'BrunoRodrigues_', 'Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Bruno Rodrigues';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892172463433535488, '#Cupom #Cabify #Brasília VEMAGOSTO  10 viagens com 25% desconto.', '2017-07-31 23:57:45', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892172463433535488, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('cupom');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('brasília');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Ariana', 'Ariana______');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Ariana';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892170455343411201, 'teste pro projeto #cabify', '2017-07-31 23:49:46', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892170455343411201, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892158079252516864, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/XIRRzcquV4', '2017-07-31 23:00:36', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892158079252516864, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Victoria', 'Vic_Walker', 'São Paulo, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Victoria';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892146632061538304, 'Precisa ir a algum lugar e está sem dinheiro? Vai de #Cabify com código VICTORIAM124 e ganhe R$15 pra usar!… https://t.co/VV0vnIq7hM', '2017-07-31 22:15:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892146632061538304, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892143032316956675, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/oKrnMtXnSR', '2017-07-31 22:00:48', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892143032316956675, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892127914342350855, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/0Ivu0Qdh8r', '2017-07-31 21:00:44', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892127914342350855, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892120211977121795, 'Assim como eu, use #Cabify e ganhe R$20,00 na sua primeira viagem . Registre-se aqui: https://t.co/MKGgKWexbD', '2017-07-31 20:30:07', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892120211977121795, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892112731435827200, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/N3ntzPNWYh', '2017-07-31 20:00:24', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892112731435827200, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892097849533530112, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/IARV6BwMVa', '2017-07-31 19:01:16', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892097849533530112, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892082697832673281, '#Spotify | Playlist Cabify PoA: Curtindo a Vida! . 🎶 https://t.co/VIU793T23u . #Cabify #PoA #PortoAlegre #Spotify… https://t.co/FdRt6DaNmP', '2017-07-31 18:01:03', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892082697832673281, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portoalegre');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892067655410212871, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/kPYphjozhP', '2017-07-31 17:01:17', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892067655410212871, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Chefe Da Quadrilha', 'QueroSerRica', 'Rio de Janeiro');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Chefe Da Quadrilha';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892060165092118530, 'Oi @CabifyRj vou precisar de promoção pra 2 corridas na 5a feira. Dá uma ajuda aí, vai... Nunca te pedi nada. #Cabify #vádecabify', '2017-07-31 16:31:31', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892060165092118530, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('vádecabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892052340370485249, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/iWLAQx9chR', '2017-07-31 16:00:26', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892052340370485249, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892037379690827777, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/DGdO0g1ZJ8', '2017-07-31 15:00:59', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892037379690827777, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892022266220990466, 'Siga/Curta nossos perfis: . 🚗 Twitter: https://t.co/1B59U1HWH7 . 🚗 Facebook: https://t.co/sNzhLhIZnv . #Cabify #PoA… https://t.co/3JVZC7a64p', '2017-07-31 14:00:55', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892022266220990466, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Mauricio Oliveira', 'aventureiros', 'Rio de Janeiro - RJ');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Mauricio Oliveira';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892022115452538880, 'Ganhe R$20,00 na sua primeira corrida de #Cabify usando o código mauricioo322', '2017-07-31 14:00:19', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892022115452538880, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(892007275770073090, 'Cabify e Panvel levam e buscam você gratuitamente pra doar sangue em POA. . Saiba mais 👉 https://t.co/3FngKpEnq3 .… https://t.co/5e81TNflYh', '2017-07-31 13:01:21', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(892007275770073090, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891992104506990592, '#Spotify | Playlist Cabify PoA: Curtindo a Vida! . 🎶 https://t.co/VIU793T23u . #Cabify #PoA #PortoAlegre #Spotify… https://t.co/7gMMdYcpnp', '2017-07-31 12:01:04', '3', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891992104506990592, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('portoalegre');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('spotify');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username) values('Teresa Wegner', 'teresa_wegner');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Teresa Wegner';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891991458059833344, 'RT @talitha_cardozo: A voz do Waze do #Cabify é o Faustão. Why God why?', '2017-07-31 11:58:30', '2', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891991458059833344, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891976961769299968, 'Desconto 50% no Cabify PoA 🚘 Código 👉 INGREDIENTE . ⚠️ Só p/ novos usuários. 📌 Válidade até: 15/12. . #Cabify #PoA… https://t.co/AsgmCjIoPf', '2017-07-31 11:00:54', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891976961769299968, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto,id_marca) values('cabify', '2');")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891961693089275904, 'Ação da Cabify com o @governo_rs está sendo um sucesso: já foram + de 30 mil peças arrecadadas!  👉… https://t.co/7eWrpPXRPi', '2017-07-31 10:00:14', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891961693089275904, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891946694774071296, 'Receba R$15 de desconto em sua 1ª viagem utilizando o código: 👉 ZENELIT1 ou faça o cadastro no link:… https://t.co/uCXjsQpaTy', '2017-07-31 09:00:38', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891946694774071296, 2);")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891916413325193216, 'Desconto 50% no Cabify #PoA 🚘 Código 👉 2ANOSMAORISUNSET . ⚠️ Destino/Origem Arena do Grêmio 📌 Válido 30/07 - 12h at… https://t.co/XJab6uxMps', '2017-07-31 07:00:18', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891916413325193216, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')
try:
    dao.Executa_SQL("insert into voudeque.usuario(nome, username, nome_lugar) values('Cabify PoA', 'CabifyPoA', 'Porto Alegre, Brasil');")
    id_usuario = dao.Busca_SQL("select id from voudeque.usuario where usuario.nome = 'Cabify PoA';")[0][0]
    id_lugar = 'null'
    str_id_usuario = str(id_usuario)
    str_id_lugar = str(id_lugar)
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891886189917208576, 'Desconto 50% no Cabify #PoA 🚘 Código 👉 2ANOSMAORISUNSET . ⚠️ Destino/Origem Arena do Grêmio 📌 Válido 30/07 - 12h at… https://t.co/qRHxlqZ6sH', '2017-07-31 05:00:12', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
    dao.Executa_SQL("insert into voudeque.tweet_marca(id_tweet, id_marca) values(891886189917208576, 2);")
    dao.Executa_SQL("insert into voudeque.hashtag(texto) values('poa');")
except:
    print('Erro')

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
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891770237183569920, 'Meu cupom ♥:uberrgomes: te dá R$ 20 de desconto em suas primeiras viagens (10 cada) com @Uber_Brasil @Uber #uber #desconto #cupom #promocao', '2017-07-30 21:19:27', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
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
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732881671954432, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasild', '2017-07-30 18:51:01', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
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
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732856946524161, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasie', '2017-07-30 18:50:55', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
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
    dao.Executa_SQL("insert into voudeque.tweet(id, texto, dataHora, id_sentimento, id_usuario, id_lugar) values(891732792178089984, 'mc9v26  #uber código promocional 20$ de desconto #UberEATS #ubersurvivor #ubermg #ubercode #linda #lindo #cute #br #twitter   #brasil', '2017-07-30 18:50:39', '1', " + str_id_usuario + ", " + str_id_lugar + ");")
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

dao.Executa_SQL('DELETE FROM voudeque.usuario WHERE (id) IN (select * from(select usuario.id from voudeque.usuario left join voudeque.tweet on voudeque.usuario.id = voudeque.tweet.id_usuario where voudeque.tweet.id_usuario is null) as p);')
dao.Executa_SQL('DELETE FROM voudeque.lugar WHERE (id) IN (select * from(select lugar.id from voudeque.lugar left join voudeque.tweet on voudeque.lugar.id = voudeque.tweet.id_lugar where voudeque.tweet.id_lugar is null) as p);')
