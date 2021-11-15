DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  population INT,
  currency VARCHAR(255),
  language VARCHAR(255)
);

CREATE TABLE cities (
  CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id),
    visited BOOLEAN
);