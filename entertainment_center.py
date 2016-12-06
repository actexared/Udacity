
"""This file defines instances of the movie class that was defined in the media.py file."""

import media
import fresh_tomatoes

"""For each movie, the instance of title, storyline, poster image and the url link for the Youtube trailer is defined"""

caddyshack = media.Movie("Caddyshack", 
	                 "A teen gets more than he bargains for while working at a high end Country Club", 
		             "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
					 "https://www.youtube.com/watch?v=zrTqenN1SqQ")


life_of_pets = media.Movie("The Secret Life of Pets",
						   "Dogs, cats and other pets have fun while their owners are away", 
						   "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
						    "www.youtube.com/watch?v=zig3eZVJmm4")

risen = media.Movie("Risen",
					"A Roman soldier investigates the disappearance of Jesus' body", 
					"http://t3.gstatic.com/images?q=tbn:ANd9GcTlr6azlxH_XC22SFc-9rt16xOcBtzt17WiiHZOJQAZLg_2ZIxE",
					"https://www.youtube.com/watch?v=ucUbAAMEF8M")

office_space = media.Movie("Office Space", 
						  "A Computer Programmer who hates his job",
						  "http://ia.media-imdb.com/images/M/MV5BOTA5MzQ3MzI1NV5BMl5BanBnXkFtZTgwNTcxNTYxMTE@._V1_SX640_SY720_.jpg",
						  "https://www.youtube.com/watch?v=dMIrlP61Z9s")

major_league = media.Movie("Major League",
						   "A group of incompetent players on a major league team finds a way to win",
						   "http://t0.gstatic.com/images?q=tbn:ANd9GcS0RIBg2KCGSZiGOj-jfLKDHgzCm9QWUIuHEk3FShTFpKk6qg6P",
						   "https://www.youtube.com/watch?v=K_ILz9bC-VU")

jason_bourne = media.Movie("Jason Bourne", 
						   "After laying low for a decade former top CIA agent Jason Bourne is drawn out of the shadows",
						   "http://t2.gstatic.com/images?q=tbn:ANd9GcRlE2se11A6emeQ_m0ovAQJdmWtdo8ViWUVAc7rDUKw3DmE_Cf-",
						   "https://www.youtube.com/watch?v=_gBnmKOixDM")



movies = [caddyshack, life_of_pets, risen, office_space, major_league, jason_bourne]

#The open_movies_page function is called from the fresh_tomatoes.py file to generate a website
fresh_tomatoes.open_movies_page(movies)


