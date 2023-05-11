import sqlite3
import numpy
import io

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
                nationality VARCHAR (30),
                number_of_paintings INT
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
        
    def add_artist(self, name, genre, birth, death, nationality, num_paintings):
        sql = """INSERT INTO artist(name, genre, birth, death, nationality, number_of_paintings)
                VALUES (:name, :genre, :birth, :death, :nationality, :num_paintings)"""
        data = {"name": name, "genre": genre
                , "birth": birth, "death": death
                , "nationality": nationality, "num_paintings": num_paintings}
        self.query(sql, data)
        self.connection.commit()
    
    def add_painting(self, painting: numpy.ndarray, artist):
        def adapt_array(arr):
            out = io.BytesIO()
            numpy.save(out, arr)
            out.seek(0)
            return sqlite3.Binary(out.read())
        artist_id = self.get_artist_id(artist)[0][0]
        size_width = painting.shape[1]
        size_height = painting.shape[0]
        painting_blob = adapt_array(painting)
        sql = """INSERT INTO painting(artist_id, size_width, size_height, painting)
                VALUES (:artist_id, :size_width, :size_height, :painting)"""
        data = {"artist_id" : artist_id
                , "size_width" : size_width
                , "size_height" : size_height
                , "painting" : painting_blob}
        self.query(sql, data)
        self.connection.commit()
    
    def get_painting(self, id_pic) -> tuple[int,str,int,int,numpy.ndarray]:
        def convert_array(text):
            out = io.BytesIO(text)
            out.seek(0)
            return numpy.load(out)
        statement = f"SELECT * FROM painting WHERE id = {id_pic}"
        self.db_cur.execute(statement)
        output = self.db_cur.fetchall()
        output[0] = output[0][:-1] + (convert_array(output[0][4]),)
        return output[0]

    def get_artist(self, id_art):
        statement = f"SELECT * FROM artist WHERE id = {id_art}"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()
    
    def get_artist_id(self, artist_name):
        statement = f"SELECT id FROM artist WHERE name = '{artist_name}'"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()
    
    def get_allartists(self):
        statement = f"SELECT * FROM artist"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()

    def delete_Artist(self, ):
        # delted artist from db
        pass