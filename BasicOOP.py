class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def sentence(self):
        print(f"{self.title} by {self.author} has {self.pages} pages")

        
b1=Book("Atomic Habits","James Clear",320)
b1.sentence()
