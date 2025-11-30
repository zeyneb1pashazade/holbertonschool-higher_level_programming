-- Creates the database 'hbtn_0d_2' and the user 'user_0d_2' with read-only privileges.
-- Both creation statements use IF NOT EXISTS to prevent script failure if they already exist.

-- 1. Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. Create the user 'user_0d_2' on localhost with the required password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- 3. Grant only SELECT privileges on the hbtn_0d_2 database to the new user.
-- The user is implicitly granted USAGE on *.* upon creation.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- 4. Apply the changes immediately
FLUSH PRIVILEGES;
