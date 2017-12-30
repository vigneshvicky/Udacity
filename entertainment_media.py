import fresh_tomatoes
import media

"""Create movie instance to specified movie"""
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "asset/images/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "00:30","John Lasseter")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                        "asset/images/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=-9ceBgWV8io",
                     "01:30","James Cameron")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                        "asset/images/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=atLg2wQQxvU",
                                "01:10","Woody Allen")

ice_age = media.Movie("Ice age",
                         "Cartoon Movie",
                        "asset/images/ice-age-poster.jpg",
                        "https://youtu.be/cMfeWyVBidk",
                      "02:50","Chris Wedge")

titanic = media.Movie("Titanic","Sinking ship",
                      "asset/images/titanic-poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      "03:05",
                      "James Cameron"
                      )
speed = media.Movie("Speed","Bus on Boom",
                    "asset/images/speed-poster.jpg",
                    "https://youtu.be/Fk4A1AY10U0",
                    "00:20",
                    "Jan de Bont")

"""Assigned all the movie into movieCollections variable"""
movieCollections = [toy_story,avatar,midnight_in_paris,ice_age,titanic,speed]

"""Send movieCollections as a parameter of fresh_tomatoes class"""
fresh_tomatoes.open_movies_page(movieCollections)

#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
