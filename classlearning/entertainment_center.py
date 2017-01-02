import fresh_tomatoes
import media

#movies
interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw&t=44s")

the_martian = media.Movie("The Martian",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                               "https://www.youtube.com/watch?v=VYZ3U1inHA4")

train_dragon = media.Movie("How to Train Your Dragon",
                           "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                           "https://www.youtube.com/watch?v=GfBHLVtbG6U&t=23s")

train_dragon2 = media.Movie("How to Train Your Dragon 2",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/How_to_Train_Your_Dragon_2_poster.jpg",
                            "https://www.youtube.com/watch?v=Z9a4PvzlqoQ&t=57s")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=CzvH6_e2a-U")

#array of movies for fresh tomatoes to use
movies = [interstellar,the_martian,fantastic_beasts,train_dragon,train_dragon2,zootopia]

#calling fresh tomatoes
fresh_tomatoes.open_movies_page(movies)
