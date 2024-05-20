SELECT 
    FLOOR(random() * 10 + 1) AS random_1_10
FROM generate_series(1, 100);