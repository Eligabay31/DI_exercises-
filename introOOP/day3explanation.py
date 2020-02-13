 class Writer:
     def __init__(self, name, n_books, genre):
         self.name = name
         self.n_books = n_books
         self.genre = genre

     def write(self):
         self.n_books += 1
         print(f"{self.name} wrote a book")

     def say_hi():
         




if __name__ == '__main__':
  albert = Writer(name = "Albert Camus", n_books = 25, genre = ["Philosophy", "Roman"])
    print(albert.name)
    print(albert.n_books)
    print(albert.genre)

