-- SQLite
-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;

-- SELECT * FROM classmates;

-- LIMIT & OFFSET
-- SELECT * FROM classmates LIMIT 2;  -- 앞에서 두개만
-- SELECT * FROM classmates LIMIT 1 OFFSET 2;  -- 앞에 두개 띄고 한개만
-- SELECT * FROM classmates LIMIT 50 OFFSET 50  -- 앞에 두개 띄고 한개만

-- WHERE
-- SELECT * FROM classmates WHERE name='김탁희';
-- SELECT * FROM classmates WHERE address='대전' LIMIT 1;

-- DISTINCT
SELECT DISTINCT age FROM classmates;



