import webbrowser

class Video():
        """This is Base class. We defined common variables here."""
        def __init__(self,title,duration):
                self.title = title
                self.duration = duration


class Movie(Video):        
        """ This class provides a way to store movie related information
            This Movie class extended the Video base class"""
        
        def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movieDuration,movie_director):
                video = Video(movie_title,movieDuration)
                self.title = video.title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.duration = video.duration
                self.director = movie_director
                
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)

class TVShow(Video):
        """TVShow class created.
        This TVShow class extended the Video base class"""

        def __init__(self,showTitle,season,episode,station,showDuration,director):
                video = Video(showTitle,showDuration)
                self.title = video.title
                self.storyline = season
                self.episode = episode
                self.tv_station = tv_station
                self.poster_image_url = episode
                self.trailer_youtube_url = tv_station
                self.duration = video.duration
                self.director = director
                
        def displayTVShow(self):
                webbrowser.open(self.trailer_youtube_url)
