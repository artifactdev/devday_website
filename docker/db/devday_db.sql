\c template1
CREATE EXTENSION IF NOT EXISTS hstore;

CREATE USER devday PASSWORD 'devday';
CREATE DATABASE devday ENCODING 'UTF-8' TEMPLATE 'template1';
GRANT CREATE, CONNECT ON DATABASE devday TO devday;
ALTER USER devday CREATEDB;
