import db_remote as db
import random

class painting():
    
    def __init__(self, id=0, artist_name="", artist_id=0) -> None:
        gallery = db.db_azure()
        db_entry = ()
        if id:
            db_entry = (gallery.get_painting(id))
        elif artist_name:
            art_id = gallery.get_artist_id(artist_name)
            print(art_id)
        elif artist_id:
            print("art.id given")
        else:
            print("random picture")
            
        # self.id = db_entry[0]
        # self.artist_id = db_entry[1]
        # self.size_width = db_entry[2]
        # self.size_height = db_entry[2]
        # self.ndarray = db_entry[4]
        
    
    def get_pic(self, id_pic):
        statement = f"SELECT * FROM painting Where {id_pic}"
        self.curser.execute(statement)
    
    def get_artist(self, id_art):
        statement = f"SELECT * FROM artist Where {id_art}"
        self.curser.execute(statement)
    
    def delete_Artist(self):
        # delted artist from db
        pass
    def blurr_image(self):
        # blurring the image
        pass
    def rescale_image(self):
        pass
        # rescale the image that is given
    
    def flip_image(self):
        pass
        # flip the image to identify different variations
        


if __name__ == "__main__":
    test_painting = painting(artist_name="Marc Chagall")
    print(test_painting.artist_id)