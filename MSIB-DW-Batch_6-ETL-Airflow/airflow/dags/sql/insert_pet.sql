INSERT INTO pet (name, pet_type, birth_date, owner)
SELECT
    md5(random()::text),          -- Generate a random name (MD5 hash)
    CASE WHEN random() < 0.5 THEN 'Dog' ELSE 'Cat' END,  -- Randomly assign 'Dog' or 'Cat'
    NOW() - '1 day'::INTERVAL * (RANDOM()::int * 100),  -- Random birth date (within the last 100 days)
    md5(random()::text)           -- Generate a random owner name (MD5 hash)
FROM generate_series(1, 100);
