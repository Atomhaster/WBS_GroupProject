import sqlite3

class database(object):
    db_name = "artgallery.db"
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect(self.db_name
                                        , detect_types=sqlite3.PARSE_DECLTYPES |
                                        sqlite3.PARSE_COLNAMES)
        self.db_cur = self.connection.cursor()
        def create_table_painting():
            self.db_cur.execute("""CREATE TABLE painting(  
                    id INTEGER NOT NULL PRIMARY KEY,
                    artist_ID INT,
                    size_width INT,
                    size_height INT,
                    painting BLOB,
                    FOREIGN KEY (artist_ID) REFERENCES artist (id)
                );""")
        try:
            self.db_cur.execute("SELECT * FROM artist")
        except:
            self.db_cur.execute("""CREATE TABLE artist(  
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(100),
                genre VARCHAR(30),
                birth YEAR,
                death YEAR, 
                nationality VARCHAR (30)
                );""")
            create_table_painting()
        else:
            try:
                self.db_cur.execute("SELECT * FROM painting")
            except:
                create_table_painting()
                
    def __del__(self):
        self.connection.close()
    
    def query(self, query, params):
        self.db_cur.execute(query, params)
        return self.db_cur.fetchall()
        
    def add_artist(self, name, genre, birth, death, nationality):
        sql = """INSERT INTO artist(name, genre, birth, death, nationality)
                VALUES (:name, :genre, :birth, :death, :nationality)"""
        data = {"name": name, "genre": genre
                , "birth": birth, "death": death, "nationality": nationality}
        self.query(sql, data)
        self.connection.commit()
    
    def get_painting(self, id_pic):
        statement = f"SELECT * FROM painting WHERE id = {id_pic}"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()

    def get_artist(self, id_art):
        statement = f"SELECT * FROM artist WHERE id = {id_art}"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()
    
    def get_artist_id(self, artist_name):
        statement = f"SELECT id FROM artist WHERE name = {artist_name}"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()
    
    def get_allartists(self):
        statement = f"SELECT * FROM artist"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()

    def delete_Artist(self):
        # delted artist from db
        pass