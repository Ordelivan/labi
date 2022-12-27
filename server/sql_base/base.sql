
create table User(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null
);

create table Personal(
	id integer primary key autoincrement,
	login varchar(16) not null unique,
	password varchar(16) not null,
	power_level integer not null
);

create table Conference(
	id integer primary key autoincrement,
	name varchar,
	place varchar,
	presonalId integer not null
);


insert into User (login, password)
	values ("UserName1", "1234"), ("UserName2", "1234");
insert into Personal (login, password, power_level) 
	values ('PresonalName1' , '1234', 1), ('PresonalName2' , '1234', 2);
insert into Conference (name, place, presonalId)
	values ("conference1","place1",1), ("conference2","place2",2);
