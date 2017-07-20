drop schema if exists voudeque;
CREATE SCHEMA if not exists voudeque ;
ALTER DATABASE voudeque CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use voudeque;

create table if not exists marca(
	id int auto_increment,
    nome varchar(20) not null unique,
    PRIMARY KEY (id));
    
create table if not exists sentimento(
	id int auto_increment,
    classe varchar(20) not null unique,
    PRIMARY KEY (id));
    
create table if not exists usuario(
	id int auto_increment,
    nome varchar(140) CHARACTER SET utf8 not null,
    username varchar(140) CHARACTER SET utf8 not null,
    nome_lugar varchar(50) CHARACTER SET utf8 unique,
    PRIMARY KEY (id));

    
create table if not exists lugar(
	id int auto_increment,
    latitude varchar(20),
    longitude varchar(20),
    nome_lugar varchar(50) not null,
    PRIMARY KEY (id));
    
create table if not exists hashtag(
	id int auto_increment,
    texto varchar(140) CHARACTER SET utf8 not null unique,
    id_marca int,
    PRIMARY KEY (id),
    FOREIGN KEY(id_marca) references marca(id));
    
create table if not exists tweet(
	id bigint,
    texto varchar(140) CHARACTER SET utf8 not null,
    tipo varchar(20),
    dataHora DateTime,
    id_sentimento int not null,
    id_usuario int,
    id_lugar int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_sentimento) references sentimento(id),
    FOREIGN KEY (id_usuario) references usuario(id),
    FOREIGN KEY (id_lugar) references lugar(id));

create table if not exists tweet_local(
	id_tweet bigint not null,
	id_local int not null,
	PRIMARY KEY(id_tweet, id_local));
    
create table if not exists tweet_marca(
	id_tweet bigint not null,
    id_marca int not null,
    PRIMARY KEY(id_tweet, id_marca));
    
    
    
insert into voudeque.marca(nome) value('Uber');
insert into voudeque.marca(nome) value('Cabify');
insert into voudeque.marca(nome) value('99pop');

insert into voudeque.sentimento(classe) value ('Positivo');
insert into voudeque.sentimento(classe) value ('Negativo');
insert into voudeque.sentimento(classe) value ('Neutro');

insert into voudeque.hashtag(texto,id_marca) value('99pop',3);
insert into voudeque.hashtag(texto,id_marca) value('Uber',1);
insert into voudeque.hashtag(texto,id_marca) value('Cabify',2);
