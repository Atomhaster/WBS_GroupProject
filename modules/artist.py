class artist():
    def __init__(self, path):
        self.path = path
    
    def get_artist(self, id_artist):
        statement = f"SELECT * FROM artist Where id_artist={id_artist}"
        self.curser.execute(statement)
    
    def delete_artist(self, id_artist):
        statement = f"DELETE * FROM artist Where id_artist={id_artist}"

    def insert_data(self,a,b,c,d,e):
        query= f"""Insert into artist (name, genre, birth, death, nationality)
        VALUES ('{a}','{b}', '{c}', '{d}','{e}');"""
        
    def __eq__(self, __o: object) -> bool:
        if self.name == __o.name:
            return True
        else: return False
        