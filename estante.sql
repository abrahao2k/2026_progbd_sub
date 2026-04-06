create database estante;

use estante;

create table livros(
codigo int primary key auto_increment,
titulo varchar(100),
autor varchar(100));

select * from livros;