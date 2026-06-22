create database esportes;

use esportes;

create table times(
codigo int primary key auto_increment,
nome varchar(100),
esporte varchar(100),
participantes int);

insert into times values(1,"Potiguar","Futebol",11);
insert into times values(2,"V-Info","Vôlei",8);
insert into times values(3,"Gugão","Tênis",1);
insert into times values(4,"Melekos","Basquete",12);