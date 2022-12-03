
-- Creation of product table
CREATE TABLE IF NOT EXISTS user_info (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  password varchar(256) NOT NULL,
  salt varchar(256) NOT NULL
);