-- Go to UTF8, converts a database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- use hbtn_0c_0 database
USE hbtn_0c_0;
-- Converts hbtn_0c_0 database to UTF8
ALTER DATABASE
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts frist_table Table to UTF8
ALTER TABLE first_table
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts field name in frist_table Table to UTF8
ALTER TABLE first_table CONVERT TO
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 