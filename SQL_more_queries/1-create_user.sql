-- Creates the MySQL server user 'user_0d_1' on localhost
-- The IF NOT EXISTS clause ensures the script does not fail if the user already exists.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases and tables (*.*) to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applies the changes
FLUSH PRIVILEGES;
