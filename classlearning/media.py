import webbrowser

#stores variables found in entertainment_center.py
class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#opens a trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
