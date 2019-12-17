--CREATE DATABASE - USER - PASSWORD - ASSIGN PRIVILEGES - FLUSH                               -- db = hbnb_test_db 
-- user - hbnb_test @ localhost
-- hbnb_test password = hbnb_test_pwd
-- hbnb_test all priv in db hbnb_test_db && select priv on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;

