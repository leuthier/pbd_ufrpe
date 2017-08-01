drop schema if exists voudeque;
CREATE SCHEMA if not exists voudeque ;
ALTER DATABASE voudeque CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use voudeque;

create table if not exists marca(
	id int auto_increment,
    nome varchar(20) not null unique,
    PRIMARY KEY (id)) ENGINE=InnoDB;

create table if not exists sentimento(
	id int auto_increment,
    classe varchar(20) not null unique,
    PRIMARY KEY (id)) ENGINE=InnoDB;

create table if not exists lugar(
	id int auto_increment,
    latitude varchar(20),
    longitude varchar(20),
    nome_lugar varchar(50) not null,
    PRIMARY KEY (id)) ENGINE=InnoDB;

create table if not exists usuario(
	id int auto_increment,
    nome varchar(140) CHARACTER SET utf8 not null,
    username varchar(140) CHARACTER SET utf8 not null unique,
    nome_lugar varchar(50) CHARACTER SET utf8 unique,
    PRIMARY KEY (id)) ENGINE=InnoDB;

create table if not exists tweet(
	id bigint,
    texto varchar(140) CHARACTER SET utf8 not null,
    dataHora DateTime,
    id_sentimento int not null,
    id_usuario int not null unique,
    id_lugar int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_sentimento) references sentimento(id),
    FOREIGN KEY (id_usuario) references usuario(id),
    FOREIGN KEY (id_lugar) references lugar(id)) ENGINE=InnoDB;

create table if not exists hashtag(
	id int auto_increment,
    texto varchar(140) CHARACTER SET utf8 not null unique,
    id_marca int,
    PRIMARY KEY (id),
    FOREIGN KEY(id_marca) references marca(id)) ENGINE=InnoDB;

create table if not exists tweet_marca(
	id_tweet bigint not null,
    id_marca int not null,
    PRIMARY KEY(id_tweet, id_marca),
    FOREIGN KEY (id_tweet) references tweet(id),
    FOREIGN KEY (id_marca) references marca(id)) ENGINE=InnoDB;



insert into voudeque.marca(nome) value('Uber');
insert into voudeque.marca(nome) value('Cabify');
insert into voudeque.marca(nome) value('99Pop');

insert into voudeque.sentimento(classe) value ('Positivo');
insert into voudeque.sentimento(classe) value ('Negativo');
insert into voudeque.sentimento(classe) value ('Neutro');

insert into voudeque.hashtag(texto,id_marca) value('Uber',1);
insert into voudeque.hashtag(texto,id_marca) value('Cabify',2);
insert into voudeque.hashtag(texto,id_marca) value('99Pop',3);