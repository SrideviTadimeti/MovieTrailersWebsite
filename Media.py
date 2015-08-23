import webbrowser

class Movie():
    def __init__(self, movie_name, movie_storyline, poster, trailer_youtube_link):
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube_link

    def play_trailer(self):
        print("In Play triler method")
        webbrowser.open(self.trailer_youtube_url)
        
    
