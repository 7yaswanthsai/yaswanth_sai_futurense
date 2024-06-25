CREATE DATABASE flipkart
USE flipkart

CREATE TABLE products
(
	pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(6),
    locatiON VARCHAR(35) CHECK(locatiON IN ('Mumbai', 'Delhi'))
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
    phONe_no INT(11) NOT NULL,
    department VARCHAR(40) NOT NULL,
    manager_id INT(5)
);

INSERT INTO products VALUES(1, 'HP Laptop', 70000, 10, 'Mumbai');
INSERT INTO products VALUES(2, 'Realme Mobile', 20000, 5, 'Delhi');
INSERT INTO products VALUES(3, 'Realme EarphONes', 1000, 15, 'Mumbai');
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

COMMIT

ROLLBACK

SAVEPOINT a;

ROLLBACK TO a;

DELIMITER //
CREATE TRIGGER products_after_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
  INSERT INTO product_log (pid, pname, price, stock, locatiON, inserted_at)
  VALUES (NEW.pid, NEW.pname, NEW.price, NEW.stock, NEW.locatiON, NOW());
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER orders_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE products
  SET stock = stock - 1
  WHERE pid = NEW.pid;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER products_after_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  IF OLD.pid <> NEW.pid OR OLD.pname <> NEW.pname OR OLD.price <> NEW.price OR OLD.stock <> NEW.stock OR OLD.locatiON <> NEW.locatiON THEN
    INSERT INTO product_log (pid, pname, price, stock, locatiON, updated_at)
    VALUES (OLD.pid, OLD.pname, OLD.price, OLD.stock, OLD.locatiON, NOW());
  END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER products_after_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
  DECLARE hAS_orders INT DEFAULT (0);
  SELECT COUNT(*) INTO hAS_orders
  FROM orders
  WHERE pid = OLD.pid;

  IF hAS_orders > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete product with existing orders. Update or delete orders first.';
  END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER set_default_payment_STATUS
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
  IF NEW.STATUS IS NULL THEN
    SET NEW.STATUS = 'Pending';
  END IF;
END //
DELIMITER ;

CREATE OR REPLACE VIEW active_customers_mumbai AS
SELECT c.cid, c.cname, c.addr
FROM customer c
WHERE c.age > 25 AND c.addr LIKE '%Mumbai%';

CREATE VIEW CustomerOrders AS
SELECT c.cid, c.cname, o.oid, o.amt, p.pname
FROM customer c
JOIN orders o ON c.cid = o.cid
JOIN products p ON o.pid = p.pid;

CREATE VIEW TotalOrdersByLocatiON AS
SELECT p.locatiON, p.pname, count(o.oid) AS total_orders
FROM products p
JOIN orders o ON p.pid = o.pid
GROUP BY p.locatiON, p.pname;

CREATE VIEW OrderPaymentSTATUS AS
SELECT o.oid, o.amt, p.MODE, p.STATUS
FROM orders o
JOIN payment p ON o.oid = p.oid;

DROP VIEW active_customers_mumbai;

DROP VIEW TotalOrdersByLocatiON;

