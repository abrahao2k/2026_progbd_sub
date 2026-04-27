create database hotel;

use hotel;

create table reserva(
codigo int primary key auto_increment,
cliente varchar(100),
data_entrada date,
data_saida date);

insert into reserva values
(1,"Gilberto Gomes","2026-04-28","2026-04-29");