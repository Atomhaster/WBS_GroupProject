# Tabelle artist erstellen
CREATE TABLE artist(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    name VARCHAR(100),
    genre VARCHAR(30),
    birth YEAR,
    death YEAR, 
    nationality VARCHAR (30)
) COMMENT '';

# Tabelle painitings erstellen
CREATE TABLE paintings(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    artist_ID INT,
    FOREIGN KEY (artist_ID) REFERENCES artist (id)
) COMMENT '';
