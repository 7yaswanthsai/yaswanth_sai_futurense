--ARITHMETIC OPERAORS
SELECT 4+3;
SELECT 4-3;
SELECT 2*3;
SELECT 18/2;
SELECT 18%2;

--COMPARISON OPERATORS
SELECT 7=7;
SELECT 10>5;
SELECT 5<8;
SELECT 5>=5;
SELECT 3<=4;
SELECT 3<>3;

--BITWISE OPERATORS
SELECT 6 & 8;
SELECT 9 | 5;
SELECT 5 ^ 6;

--LOGICAL OPERATORS
SELECT 4!=6 AND 15>5;
SELECT 5>4 OR 10=9;
SELECT NOT 5<7;
SELECT 7 BETWEEN 2 AND 15;

--EXAMPLE
SELECT SUM(price) AS total_revenue 
FROM products;

SELECT * 
FROM customer 
WHERE age != 30;

SELECT * 
FROM payment 
WHERE mode != 'upi' 
AND status = 'completed';