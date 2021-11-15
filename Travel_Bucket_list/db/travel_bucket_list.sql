DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INT,
  favourite_country VARCHAR(255),
);

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  city VARCHAR(255),
  population iNT,
  currency VARCHAR(255),
  language VARCHAR(255),
  visited BOOLEAN,
  user_id INT REFERENCES users(id)
);
