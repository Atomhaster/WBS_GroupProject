import db_remote as db

class painting():
    
    def __init__(self, id=0, **args) -> None:
        gallery = db.db_azure()
        db_entry = ()
        if id:
            db_entry = gallery.get_painting(id)
        else:
            db_entry = gallery.get_random_painting(**args)
            
        self.id = db_entry[0]
        self.artist_id = db_entry[1]
        self.size_width = db_entry[2]
        self.size_height = db_entry[2]
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
    test_painting = painting(artist_name="Marc Chagall")
    print(test_painting.artist_id)
    
    import matplotlib.pyplot as plt
    imgplot = plt.imshow(test_painting.ndarray)
    plt.show()