import sqlite3

class database(object):
    db_name = "artgallery.db"
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect(self.db_name
                                        , detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
        self.db_cur = self.connection.cursor()
        try:
            self.db_cur.execute("SELECT * FROM artist")
        except:
            self.db_cur.execute("""CREATE TABLE artist(  
                id int NOT NULL PRIMARY KEY,
                name VARCHAR(100),
                genre VARCHAR(30),
                birth YEAR,
                death YEAR, 
                nationality VARCHAR (30)
                );""")
        else:
            try:
                self.db_cur.execute("SELECT * FROM paintings")
            except:
                self.db_cur.execute("""CREATE TABLE paintings(  
                    id int NOT NULL PRIMARY KEY,
                    artist_ID INT
                    painting BLOB,
                    FOREIGN KEY (artist_ID) REFERENCES artist (id)
                );""")
        
    def __del__(self):
        self.connection.close()