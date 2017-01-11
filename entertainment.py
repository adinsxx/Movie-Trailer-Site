import fresh_tomatoes
import trailers

star_wars = trailers.Movie("Star Wars: TFA",
                           "Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
                           "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823",
                           "https://www.youtube.com/watch?v=sGbxmsDFVnE")
#print(star_wars.storyline)
mad_max = trailers.Movie("Mad Max: Fury Road",
                         "A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
                         "http://cdn2-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/11110866_658246694280855_1682386295316885693_o.jpg",
                         "https://www.youtube.com/watch?v=hEJnMQG9ev8")
#print(mad_max.storyline)
#mad_max.show_trailer()
chef = trailers.Movie("Chef",
                      "A head chef quits his restaurant job and buys a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.",
                      "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                      "https://www.youtube.com/watch?v=wgFws3AoIUY")

big_hero = trailers.Movie("Big Hero 6",
                          "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                          "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                          "https://www.youtube.com/watch?v=z3biFxZIJOQ")

scott_pilgrim = trailers.Movie("Scott Pilgrim vs. The World",
                               "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
                               "https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg",
                               "https://www.youtube.com/watch?v=7wd5KEaOtm4")

star_trek = trailers.Movie("Star Trek: First Contact",
                           "The Borg travel back in time intended on preventing Earth's first contact with an alien species. Captain Picard and his crew pursue them.",
                           "https://upload.wikimedia.org/wikipedia/en/d/dd/Star_Trek_08-poster.png",
                           "https://www.youtube.com/watch?v=MWcbmkdsFYs")

movies = [star_wars, mad_max, chef, big_hero, scott_pilgrim, star_trek]
fresh_tomatoes.open_movies_page(movies)
