CREATE USER IF NOT EXISTS 'pl_app_writer'@'localhost' IDENTIFIED BY 'strong_password';


GRANT
	SELECT,
    INSERT,
    UPDATE,
    DELETE,
    CREATE,
    ALTER,
    DROP
ON premier_league_db.* TO 'pl_app_writer'@'localhost';

SHOW DATABASES;
SELECT user, host FROM mysql.user;
SHOW GRANTS FOR 'pl_app_writer'@'localhost';
