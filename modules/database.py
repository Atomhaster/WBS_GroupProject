import sqlite3
import numpy
import io
import random

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
    
    def drop_all(self):
        self.query("DROP TABLE painting", ())
        self.query("DROP TABLE artist", ())
        
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
        artist_id = self.get_artist_id(artist)
        size_width = painting.shape[1]
        size_height = painting.shape[0]
        painting_blob = adapt_array(painting)
        print(artist)
        print(artist_id)
        sql = """INSERT INTO painting(artist_id, size_width, size_height, painting)
                VALUES (:artist_id, :size_width, :size_height, :painting)"""
        data = {"artist_id" : artist_id
                , "size_width" : size_width
                , "size_height" : size_height
                , "painting" : painting_blob}
        self.query(sql, data)
        self.connection.commit()
    
    def get_painting(self, id_pic) -> tuple[int,int,int,int,numpy.ndarray]:
        def convert_array(text):
            out = io.BytesIO(text)
            out.seek(0)
            return numpy.load(out)
        statement = f"SELECT * FROM painting WHERE id = {id_pic}"
        self.db_cur.execute(statement)
        output = self.db_cur.fetchall()
        output[0] = output[0][:-1] + (convert_array(output[0][4]),)
        return output[0]
    
    def get_random_painting(self, artist_name="", artist_id=0):
        if not artist_name and not artist_id:
            max_id = self.get_max_painting_id()
            painting_id = random.randint(1, max_id)
        else:
            if artist_name:
                artist_id = self.get_artist_id(artist_name)
            p_ids = self.get_paintingids_from_artist(artist_id)
            painting_id = random.randint(min(p_ids)[0], max(p_ids)[0])
        return self.get_painting(painting_id)
    
    def get_max_painting_id(self):
        return self.query("SELECT MAX(id) FROM painting", ())[0][0]
    
    def get_artist(self, id_art):
        statement = f"SELECT * FROM artist WHERE id = {id_art}"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()[0]
    
    def get_artist_id(self, artist_name):
        statement = f"SELECT id FROM artist WHERE name = '{artist_name}'"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()[0][0]
    
    def get_all_artists(self):
        statement = f"SELECT * FROM artist"
        self.db_cur.execute(statement)
        return self.db_cur.fetchall()
    
    def get_paintingids_from_artist(self, artist_id):
        return self.query(f"SELECT ID FROM painting WHERE artist_id = {artist_id}", ())
    
if __name__ == "__main__":
    gallery = database()
    # painting = gallery.get_painting(265)
    # for i in painting[:4]:
    #     print(i)
    #     print(type(i))
    class_names = [i[1] for i in gallery.get_all_artists()]
    print(class_names)
    # count_all_paintings = gallery.query("SELECT COUNT(id) FROM painting", ())
    # print(count_all_paintings[0][0]) # 3971
    # print(gallery.get_max_painting_id())
    