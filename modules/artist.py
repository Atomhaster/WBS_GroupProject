import db_remote as db

class artist():
    
    def __init__(self, id=0, fullname=""):
        gallery_con = db.db_azure()
        if fullname:
            id = gallery_con.get_artist_id(fullname)
        db_entry = gallery_con.get_artist(id_art=id)
        
        self.id = db_entry[0]
        self.name = db_entry[1]
        self.genre = db_entry[2]
        self.birth = db_entry[3]
        self.death = db_entry[4]
        self.nationality = db_entry[5]
        self.num_paintings = db_entry[6]
        
        
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
        
        
if __name__ == "__main__":
    test_artist = artist(id = 10)
    test_artist1 = artist(id = 10)
    print(test_artist.__dict__)
    print(test_artist == test_artist1)