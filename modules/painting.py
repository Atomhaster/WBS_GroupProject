import modules.db_remote as db_remote
import modules.database as db_local

class painting():
    
    def __init__(self, db_type, id=0, **args) -> None:
        if db_type == "remote DB":
            gallery = db_remote.db_azure()
        elif db_type == "local DB":
            gallery = db_local.database()
        else:
            print("value of argument db_type not recognized."
                    + " Try 'remote DB' or 'local DB' insted")
            return False
        db_entry = ()
        if id:
            db_entry = gallery.get_painting(id)
        else:
            db_entry = gallery.get_random_painting(**args)
            
        self.id = db_entry[0]
        self.artist_id = db_entry[1]
        self.size_width = db_entry[2]
        self.size_height = db_entry[3]
        self.ndarray = db_entry[4]
    
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
    import database as db_local
    import db_remote as db_remote
    test_painting = painting("local DB",id=2409)
    print(type(test_painting.artist_id))
    
    import matplotlib.pyplot as plt
    imgplot = plt.imshow(test_painting.ndarray)
    plt.show()