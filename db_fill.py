import os
import matplotlib.pyplot as plt
import modules.database as db
import csv

# absolute path where the picture archive from best art work of all time was unzipped
FOLDER_PATH = "C:/Users/bvondewitz/Downloads/archive"

# list of available artists
ARTISTS = {}

# to just display an image use: 
# img = mpimg.imread( FOLDER_PATH + '/images/images/Amedeo_Modigliani/Amedeo_Modigliani_2.jpg')
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
# checking the folder content of the archive

ARTISTS = get_all_artist_names()

number_paintings = list_num_paintings()
# print(number_paintings)

# for i in number_paintings.items():
#     if i[1] > 200:
#         print(f"{i[0]}\t\t{i[1]}")

#  artists with more than 200 paintings available   
#  Alfred_Sisley           259
#  Edgar_Degas             702
#  Francisco_Goya          291
#  Marc_Chagall            239
#  Pablo_Picasso           439
#  Paul_Gauguin            311
#  Pierre-Auguste_Renoir   336
#  Rembrandt               262
#  Titian                  255
#  Vincent_van_Gogh        877



#_______________________________________________________________________________________
#  getting the artists infos from the excel file. I've removed the wiki columns from
#  the file and saved it again with excel. the delimiter therefore changed to ";"

# reading all content of the csv
csv_content = {}
with open(FOLDER_PATH + "/artists_small.csv") as f_csv:
    reader = csv.reader(f_csv, delimiter=";")
    for zeile in reader:
        csv_content[zeile[1]] = (zeile[2][:4], zeile[2][-4:]
                                 , zeile[3], zeile[4], zeile[5])

# deleting the first row with column names
del csv_content["name"]

# selecting only rows with more than 200 paintings and not Albrecht Dürer
csv_content_selected = {}
for j, i in csv_content.items():
    if int(i[4]) > 200 and not j.startswith("Albrecht"):
        csv_content_selected[j] = i



#_______________________________________________________________________________________
#  adding the remaining artists to the database

# making the object of out type database
gallery = db.database()

# adding all artists to the database
# for j, i in csv_content_selected.items():
#     gallery.add_artist(
#         j, i[2], i[0], i[1], i[3], i[4]
#     )
    
# checking if artists are in database
# all_artist_db = gallery.get_allartists()
# print(all_artist_db)


#_______________________________________________________________________________________
#  adding the pictures of the remaining artists to the database

# for name in csv_content_selected.keys():
#     print("adding paintings of: " + name)
#     name_underscore = name.replace(" ", "_")
#     file_names = get_all_filenames(name_underscore)
#     print(len(file_names), " paintings found")
#     for paint in file_names:
#         ###  with the original image files, the database is getting 12 GB big. ###
#         # full_path = FOLDER_PATH + "/images/images/" + name_underscore + "/" + paint
#         ###   resized images still big with 4.5 GB.
#         full_path = FOLDER_PATH + "/resized/resized/" + paint
#         im = plt.imread(full_path)
#         gallery.add_painting(im, name)
#         print("+", end=" ")
#     print("\n")
    
## check how many paintings are in the db:
count_all_paintings = gallery.query("SELECT COUNT(id) FROM painting", ())
print(count_all_paintings) # 3971
