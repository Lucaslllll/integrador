create database repositorio;
use repositorio;

create table cadastro(
	id int auto_increment primary key, 
	nome varchar(200) not null,
    senha varchar(16) not null,
    nascimento date not null,
	sexo varchar(10)
    
);

create table games(
	id int auto_increment primary key,
    novogame text,
    nome varchar(200) not null,
    descricao text

);

create table materia(
	id int auto_increment primary key,
    conteudo text not null,
	nomej text,
    foreign key (nome) references games (nome) 
);
