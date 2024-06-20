CREATE DATABASE flipkart
USE flipkart

CREATE TABLE products
(
	pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(6),
    location VARCHAR(35) CHECK(location IN ('Mumbai', 'Delhi'))
);

CREATE TABLE customers
(
	cid INT(3) PRIMARY KEY,
    cname VARCHAR(30) NOT NULL,
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

CREATE TABLE employee
(
	eid INT(4) PRIMARY KEY,
    ename VARCHAR(45) NOT NULL,
    phone_no INT(11) NOT NULL,
    department VARCHAR(40) NOT NULL,
    manager_id INT(5)
);

INSERT INTO products VALUES(1, 'HP Laptop', 70000, 10, 'Mumbai');
INSERT INTO products VALUES(2, 'Realme Mobile', 20000, 5, 'Delhi');
INSERT INTO products VALUES(3, 'Realme Earphones', 1000, 15, 'Mumbai');
INSERT INTO products VALUES(4, 'Charger', 950, 12, 'Mumbai');
INSERT INTO products VALUES(5, 'Keyboard', 1500, 6, 'Delhi');

INSERT INTO customers VALUES(101, 'Ravi', 21, 'fdslfjl');
INSERT INTO customers VALUES(102, 'Suraj', 19, 'fdslfjl');
INSERT INTO customers VALUES(103, 'Arjun', 25, 'fdslfjl');
INSERT INTO customers VALUES(104, 'SINgh', 30, 'fdslfjl');
INSERT INTO customers VALUES(105, 'Rahul', 35, 'fdslfjl');

INSERT INTO orders VALUES(10001, 102, 3, 2700);
INSERT INTO orders VALUES(10002, 104, 2, 18000);
INSERT INTO orders VALUES(10003, 105, 4, 200);
INSERT INTO orders VALUES(10004, 101, 1, 9000);


INSERT INTO payment VALUES(1, 10001, 2700, 'upi', 'completed');
INSERT INTO payment VALUES(2, 10002, 18000, 'credit', 'completed');
INSERT INTO payment VALUES(3, 10003, 200, 'debit', 'completed');
INSERT INTO payment VALUES(4, 10004, 9000, 'credit', 'IN process');
INSERT INTO payment VALUES(5, 10005, 4500, 'upi', 'IN process');

INSERT INTO employee VALUES(401, "Rohan", 986275025, "Analysis", 401);
INSERT INTO employee VALUES(402, "Sanjay", 846929084, "Delivery", 404);
INSERT INTO employee VALUES(403, "Ajay", 967510568, "Tech", 403);
INSERT INTO employee VALUES(404, "Varun", 637845019, "Sales", 404);
INSERT INTO employee VALUES(405, "Kiran", 729624062, "HR", 402);

SELECT * FROM products;

SELECT * FROM customer;

SELECT * FROM orders;

SELECT * FROM payment;

SELECT * FROM employee;

SELECT customers.cid, cname, orders.oid FROM orders 
INNER JOIN customer ON orders.cid = customer.cid;

SELECT products.pid, pname, amt, orders.oid FROM products
LEFT JOIN orders ON orders.pid = products.pid;

SELECT * FROM payment 
RIGHT JOIN orders ON orders.oid = payment.oid;

SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
LEFT JOIN products ON orders.pid = products.pid
UNION
SELECT orders.oid, products.pid, pname, amt, price, stock, location FROM orders
RIGHT JOIN products ON orders.pid = products.pid;

SELECT e1.ename AS Employee, e2.ename AS Manager FROM employee e1
INNER JOIN employee e2 ON e1.manager_id = e2.eid;

SELECT customer.cid, cname, orders.oid, amt FROM customer
CROSS JOIN orders ON customer.cid = orders.cid
WHERE amt > 3000;








