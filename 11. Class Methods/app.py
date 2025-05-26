class Book:
    total_books = 0  # Class variable to count total number of books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Class method ko call kar rahe hain har book banne par

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# Books create karte hain
book1 = Book("Python Programming")
book2 = Book("Data Science Basics")

# Total books print karte hain
print(f"Total books created: {Book.total_books}")
