import Media
import fresh_tomatoes

#Creating Movie instances

kung_fu_panda3 = Media.Movie("Kung Fu Panda 3", "After reuniting with his long-lost father (Bryan Cranston), Po (Jack Black) must train a village of clumsy pandas to help him defeat the villainous Kai (J.K. Simmons).",
                       "http://cdn.sleepyskunk.com/uploads/kungfupanda3.jpg",
                       "https://www.youtube.com/watch?v=UgBWSPD6MUU")

frozen = Media.Movie("Frozen", "When their kingdom becomes trapped in perpetual winter, fearless Anna (Kristen Bell) joins forces with mountaineer Kristoff (Jonathan Groff) and his reindeer sidekick to find Anna's sister, Snow Queen Elsa (Idina Menzel), and break her icy spell. Although their epic journey leads them to encounters with mystical trolls, a comedic snowman (Josh Gad), harsh conditions, and magic at every turn, Anna and Kristoff bravely push onward in a race to save their kingdom from winter's cold grip.",
                       "http://vignette2.wikia.nocookie.net/frozen/images/5/58/Frozen-movie-poster.jpg/revision/latest?cb=20140115094640",
                       "https://www.youtube.com/watch?v=TbQm5doF_Uc")

monsters_inc = Media.Movie("Monsters Inc.", "Monsters Incorporated is the largest scare factory in the monster world, and James P. Sullivan (John Goodman) is one of its top scarers. Sullivan is a huge, intimidating monster with blue fur, large purple spots and horns. His scare assistant, best friend and roommate is Mike Wazowski (Billy Crystal), a green, opinionated, feisty little one-eyed monster. Visiting from the human world is Boo (Mary Gibbs), a tiny girl who goes where no human has ever gone before.",
                       "http://img4.wikia.nocookie.net/__cb20150108181000/disney/images/1/10/Monsters,_Inc._-_Poster.jpg",
                       "https://www.youtube.com/watch?v=cvOQeozL4S0")

despicable_me = Media.Movie("Despicable Me", "A man who delights in all things wicked, supervillain Gru (Steve Carell) hatches a plan to steal the moon. Surrounded by an army of little yellow minions and his impenetrable arsenal of weapons and war machines, Gru makes ready to vanquish all who stand in his way. But nothing in his calculations and groundwork has prepared him for his greatest challenge: three adorable orphan girls (Miranda Cosgrove, Dana Gaier, Elsie Fisher) who want to make him their dad.",
                       "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                       "https://www.youtube.com/watch?v=zZcLxQRzg18")

inside_out = Media.Movie("Inside Out", "Riley (Kaitlyn Dias) is a happy, hockey-loving 11-year-old Midwestern girl, but her world turns upside-down when she and her parents move to San Francisco. Riley's emotions -- led by Joy (Amy Poehler) -- try to guide her through this difficult, life-changing event. However, the stress of the move brings Sadness (Phyllis Smith) to the forefront. When Joy and Sadness are inadvertently swept into the far reaches of Riley's mind, the only emotions left in Headquarters are Anger, Fear and Disgust.",
                         "http://www.fatmovieguy.com/wp-content/uploads/2015/03/Disney-Pixar-Inside-Out-Movie-Poster.jpg",
                         "https://www.youtube.com/watch?v=7ZLOYXKmIkw")

big_hero = Media.Movie("Big Hero 6", "Robotics prodigy Hiro (Ryan Potter) lives in the city of San Fransokyo. Next to his older brother, Tadashi, Hiro's closest companion is Baymax (Scott Adsit), a robot whose sole purpose is to take care of people. When a devastating turn of events throws Hiro into the middle of a dangerous plot, he transforms Baymax and his other friends, Go Go Tamago (Jamie Chung), Wasabi (Damon Wayans Jr.), Honey Lemon (Genesis Rodriguez) and Fred (T.J. Miller) into a band of high-tech heroes.",
                       "http://posterposse.com/wp-content/uploads/2014/10/poster-big-hero-6_hi.jpg",
                       "https://www.youtube.com/watch?v=bT8qmoCgxZg")

movies_list = [kung_fu_panda3, frozen, monsters_inc, despicable_me, inside_out, big_hero]

#Show movie trailers in a web page

fresh_tomatoes.open_movies_page(movies_list)




                       
