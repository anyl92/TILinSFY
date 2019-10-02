-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age = 30;
-- SELECT * FROM users WHERE age >= 30;

-- SELECT first_name FROM users WHERE age >= 30;

-- users에서 age 30이상, 성이 '김'인 사람의 성과 나이만 가져온다면?
-- SELECT age, last_name FROM users  
-- WHERE age >= 30 AND last_name = '김' 
-- LIMIT 10;

--COUNT
-- SELECT COUNT(id) FROM users;

-- AVG, SUM, MIN, MAX
-- 30살 이상인 사람들의 평균나이
-- SELECT AVG(age) FROM users
-- WHERE age >= 30;

-- users에서 잔액이 가장 높은 사람의 first_name과 잔액
-- SELECT first_name, MAX(balance) FROM users;

-- SELECT AVG(balance) FROM users
-- Where age >= 30;

--wild cards
-- SELECT * FROM users WHERE age LIKE '2_';
-- SELECT phone FROM users WHERE phone LIKE '02-%';
-- SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';
-- SELECT phone FROM users WHERE phone LIKE '%-5114-%';

--ORDER
-- SELECT age, first_name FROM users ORDER BY age DESC LIMIT 10;

-- SELECT age, balance FROM users
-- ORDER BY age, balance LIMIT 10;

-- SELECT age, last_name FROM users
-- ORDER BY last_name, age LIMIT 10;

SELECT last_name, first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;