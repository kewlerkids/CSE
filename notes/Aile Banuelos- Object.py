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

