create table user(
seq int primary key auto_increment,
id varchar(255) not null,
password varchar(255) not null,
username varchar(255) not null,
email varchar(255) not null,
phone varchar(255) not null,
address varchar(255) not null,
game_type int not null,
is_staff int default 0,
regist_date datetime default now(),
modify_date datetime default now(),
delete_yn varchar(10) default 'N'
);

create table user_login_attempt(
seq int primary key auto_increment,
user_id int not null,
attempt int default 0,
regist_date datetime default now(),
modify_date datetime default now(),
delete_yn varchar(10) default 'N'
);

create table code_group(
id int primary key,
group_name varchar(255) not null,
regist_date datetime default now(),
modify_date datetime default now()
);

create table code_detail(
seq int primary key auto_increment,
group_id int not null,
id int not null,
code_name varchar(255) not null,
regist_date datetime default now(),
modify_date datetime default now()
);

create table history_payment(
seq int primary key auto_increment,
user_id int not null,
money int not null,
charge_time varchar(255) not null,
back varchar(10) default 'N',
regist_date datetime default now()
);

create table user_time(
seq int primary key auto_increment,
user_id int not null,
user_time varchar(255) default '0',
regist_date datetime default now(),
modify_date datetime default now(),
delete_yn varchar(10) default 'N'
);

create table history_use_time(
seq int primary key auto_increment,
user_id int not null,
use_time varchar(255) not null,
regist_date datetime default now()
);

create table history_idle_time(
seq int primary key auto_increment,
user_id int not null,
idle_time varchar(255) not null,
regist_date datetime default now()
);

create table user_log(
seq int primary key auto_increment,
user_id int not null,
start_end int not null,
regist_date datetime default now()
);

create table logic_lock(
logic int primary key,
logic_lock int default 0
);

insert into code_group (id, group_name) values(1, '게임');
insert into code_group (id, group_name) values(2, '요금제');
insert into code_group (id, group_name) values(3, '서비스상태');
insert into code_group (id, group_name) values(4, '트랜잭션');

insert into code_detail (group_id, id, code_name) values(3, 1, '시작');
insert into code_detail (group_id, id, code_name) values(3, 2, '종료');

insert into code_detail (group_id, id, code_name) values(4, 1, '회원가입');
insert into code_detail (group_id, id, code_name) values(4, 2, '서비스');