CREATE DATABASE amazon
USE amazon
CREATE TABLE products
(
	pid int(3) primary key,
    pname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    location varchar(30) check(location in ('Mumbai', 'Delhi'))
);

CREATE TABLE customer
(
cid int(3) primary key,
cname varchar(30) not null,
age int(3),
addr varchar(50)
);

CREATE TABLE orders
(
	oid int(3) primary key,
    cid int(3),
    pid int(3),
    amt int(10) not null,
    foreign key(cid) references customer(cid)
);

CREATE TABLE payment
(
	pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);

ALTER TABLE customer

ALTER TABLE orders
RENAME COLUMN amt to amount

TRUNCATE table products

INSERT INTO products VALUES(1, 'HP Laptop', 70000, 15, 'Mumbai')
INSERT INTO products VALUES(2, 'Realme Mobile', 20000, 30, 'Delhi')








