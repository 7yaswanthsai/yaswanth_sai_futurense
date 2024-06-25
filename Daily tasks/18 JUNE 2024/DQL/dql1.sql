USE amazon

--GROUPBY USED FOR GROUPING ROWS WITH SAME VALUES
SELECT cname, COUNT(*) AS Number
FROM customer
GROUP BY cname
HAVING Number >= 1;

SELECT location, GROUP_CONCAT(DISTINCT pname) AS product_names
FROM products
GROUP BY location;

--ORDER BY USED FOR ORDERING ROWS IN A SPECIFIC WAY
SELECT pid, pname, price
FROM products
ORDER BY price ASC;

SELECT cid, cname, age
FROM customer
ORDER BY age DESC;

--HAVING BY IS USED TO ALLOW THE FILTERING OF QUERY RESULTS BASED ON AGGREGATE FUNCTIONS AND GROUPINGS
SELECT pid, pname, stock
FROM products
GROUP BY pid, pname, stock
HAVING stock < 10;

SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location
HAVING SUM(stock) > 50;