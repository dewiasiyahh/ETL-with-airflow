SELECT
    MD5(RAND()),  -- Generate a random name (MD5 hash)
    CASE WHEN RAND() < 0.5 THEN 'Dog' ELSE 'Cat' END,  -- Randomly assign 'Dog' or 'Cat'
    DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 100) DAY),  -- Random birth date (within the last 100 days)
    MD5(RAND())  -- Generate a random owner name (MD5 hash)
FROM
    (SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5) AS dummy
LIMIT 100;