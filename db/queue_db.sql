CREATE DATABASE queue_db;
use queue_db;
CREATE TABLE sms_table (id INT PRIMARY KEY NOT NULL, message TEXT,origin VARCHAR(100),destination VARCHAR(100),time_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP );
CREATE TABLE sms_archive (id INT PRIMARY KEY NOT NULL, message TEXT,origin VARCHAR(100),destination VARCHAR(100),time_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP );