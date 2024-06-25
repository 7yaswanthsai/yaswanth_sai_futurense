--UPDATE ANOMALY
UPDATE products
SET price = 50000
WHERE pid = 1;
SELECT * FROM products;

--DELETE ANOMALY
DELETE FROM products
WHERE pid = 5;
SELECT * FROM products;

--INSERTION ANOMALY
INSERT INTO orders (orderID, customerID, productID, quantity)
VALUES(10005, 106, 2, 1); 

--PRIMARY KEY
CREATE TABLE products
(
	pid INT(3) PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5),
    location VARCHAR(30) CHECK(location IN ('Mumbai', 'Delhi'))
);

ALTER TABLE products
ADD PRIMARY KEY (pid);

ALTER TABLE products 
DROP PRIMARY KEY;

--FOREIGN KEY
ALTER TABLE orders
ADD FOREIGN KEY (pid) REFERENCES products(pid)

ALTER TABLE products 
DROP FOREIGN KEY products_ibfl_1;


