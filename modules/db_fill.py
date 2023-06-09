import os
from pathlib import Path
import matplotlib.pyplot as plt
import csv
# import db_remote as db
import database as db


## comment use of this script:  ########################################################
##  download the archive from
## https://www.kaggle.com/code/supratimhaldar/deepartist-identify-artist-from-art
## change the FOLDER_PATH variable to the folder the unpacked archive is located
## import the artists.csv into excel. Delete the columns of bio and wikilink. 
## save the file again as csv. Change the value of artists_small if necessary

# absolute path where the picture archive from best art work of all time was unzipped
# FOLDER_PATH = "C:/Users/bvondewitz/Downloads/archive"
# setting path variable for Working Directory and  
WD_PATH =  os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
USER_DOWNLOAD =  os.path.join(Path.home(), "Downloads")
FOLDER_PATH = os.path.join(USER_DOWNLOAD, "archive")

# file name of the artists.csv with reduced columns
FILE_CSV = "artists_small.csv"

# list of available artists
ARTISTS = {}

# to just display an image use: 
# img = mpimg.imread( FOLDER_PATH + '/images/images/Amedeo_Modigliani/Amedeo_Modigliani_2.jpg')
# imgplot = plt.imshow(img)
# plt.show()


###_________________________________________________________________________________####

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
    path_temp = os.path.join(FOLDER_PATH ,"images\\images")
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

def print_artist_minpainting(minimum):
    number_paintings = list_num_paintings()
    print("Count available paintings")
    for i in number_paintings.items():
        if i[1] > minimum:
          print("{:<25}{}".format(i[0],i[1]))
          
def read_csv_artists_content(file, minimum = 0):
    csv_content = {}
    with open(WD_PATH + "\\DB_design\\" + file) as f_csv:
        reader = csv.reader(f_csv, delimiter=";")
        for zeile in reader:
            csv_content[zeile[1]] = (zeile[2][:4], zeile[2][-4:]
                                    , zeile[3], zeile[4], zeile[5])
    # deleting the first row with column names
    del csv_content["name"]
    # selecting only rows with more than the minimum and not Albrecht Dürer
    csv_content_selected = {}
    for j, i in csv_content.items():
        if int(i[4]) > minimum and not j.startswith("Albrecht"):
            csv_content_selected[j] = i
    return csv_content_selected


def add_artists_to_db(artists, gallery):
    for j, i in artists.items():
        gallery.add_artist(
            j, i[2], i[0], i[1], i[3], i[4]
        )
        
def add_pictures_to_db(artist_list, gallery, resized=False):
    for name in artist_list.keys():
        print("adding paintings of: " + name)
        name_underscore = name.replace(" ", "_")
        file_names = get_all_filenames(name_underscore)
        print(len(file_names), " paintings found")
        for paint in file_names:
            if resized:
                full_path = FOLDER_PATH + "/resized/resized/" + paint
            else:
                full_path = FOLDER_PATH + "/images/images/" + name_underscore + "/" + paint
            im = plt.imread(full_path)
            gallery.add_painting(im, name)
            print("+", end=" ")
        print("\n")
    
    

#______________________________________________________________________________________
# checking the folder content of the archive

ARTISTS = get_all_artist_names()

# print(ARTISTS)

# print_artist_minpainting(200)

#  artists with more than 200 paintings available   
#  Vincent_van_Gogh        877
#  Pablo_Picasso           439
#  Pierre-Auguste_Renoir   336
#  Francisco_Goya          291
#  Alfred_Sisley           259
#  Marc_Chagall            239
#  Edgar_Degas             702
#  Rembrandt               262
#  Titian                  255
#  Paul_Gauguin            311


#  getting the artists infos from the excel file. I've removed the wiki columns from
#  the file and saved it again with excel. the delimiter therefore changed to ";"
# reading content of the csv (needed for further steps)
csv_artists = read_csv_artists_content(FILE_CSV, 200)
# printing the list selected
# print("\n\n","content selected csv file \n")
# for i, j in csv_artists.items():
#     print("{:<25}{}".format(i,j))


#______________________________________________________________________
#  FROM HERE TWO POSSIBLE WAYS TO GO                                   
#______________________________________________________________________
#
#  There is the possibility to use this script to fill a remote DB
#  running in Azure with the db_remote module, or to create a local
#  db instance with a file the DB lives in, with the database module.
#  Bevor running the script comment out one of the possibilities.
#  Please also make sure you comment out the related import statement
#  at the very beginning of this script.


#_____________________________________________________________________________
##  POSSIBILITY 1  LOCAL DB   with sqlite3
#_____________________________________________________________________________

# making the object of our type database (holds also the connection to the db
#       needed for further steps)
# for local creation of DB use:
gallery = db.database()

# adding artists to db
# for j, i in csv_artists.items():
#     gallery.add_artist(
#         j, i[2], i[0], i[1], i[3], i[4]
#     )

# checking if artists are in database
# print("\nAll artists existing in db")
# all_artist_db = gallery.get_all_artists()
# for row in all_artist_db:
#     print(row)


# adding the paintings to the db
# for name in csv_artists.keys():
#     print("adding paintings of: " + name)
#     name_underscore = name.replace(" ", "_")
#     file_names = get_all_filenames(name_underscore)
#     print(len(file_names), " paintings found")
#     for paint in file_names:
#         ###  with the original image files, the database is getting 12 GB big. ###
#         # full_path = FOLDER_PATH + "/images/images/" + name_underscore + "/" + paint
#         ###   resized images still big with 4.5 GB.
#         full_path = FOLDER_PATH + "/resized/resized/" + paint
#         print(full_path)
#         # im = plt.imread(full_path)
#         # gallery.add_painting(im, name)
#         # print("+", end=" ")
#     # print("\n")

## check how many paintings are in the db:
# count_all_paintings = gallery.query("SELECT COUNT(id) FROM painting", ())
# print(count_all_paintings[0][0]) # 3971

# tests about retrieving the paintings again
test_painting = gallery.get_painting(id_pic=1944)
print(test_painting[:4])
imgplot = plt.imshow(test_painting[4])
plt.show()



#______________________________________________________________________________
### POSSIBILITY 2 REMOTE AZURE DB
#______________________________________________________________________________
# making the object of our type database (holds also the connection to the db
#       needed for further steps)
# for azue reomte DB use:
# gallery = db.db_azure()

# adding the two tables to the database
# gallery.create_table_artist()
# gallery.create_table_painting()

# adding all artists to the database
# add_artists_to_db(csv_artists, gallery)
    
# checking if artists are in database
# print("\nAll artists existing in db")
# all_artist_db = gallery.get_all_artists()
# for row in all_artist_db:
#     print(row)

# adding the pictures of the selected artists to the database

# add_pictures_to_db(csv_artists, gallery)
###  with the original image files, the database is getting 12 GB big. ###

# add_pictures_to_db(csv_artists, gallery, resized=True)
###   resized images still big with 4.5 GB.
    
## check how many paintings are in the db:
# count_all_paintings = gallery.query("SELECT COUNT(id) FROM painting", ())
# print(count_all_paintings[0][0]) # 3971
