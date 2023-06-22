import pyodbc, numpy, io, pyodbc, random

class db_azure(object):
    SERVER = 'artistrecognition.database.windows.net'
    DSN = "Azure_DB"
    admin_user = "sqluser"
    admin_pwd = r"ghUZ6%lop§$f"
    database = "artgallery"
    con_string_db = ('DSN=' + DSN + ";UID=" + admin_user + ";PWD=" + admin_pwd
                     + ";DATABASE=" + database)
    
    def __init__(self, constring="") -> None:
        if constring:
            self.conn = pyodbc.connect(constring)
        else:
            self.conn = pyodbc.connect(self.con_string_db)
        self.cursor = self.conn.cursor()
        
    def __del__(self):
        self.conn.close()
        
    def query(self, query, params, print_out=False):
        self.cursor.execute(query, params)
        if not query.startswith("SELECT"):
            self.cursor.commit()
        else:
            answer = self.cursor.fetchall()
            if print_out:
                for row in answer:
                    print(row)
            else:
                return answer
                
    def check_permissions(self, print_out=False):
        query_temp = """SELECT DISTINCT pr.principal_id, pr.name, pr.type_desc, 
                    pr.authentication_type_desc, pe.state_desc, pe.permission_name
                    FROM sys.database_principals AS pr
                    JOIN sys.database_permissions AS pe
                    ON pe.grantee_principal_id = pr.principal_id;"""
        self.query(query_temp,(), True)
        
    def create_table_artist(self):
        temp_q = """CREATE TABLE artist(  
                    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
                    name VARCHAR(100),
                    genre VARCHAR(30),
                    birth INT,
                    death INT, 
                    nationality VARCHAR (30),
                    number_of_paintings INT
                );"""
        try:
            self.query(temp_q, ())
        except Exception as ex:
            print(f"could not create table artist: Message {str(ex)}")
            
    def create_table_painting(self):
        temp_q = """CREATE TABLE painting(  
                    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
                    artist_ID INT,
                    size_width INT,
                    size_height INT,
                    painting IMAGE,
                    FOREIGN KEY (artist_ID) REFERENCES artist (id)
                );"""
        try:
            self.query(temp_q, ())
        except Exception as ex:
            print(f"could not create table artist: Message {str(ex)}")
            
    def drop_all(self):
        self.query("DROP TABLE painting", ())
        self.query("DROP TABLE artist", ())
        
    def add_artist(self, name, genre, birth, death, nationality, num_paintings):
        data = (name, genre, birth, death, nationality, num_paintings)
        sql = """INSERT INTO artist(name, genre, birth, death, nationality, number_of_paintings)
            VALUES (?,?,?,?,?,?)"""
        self.query(sql, data)
        
    def get_artist(self, id_art):
        return self.query(f"SELECT * FROM artist WHERE id = {id_art}",())[0]
        
    def get_artist_id(self, artist_name):
        return self.query(f"SELECT id FROM artist WHERE name = '{artist_name}'",())[0][0]
    
    def get_all_artists(self):
        return self.query("SELECT * FROM artist", ())
        
    def add_painting(self, painting: numpy.ndarray, artist):
        def adapt_array(arr):
            out = io.BytesIO()
            numpy.save(out, arr)
            out.seek(0)
            return pyodbc.Binary(out.read())
        artist_id = self.get_artist_id(artist)
        size_width = painting.shape[1]
        size_height = painting.shape[0]
        painting_blob = adapt_array(painting)
        sql = """INSERT INTO painting(artist_id, size_width, size_height, painting)
                VALUES (?,?,?,?)"""
        data = (artist_id, size_width, size_height, painting_blob)
        self.query(sql, data)
    
    def get_painting(self, id_pic) -> tuple[int,str,int,int,numpy.ndarray]:
        def convert_array(text):
            out = io.BytesIO(text)
            out.seek(0)
            return numpy.load(out)
        statement = f"SELECT * FROM painting WHERE id = {id_pic}"
        self.cursor.execute(statement)
        output = self.cursor.fetchall()
        output[0] = output[0][:-1] + (convert_array(output[0][4]),)
        return output[0]
    
    def get_max_painting_id(self):
        return self.query("SELECT MAX(id) FROM painting", ())[0][0]
    
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
            
    def get_paintingids_from_artist(self, artist_id):
        return self.query(f"SELECT ID FROM painting WHERE artist_id = {artist_id}", ())

if __name__ == "__main__":
    
    db = db_azure()
    # to build database up:
    # db.create_table_artist()
    # db.create_table_painting()
    # db.drop_all()
    # db.add_artist("Frida Kahlo","Primitivism,Surrealism", "1907", "1954","Mexican", "120")
    
    # print(db.get_artist_id("Frida Kahlo"))
    
    import matplotlib.pyplot as plt
    # image_path = "C:/Users/bvondewitz/Downloads/archive/resized/resized/Frida_Kahlo_58.jpg"
    # im = plt.imread(image_path)
    # imgplot = plt.imshow(im)
    # plt.show()
    # db.add_painting(im, "Frida Kahlo")
    # for driver in pyodbc.drivers():
    #     print(driver)
    # painting_rec = db.get_painting(1)
    # print(type(painting_rec[4]))
    # imgplot = plt.imshow(painting_rec[4])
    # plt.show()
    
    
    im = db.get_random_painting("Pablo Picasso")[4]
    # print(type(im))
    imgplot = plt.imshow(im)
    plt.show()
    # print(db.get_max_painting_id())
    
    # server = 'artistrecognition.database.windows.net'
    # DSN = "Azure_DB"
    # admin_user = "sqluser"
    # admin_pwd = r"ghUZ6%lop§$f"   
    # driver= 'SQL Server'
    # grouplogin = "huZGu6732eju89"
    # group_user= "group_user"
    # database = "artgallery"
    # query = ""

    # con_string_master = ('DSN=' + DSN + ";UID=" + admin_user + ";PWD=" + admin_pwd)
    # con_string_DSN_default = ('DSN=' + DSN)
    # con_string_db = ('DSN=' + DSN + ";UID=" + admin_user + ";PWD=" + admin_pwd
    #                  + ";DATABASE=" + database)
    # con_string_db_group_user = ('DSN=' + DSN + ";UID=" + group_user + ";PWD=" + grouplogin
    #                  + ";DATABASE=" + database)
    # con_string_master_groupuser = ('DSN=' + DSN + ";UID=" + group_user 
                                #    + ";PWD='" + grouplogin + "'")
    
    # print(con_string_db)

    # connection with DSN default:
    # db = db_azure(con_string_DSN_default) # not working. User not passed through
    # connection with master db:
    # db = db_azure(con_string_master)
    # connection with artgallery db:
    # db = db_azure(con_string_db)
    # with group_user
    # db = db_azure(con_string_db_group_user)
    # master with group_user
    # db = db_azure(con_string_master_groupuser)
        
    # see user and their roles
    # db.check_permissions(True)
    
    # querys:
    # query = "SELECT CURRENT_USER"
    # query = "SELECT DB_NAME()"
    # get infos about existing databases
    # query = """SELECT [name] as database_name,
    #         database_id,
    #         create_date
    #         from sys.databases 
    #         order by name"""
    
    # get all schemas existing
    # query = """SELECT s.name as schema_name,
    #     	    s.schema_id, u.name as schema_owner
    #             from sys.schemas s
    #             inner join sys.sysusers u
    #             on u.uid = s.principal_id
    #             order by s.name"""
    
    
    # add User object
    # query = "CREATE login grouplogin with password = 'huZGu6732eju89'"
    # query = "SELECT * FROM sys.sql_logins"
    # query = """CREATE USER group_user for login grouplogin WITH DEFAULT_SCHEMA=dbo;"""
    # query = "ALTER ROLE db_owner ADD MEMBER group_user;"
    # query = "GRANT ALL TO group_user;"
    # query = "GRANT ALL TO db_owner;"

    
    # drop login object
    # query = "DROP LOGIN grouplogin"
    
    # delete USER
    # query = "DROP USER " + group_user
    
    # query = "SELECT name, database_id, create_date FROM sys.databases"
    # query = "CREATE TABLE artist(id int NOT NULL PRIMARY KEY, name VARCHAR(100))"
    # query = "INSERT INTO artist(name) VALUES ('Horstguenter')"
    
    # params:
    # parameters = ()
    # if query:
    #     db.query(query,parameters, True)