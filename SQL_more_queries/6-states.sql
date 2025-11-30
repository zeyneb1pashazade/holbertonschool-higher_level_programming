-- Creates the database 'hbtn_0d_usa' and the table 'states' within it.

-- 1. Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Switch to the new database
USE hbtn_0d_usa;

-- 3. Create the 'states' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    -- id: INT, unique, auto generated, cannot be null, and is the primary key
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    -- name: VARCHAR(256), cannot be null
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
