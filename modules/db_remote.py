import pyodbc


class db_azure(object):
    
    def __init__(self, constring) -> None:
        self.conn = pyodbc.connect(constring)
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

if __name__ == "__main__":
    pass
    
    server = 'artistrecognition.database.windows.net'
    DSN = "Azure_DB"
    admin_user = "sqluser"
    admin_pwd = r"ghUZ6%lop§$f"   
    driver= 'SQL Server'
    grouplogin = "huZGu6732eju89"
    group_user= "group_user"
    database = "artgallery"
    query = ""

    con_string_master = ('DSN=' + DSN + ";UID=" + admin_user + ";PWD=" + admin_pwd)
    con_string_DSN_default = ('DSN=' + DSN)
    con_string_db = ('DSN=' + DSN + ";UID=" + admin_user + ";PWD=" + admin_pwd
                     + ";DATABASE=" + database)
    con_string_db_group_user = ('DSN=' + DSN + ";UID=" + group_user + ";PWD=" + grouplogin
                     + ";DATABASE=" + database)
    con_string_master_groupuser = ('DSN=' + DSN + ";UID=" + group_user 
                                   + ";PWD='" + grouplogin + "'")
    
    # print(con_string_db)

    # connection with DSN default:
    # db = db_azure(con_string_DSN_default) # not working. User not passed through
    # connection with master db:
    # db = db_azure(con_string_master)
    # connection with artgallery db:
    # db = db_azure(con_string_db)
    # with group_user
    db = db_azure(con_string_db_group_user)
    # master with group_user
    # db = db_azure(con_string_master_groupuser)
        
    # see user and their roles
    # db.check_permissions(True)
    
    # querys:
    # query = "SELECT CURRENT_USER"
    query = "SELECT DB_NAME()"
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
    
    # params:
    parameters = ()
    if query:
        db.query(query,parameters, True)







            
            # cursor.execute(f"CREATE USER group_user for login grouplogin")
            # cursor.execute("GRANT INSERT ON artgallery TO sqluser")
            # cursor.execute("SELECT DB_NAME()")
            # cursor.execute("SELECT name, database_id, create_date FROM sys.databases")
            # cursor.execute("CREATE TABLE artist(id int NOT NULL PRIMARY KEY, name VARCHAR(100))")
            # cursor.execute("INSERT INTO artist(name) VALUES ('Horstguenter')")
            # cursor.execute("SELECT * FROM artist")