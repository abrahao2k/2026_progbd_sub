# criar um banco de dados
create database aula;

# escolher o banco que será usado
use aula;

# criar uma tabela
create table contato(
codigo int primary key auto_increment,
nome varchar(60) not null,
telefone varchar(60)
);

# exibir os dados da tabela
select * from contato;

# inserir um cadastro na tabela
insert into contato
values(1,"Ana","9876-5432");

# inserir usando o auto_increment
insert into contato
values(null, "Helena", "9888-7777");

insert into contato(nome,telefone)
values("Kelvin","8877-4433");

# cadastrar vários registros em um comando
insert into contato values
(null,"Carlos","7415-1245"),
(null,"Marisa","9999-1111"),
(null,"Dionisio","4444-3332");

# variações do SELECT
# ordenar por uma coluna indicada
select * from contato 
order by nome;

# ordem inversa
select * from contato order by codigo desc;

# usando condições
select * from contato
where nome = "ana" or nome = "helena";







