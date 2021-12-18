-- create the user user_0d_1 with password user_0d_1_pwd.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1_pwd@localhost;
