CREATE DATABASE myntra
USE myntra

CREATE TABLE products
(
	pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(7),
    location VARCHAR(30) CHECK(location IN('Mumbai', 'Delhi'))
);

CREATE TABLE customer
(
	cid INT(3) PRIMARY KEY,
    cname VARCHAR(35) NOT NULL,
    age INT(3),
    addr VARCHAR(50)
);

CREATE TABLE orders
(
	oid INT(3) PRIMARY KEY,
    cid INT(3),
    pid INT(3),
    amt INT(10) NOT NULL,
    FOREIGN KEY(cid) REFERENCES customer(cid),
    FOREIGN KEY(pid) REFERENCES products(pid)
);

CREATE TABLE payment
(
	pay_id INT(3) PRIMARY KEY,
    oid INT(3),
    amount INT(10) NOT NULL,
    MODE VARCHAR(30) CHECK(MODE IN('upi', 'credit', 'debit')),
	STATUS VARCHAR(30),
    FOREIGN KEY(oid) REFERENCES orders(oid)
);

ALTER TABLE payment
ADD COLUMN timestamp TIMESTAMP;

INSERT INTO products VALUES(1, 'HP Laptop', 70000, 10, 'Mumbai');
INSERT INTO products VALUES(2, 'Realme Mobile', 20000, 5, 'Delhi');
INSERT INTO products VALUES(3, 'Realme Earphones', 1000, 15, 'Mumbai');
INSERT INTO products VALUES(4, 'Charger', 950, 12, 'Mumbai');
INSERT INTO products VALUES(5, 'Keyboard', 1500, 6, 'Delhi');

INSERT INTO customer VALUES(101, 'Ravi', 21, 'fdslfjl');
INSERT INTO customer VALUES(102, 'Suraj', 19, 'fdslfjl');
INSERT INTO customer VALUES(103, 'Arjun', 25, 'fdslfjl');
INSERT INTO customer VALUES(104, 'Singh', 30, 'fdslfjl');
INSERT INTO customer VALUES(105, 'Rahul', 35, 'fdslfjl');

INSERT INTO orders VALUES(10001, 102, 3, 2700);
INSERT INTO orders VALUES(10002, 104, 2, 18000);
INSERT INTO orders VALUES(10003, 105, 4, 200);
INSERT INTO orders VALUES(10004, 101, 1, 9000);

INSERT INTO payment VALUES(1,10001,2700,'upi','completed');
INSERT INTO payment VALUES(2,10002,18000,'credit','completed');
INSERT INTO payment VALUES(3,10003,200,'debit','in process');

UPDATE PAYMENT
SET timestamp = '2024-06-20 10:55:45'
WHERE pay_id = 1;
SET TIMESTAMP = '2024-06-20 11:00:10'
WHERE pay_id = 2;
UPDATE payment
SET TIMESTAMP = '2024-06-20 11:30:00'
WHERE pay_id = 3;

--SINGLE ROW SUBQUERIES
SELECT cname FROM customer
WHERE cid=(SELECT cid
FROM orders
ORDER BY amt
DESC LIMIT 1);

SELECT pname FROM products
WHERE price=(SELECT MAX(price) FROM products);

--MULTIPLE-ROW SUBQUERIES
SELECT cname
FROM customer
WHERE cid IN (SELECT cid
FROM orders);

--CORRELATED SUBQUERIS
SELECT pname, price
FROM products p
WHERE price > (
	SELECT AVG(price)
    FROM products
    WHERE location = p.location
);

--INNERJOIN
SELECT p.pname, o.oid, o.amt
FROM products p
INNER JOIN (
    SELECT *
    FROM orders
) o ON p.pid = o.pid
WHERE p.price > 100

--LEFTJOIN
SELECT p.pname, SUM(o.amt) AS total_orders_amount
FROM products p
LEFT JOIN orders o ON p.pid = o.pid
GROUP BY p.pname

--RIGHTJOIN
SELECT o.oid, o.amt, p.status, p.timestamp
FROM orders o
RIGHT JOIN payment p ON o.oid = p.oid;

--RANK
SELECT pid, pname, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

--DENSE_RANK
SELECT pid, pname, price, 
DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

--ROW_NUMBER
SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, cid, cname, age, addr
FROM customer;

--CUME_DIST
SELECT oid, amount,
CUME_DIST() OVER (ORDER BY amount) AS cumulative_distribution
FROM payment;

--LAG
SELECT pname, price, location,
LAG(price) OVER (PARTITION BY location ORDER BY price) AS lag_price
FROM products;

--LEAD
SELECT pname, price, location,
LEAD(price) OVER (PARTITION BY location ORDER BY price) AS lead_price
FROM products;