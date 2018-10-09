create database blog;
use database;
create table user (
seq int primary key auto_increment,
id varchar(255) not null,
password varchar(255) not null,
regist_date datetime default now(),
modify_date datetime default null,
delete_yn varchar(10) default 'Y'
);

create table user_login_attempt(
seq int primary key auto_increment,
user_id int not null,
attempt int default 1,
regist_date datetime default now(),
modify_date datetime default null
);

insert into user(id, password) values ('test', 'test');