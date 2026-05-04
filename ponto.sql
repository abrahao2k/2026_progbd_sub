create database empresa;
use empresa;
create table ponto(
codigo int primary key auto_increment,
funcionario int,
data_ponto date,
hora_ponto time);
insert into ponto values
(1, 35, "2026-05-04", "07:03:00");

insert into ponto values
(2, 35, "2026-05-04", "45:67:88");

select * from ponto;


select timediff("11:58:15",
"07:03:00");

select addtime("04:55:15",
"03:28:35");

select hour("07:03:00");
select minute("07:03:00");
select second("07:03:00");

select year("2026-05-04");
select month("2026-05-04");
select day("2026-05-04");

create table ponto2(
codigo int primary key auto_increment,
funcionacio int,
marcacao datetime);

insert into ponto2 values
(null,35,"2026-05-04 07:03:00");

select timediff("2026-05-04 08:00:00",
"2026-05-01 07:00:00");

select now(); 
# now() informa data e hora atual do sistema

insert into ponto2 values(
null, 48, now() );


select * from ponto2;
