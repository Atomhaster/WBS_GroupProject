import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import modules.database as db

# absolute path where the picture archive from best art work of all time was unzipped
FOLDER_PATH = "C:/Users/bvondewitz/Downloads/archive"

# list of available artists
ARTISTS = {}

# img = mpimg.imread('C:/Users/bvondewitz/Downloads/archive/images/images/Amedeo_Modigliani/Amedeo_Modigliani_2.jpg')
# imgplot = plt.imshow(img)
# plt.show()

def get_all_filenames(artist) -> list:
    global FOLDER_PATH
    path_temp = FOLDER_PATH + f"/images/images/{artist}"
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path_temp):
        f.extend(filenames)
    return f

def get_all_artist_names():
    """returns all artists having a folder. I've exlcuded Albrecht Dürer"""
    global FOLDER_PATH
    path_temp = FOLDER_PATH + f"/images/images"
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path_temp):
        f.extend(dirnames)
    i = 0
    dic = {}
    for artist in f:
        if not artist.startswith("Albrecht_"):
            dic[i] = artist
            i += 1
    return dic

def get_num_paintings(artist):
    files = get_all_filenames(artist)
    return len(files)

def list_num_paintings():
    global ARTISTS
    out = {}
    for ar in ARTISTS.values():
        out[ar] = get_num_paintings(ar)
    return out
    

#______________________________________________________________________________________


ARTISTS = get_all_artist_names()

number_paintings = list_num_paintings()
# print(number_paintings)

for i in number_paintings.items():
    if i[1] > 300:
        print(f"{i[0]}\t\t{i[1]}")

gallery = db.database()
