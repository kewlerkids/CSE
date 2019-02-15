class Book (object):
    def __init__(self, cover, pages, titles, colors):
        self.cover = cover
        self.pages = pages
        self.size = 7
        self.title = titles
        self.color = colors

    def open(self):
        if self.pages:
            Book.pages = ()

    def shrink(self):
        self.size -= 1


hard = "A hard cover book"
black = "The color black"

harry_potter = Book(hard, 636, 'Harry Potter', black)
# percy_jackson = Book(hard,)
# the_hobbit = Book()
# hunger_games = Book()
# life_of_pi = Book()
# cat_in_the_hat = Book()
# the_chronicles_of_narnia = Book(paper,)
