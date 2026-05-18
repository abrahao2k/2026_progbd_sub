create database sistematop;

use sistematop;

create table usuarios(
codigo int primary key auto_increment,
usuario varchar(255),
senha varchar(255) );

insert into usuarios 
values(1,'joao','123');


insert into usuarios
values(2,'maria', 
	   aes_encrypt('ninja','segredo'));

select usuario, 
cast(aes_decrypt(senha, 'segredo') as char(100))
from usuarios;