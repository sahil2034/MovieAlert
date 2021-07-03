import requests
from bs4 import BeautifulSoup

MN_HD = "https://www.indiandth.in/epg/mn+-hd-2801-epg-schedule.html"
STAR_MOVIES = "https://www.indiandth.in/epg/star-movies-hd-2813-epg-schedule.html"
STAR_MOVIES_SELECT = "https://www.indiandth.in/epg/star-movies-select-hd-3010-epg-schedule.html"
UTV_ACTION = "https://www.indiandth.in/epg/utv-action-2520-epg-schedule.html"
SONY_PIX = "https://www.indiandth.in/epg/sony-pix-hd-2811-epg-schedule.html"
MOVIES_NOW = "https://www.indiandth.in/epg/movies-now-2515-epg-schedule.html"
MNX = "https://www.indiandth.in/epg/mnx-1865-epg-schedule.html"
PRIVE_HD = "https://www.indiandth.in/epg/andprive-hd-2727-epg-schedule.html"
ROMEDY_NOW = "https://www.indiandth.in/epg/romedy-now-hd-3025-epg-schedule.html"
FLIX_HD = "https://www.indiandth.in/epg/andflix-3026-epg-schedule.html"


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

MOVIE_LINK_LIST = [MN_HD, STAR_MOVIES, STAR_MOVIES_SELECT, UTV_ACTION, SONY_PIX, MNX, PRIVE_HD,
                   ROMEDY_NOW, FLIX_HD, MOVIES_NOW]

MovieDict = {}
moviedata = []

for moviechannels in MOVIE_LINK_LIST:
    response = requests.get(moviechannels)
    tv_schedule_html = response.text

    soup = BeautifulSoup(tv_schedule_html, "html.parser")

    channels = soup.find(name="h2").getText().replace("EPG Schedule / Program Listings", "")
    movie_details = soup.find_all(name="table")


    for movietable in movie_details:
        table_body = movietable.find('tbody')
        rows = table_body.find_all('tr')
        for tr in rows:
                cols = tr.find_all('td')
                for td in cols:
                    moviedata.append(td.text)
                    x = list(divide_chunks(moviedata, 4))
                    MovieDict[channels] = [x]


print(MovieDict)
























