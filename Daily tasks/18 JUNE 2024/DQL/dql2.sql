SELECT DISTINCT cname,addr FROM customer;

SELECT * FROM orders;

SELECT * FROM customer WHERE cname LIKE "%Ra%";
SELECT * FROM customer WHERE cname LIKE "Ra%";
SELECT * FROM customer WHERE cname LIKE "%vi";

SELECT cid,
	   cname,
       CASE WHEN cid > 102 THEN 'Pass' ELSE 'Fail' END AS 'Remark'
FROM customer;

SELECT cid,
	   cname,
       IF(cid > 102, 'Pass', 'Fail')AS 'Remark'
FROM customer;

SELECT * 
FROM customer
ORDER BY cid
LIMIT 2;

SELECT * FROM customer WHERE cname = "Ravi";