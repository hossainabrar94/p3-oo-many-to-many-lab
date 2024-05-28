class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties)

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(date, str):
            self.date = date
        else:
            raise TypeError('date must be a string')
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise TypeError('royalties must be an integer')
        self.author = author
        self.book = book
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author not an instance of the Author class')
        
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book=book
        else:
            raise Exception('Book is not an instance of the Book class')
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]