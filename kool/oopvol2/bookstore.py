"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        :param rating:book's rating
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        :param rating: book store rating
        """
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating >= self.rating:
            title = book.title
            author = book.author
            for item in self.books:
                if item.title == title and item.author == author:
                    return False
            return True
        else:
            return False


    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        title = book.title
        author = book.author
        for item in self.books:
            if item.title == title and item.author == author:
                return True
        return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if Store.can_remove_book(self, book):
            self.books.remove(book)


    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """

        bookandpricesorted = []
        allbooks = self.get_all_books()
        books_sorted= sorted(allbooks, key=lambda book: book.price)
        for item in books_sorted:
            bookandpricesorted.append([item.title, item.price])
        return bookandpricesorted

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        bookandratingsorted = []
        allbooks = self.get_all_books()
        books_sorted = sorted(allbooks,reverse=True, key=lambda book: book.rating)
        max_rating = max(books_sorted, key=lambda book: book.rating)
        for item in books_sorted:
            if item.rating == max_rating.rating:
                bookandratingsorted.append(item)
        return bookandratingsorted
if __name__ == '__main__':
    book1 = Book("Martin Eden", "Jack London", 22.25, 8.5)
    book2 = Book("Game of thrones", "George R. R. Martin", 27.46, 9.2)
    book3 = Book("Progeme", "Peeter Mees", 14.2, 6.2)
    book4 = Book("Exel algajatele", "N. Nekrassova", 12.2, 8.2)
    book5 = Book("MingiRaamat", "Suva Mees", 15.2, 9.2)
    store = Store("Raamatupood",5.5)
    store.add_book(book1)
    store.add_book(book2)
    store.add_book(book3)
    store.add_book(book4)
    store.add_book(book5)
    #print(store.get_books_by_price())
    print(store.get_most_popular_book())