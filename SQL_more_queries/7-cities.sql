-- Creates the database 'hbtn_0d_usa' and the table 'cities' within it.
-- This script uses a FOREIGN KEY to link cities to states.

-- 1. Create the database if it doesn't already exist (safe creation)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Switch to the new database
USE hbtn_0d_usa;

-- 3. Create the 'cities' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    -- id: INT, unique, auto generated, cannot be null, and is the primary key
    id INT UNIQUE NOT NULL AUTO_INCREMENT,

    -- state_id: INT, cannot be null, and must reference the 'states' table
    state_id INT NOT NULL,

    -- name: VARCHAR(256), cannot be null
    name VARCHAR(256) NOT NULL,

    -- Define the Primary Key
    PRIMARY KEY (id),

    -- Define the Foreign Key constraint
    -- This links the 'state_id' column in this table to the 'id' column in the 'states' table.
    FOREIGN KEY (state_id) REFERENCES states(id)
);
