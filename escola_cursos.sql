use escola;

create table cursos(
codigo int primary key auto_increment,
nome varchar(100));

insert into cursos values(1, 'Informática');
insert into cursos values(2, 'Letras');
insert into cursos values(3, 'Biologia');
insert into cursos values(4, 'Matemática');
insert into cursos values(5, 'Física');
insert into cursos values(6, 'Direito');

select * from cursos;
