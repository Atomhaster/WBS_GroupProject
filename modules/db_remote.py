import pyodbc


server = 'groupwork-wbs.database.windows.net'
database = ''
DSN = "Azure_sql_DB"
username = "sqluser"
password = r"ghUZ6%lop§$f"   
driver= 'SQL Server'
grouplogin = "huzgue/!!ju89"
group_user= "group_user"
database = "Artgallery"

# print(('DSN=' + DSN + ";UID=" + username + ";PWD" + password))

with pyodbc.connect('DSN=' + DSN + ";UID=" + username 
                    + ";PWD=" + password + ";DATABASE=" + database) as conn:
    with conn.cursor() as cursor:
        # cursor.execute(f"CREATE login grouplogin with password = '{grouplogin}'")
        # cursor.execute(f"CREATE USER group_user for login grouplogin")
        # cursor.execute("GRANT INSERT ON artgallery TO sqluser")
        # cursor.execute("SELECT DB_NAME()")
        # cursor.execute("SELECT name, database_id, create_date FROM sys.databases")
        # cursor.execute("CREATE TABLE artist(id int NOT NULL PRIMARY KEY, name VARCHAR(100))")
        # cursor.execute("INSERT INTO artist(name) VALUES ('Horstguenter')")
        # cursor.execute("SELECT * FROM artist")
        # conn.commit()
        cursor.execute("SELECT CURRENT_USER")
        # cursor.execute("""SELECT DISTINCT pr.principal_id, pr.name, pr.type_desc, 
        #         pr.authentication_type_desc, pe.state_desc, pe.permission_name
        #     FROM sys.database_principals AS pr
        #     JOIN sys.database_permissions AS pe
        #     ON pe.grantee_principal_id = pr.principal_id;""")
        for row in cursor.fetchall():
            print(row)


    
if __name__ == "__main__":
    pass
    
    