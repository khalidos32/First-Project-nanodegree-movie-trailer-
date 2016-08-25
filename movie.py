import webbrowser
import fresh_tomatoes

class movies():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_link):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

Civil_War = movies("Civil War",
                   "Lorem ipsum dolor sit amet",
                    "http://goo.gl/KsNYrv",
                   "https://www.youtube.com/watch?v=dKrVegVI0Us")
Deadpool = movies("Deadpool",
                   "Lorem ipsum dolor sit amet",
                    "http://goo.gl/qACuhi",
                   "https://www.youtube.com/watch?v=9vN6DHB6bJc")
Suicide_squad = movies("Suicide squad",
                   "Lorem ipsum dolor sit amet",
                    "http://goo.gl/D8iyN1",
                   "https://www.youtube.com/watch?v=CmRih_VtVAs")
X_Men = movies("X-Men: Apocalypse",
                   "Lorem ipsum dolor sit amet",
                    "http://goo.gl/DqD2Ce",
                   "https://www.youtube.com/watch?v=Jer8XjMrUB4")
Big_Hero = movies("Big Hero 6",
                   "Lorem ipsum dolor sit amet",
                    "https://goo.gl/G8rpkT",
                   "https://www.youtube.com/watch?v=ppphQ1IeGfs")

list_movies =[Civil_War, Deadpool, Suicide_squad, X_Men, Big_Hero]

fresh_tomatoes.open_movies_page(list_movies)

