class Book:
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text

    def __repr__(self):
        return f'Book: {self.title} by {self.author}'

    def __add__(self, other):
        return Book(title=self.title + )

    if __name__ == '__main__':
        zohar = Book(title='The Zohar', author='Rabbi Shimon')





