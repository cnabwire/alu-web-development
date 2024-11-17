-- Query to list all privileges (GRANT) of the MySQL users
-- Check privillages for user_0d_1
SELECT CONCAT('Grants for user_0d_1@localhost') AS '';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check privillages for user_0d_2
SELECT CONCAT('Grants for user_0d_2@localhost') AS '';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
