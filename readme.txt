#####################################################
###                                               ###
###                 Megu Bot v1.1                 ###
###                                               ###
#####################################################


### Helios ###
Vars:
    Helios_base - Helios base webpage, we are using it to crate film link
    Helios_web - place where we find all movies on screen at cinema
    imdb = Imdb(anonymize=True) <-- we are using it for IMDB library

First loop:
    Helios web on 'Repertuar' view do not have any english movie names, which we need to search on imdb
    We simply take Helios ID for film, and create link to it

Second loop:
    We find english movie name on "h2" for each Helios movie web page, we just extract text from "h2" building movie_db

Remove duplicates:
    There are many Helios web page for some movies, normal, normal with lector, 3D etc.

Third loop:
    This is loop we gather information from IMDB, we use IMBD library for it
    -First we find IMdB movie ID by it title - function: search_for_title
    -When we got movie ID we create IMdB object, that collect all data from IMdB - func: get_title_by_id
    -Now, we just gather intesesting data movie name, rating, genere, and trailer
        -Some words about trailer, IMdB library gather all kind of data from IMdB, including trailer
         Unfortunately it does not sort it via quality, so i add little logic to find best quality
    All data are updated to Mail body