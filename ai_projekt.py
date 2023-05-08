# Hi an Alle




#Anna






#Hallo zurück


class datenbank():
    
    def __init__(self, path) -> None:
        path = path
    
    def get_pic(self, id_pic):
        statement = f"SELECT * FROM painting Where {id_pic}"
        self.curser.execute(statement)
    
    def get_artist(self, id_art):
        statement = f"SELECT * FROM artist Where {id_art}"
        self.curser.execute(statement)
    
    def delete_Artist(self):
        # delted artist from db
        pass
    
    