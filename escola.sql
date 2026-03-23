create database escola;
use escola;
create table alunos(
codigo int primary key 
auto_increment,
nome varchar(100) not null,
curso varchar(100),
serie int);
