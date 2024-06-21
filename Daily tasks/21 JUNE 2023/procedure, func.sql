USE amazon

--DELIMITER
DELIMITER //
CREATE PROCEDURE select_all_products()
BEGIN
	SELECT * FROM products;
END //
DELIMITER;

CALL select_all_products();

DROP PROCEDURE select_all_products;

DELIMITER $$
CREATE FUNCTION get_total_revenue()
RETURNS INT
DETERMINISTIC 
BEGIN
DECLARE total_revenue INT; 
SELECT SUM(p.amount) INTO total_revenue
FROM payment p
INNER JOIN orders o ON p.oid = o.oid
WHERE p.status = 'completed';
RETURN total_revenue; 
END$$
DELIMITER ;

SELECT get_total_revenue();

DROP FUNCTION IF EXISTS get_total_revenue;

--IN
DELIMITER //
CREATE PROCEDURE get_product_details(IN product_id INT)
BEGIN
    SELECT * FROM products WHERE pid = product_id;
END //

CALL get_product_details(3);

--OUT
DELIMITER //
CREATE PROCEDURE get_product_count(OUT product_count INT)
BEGIN
    SELECT COUNT(*) INTO product_count FROM products;
END //

CALL get_product_count(@product_count);
SELECT @product_count as product_count;

--CURSOR(Cursors in SQL are used to retrieve and process rows one by one from the result set of a query)
--USER-DEFINED
DELIMITER //
DECLARE @customer_count INT;
SELECT @customer_count = COUNT(*)
FROM customer;
PRINT 'Number of customers: ' + CAST(@customer_count AS VARCHAR(10));
DELIMITER ;

--PREDEFINED
DELIMITER //
DECLARE @total_price INT;
SELECT @total_price = SUM(price)
FROM products
WHERE pname = 'HP Laptop';
PRINT 'Total price of all HP Laptops: ' + CAST(@total_price AS VARCHAR(20));
DELIMITER ;