class Ebook:
    """Represents an e-book in the store."""

    def __init__(self, title, author, publication_date, genre, price, isbn, stock_quantity):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price
        self.__isbn = isbn
        self.__stock_quantity = stock_quantity

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def get_stock_quantity(self):
        return self.__stock_quantity

    def update_price(self, new_price):
        self.__price = new_price

    def update_stock(self, new_stock):
        self.__stock_quantity = new_stock

    def is_available(self):
        return self.__stock_quantity > 0

    def __str__(self):
        return f"Ebook(title={self.__title}, author={self.__author}, price={self.__price})"
