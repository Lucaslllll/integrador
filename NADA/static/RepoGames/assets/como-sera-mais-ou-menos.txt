create database repositorio;
use repositorio;
select * from cadastro;
describe cadastro;
create table cadastro(
	id int auto_increment primary key, 
	nome varchar(200) not null,
    email varchar(100),
    senha varchar(16) not null,
    nascimento date not null,
	sexo varchar(10)
    
);
alter table cadastro add email varchar(100);
alter table cadastro add nascimento date;
alter table cadastro add sexo varchar(11);
alter table cadastro drop nascimento;
alter table cadastro drop sexo;
alter table cadastro modify sexo varchar(16);

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
