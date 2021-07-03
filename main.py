#
# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method == "POST":
#         movies_name = request.form["movie_name"]
#         author = request.form["author"]
#         number = request.form["number"]
#         channel_name = request.form["channel_name"]
#         print(f"{movies_name} {author} {number} {channel_name}")
#
#     return render_template("forms.html")
#
#
# @app.route('/welcome', methods=['GET', 'POST'])
# def welcome():
#     return render_template("welcome.html")
#
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
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

#connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#creating table
class Movies(db.Model):
    __tablename__ = "movie_details"
    movie_name = db.Column(db.String(100), primary_key=True)
    time = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), unique=True, nullable=False)
    duration = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    channel = db.Column(db.String(100), nullable=False)

db.create_all()

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
                    MovieDict[channels] = [moviedata]
print(MovieDict)

# l = 0
# s = 0
# string = []
# for i in range(0, len(MovieDict[0])):
#         string.append(MovieDict[0][i])
#         l+=1
#         if l%4 == 0:
#             print(string)







if __name__ == "__main__":
    app.run(debug=True)