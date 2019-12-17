-- CREATE DATABASE - USER - PASSWORD - ASSIGN PRIVILEGES - FLUSH
-- db = hbnb_dev_db
-- new user hbnb_dev @ localhost
-- hbnb_dev password = hbnb_dev_pwd
-- all priv in db and select priv perform schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
