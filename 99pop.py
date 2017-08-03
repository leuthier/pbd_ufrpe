import persistencia.DataBase as dao
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
dao.Executa_SQL('DELETE FROM voudeque.usuario WHERE (id) IN (select * from(select usuario.id from voudeque.usuario left join voudeque.tweet on voudeque.usuario.id = voudeque.tweet.id_usuario where voudeque.tweet.id_usuario is null) as p);')
dao.Executa_SQL('DELETE FROM voudeque.lugar WHERE (id) IN (select * from(select lugar.id from voudeque.lugar left join voudeque.tweet on voudeque.lugar.id = voudeque.tweet.id_lugar where voudeque.tweet.id_lugar is null) as p);')
