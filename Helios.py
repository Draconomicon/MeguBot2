import requests
from bs4 import BeautifulSoup as bs
from imdbpie import Imdb
from utility import *


def check_helios():

    ###   Vars   ###
    Helios_base = 'http://www.helios.pl'
    Helios_web = requests.get('http://www.helios.pl/3,Wroclaw/Repertuar/')
    repertuar = []
    movie_db = []
    imdb = Imdb(anonymize=True)
    UpdateMailBody('=== Helios Films ===<br>')
    ################

    if Helios_web.status_code == 200:
        print('Successful connectet to Helios website')
    else:
        exit()

    Helios_data = bs(Helios_web.text, "html.parser")

    ### First loop - create Helios link to each movie ###
    for data in Helios_data.findAll('a', {'class': 'movie-link'}):
        link = data.get('href')
        link = Helios_base + link
        repertuar.append(link)

    ### Second loop - extract movie name from each Helios movie web page ###
    for data in repertuar:
        # print(data)
        temp = bs(requests.get(data).text, "html.parser")
        a = temp.find('h2')
        if a.string:
            movie_db.append(a.string)

    movie_db = remove_duplicates(movie_db)
    # print(movie_db)


    ### third loop - gather data from IMdB ###
    for data in movie_db:
        # print(data)
        temp = imdb.search_for_title(data)
        if temp:
            temp = temp[0]
            # print(temp['imdb_id'])
            title = imdb.get_title_by_id(temp['imdb_id'])
            # print(title.rating)
            UpdateMailBody(data + '<br>   Genres: ' + str(title.genres) + '<br>')
            UpdateMailBody('   IMDB Rated: ' + str(title.rating) + '<br>')
            # print(mail_body)
            quality = 0
            for a in title.trailers:
                if a['format'] == 'HD 1080p' and quality < 3:
                    jakosc = a['url']
                    quality = 3
                if a['format'] == 'HD 720p' and quality < 2:
                    jakosc = a['url']
                    quality = 2
                if a['format'] == 'HD 480p' and quality < 1:
                    jakosc = a['url']
                    quality = 1
            if quality == 0:
                UpdateMailBody('No Normal quality trailer<br><br>')
            else:
                UpdateMailBody('<a href = "' + jakosc + '" > (Trailer) </a><br><br>')



