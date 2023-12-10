class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        temp_list = []
        for contract in Contract.all:
            if self == contract.author:
                temp_list.append(contract)
        return temp_list

    def books(self):
        temp_list = []
        for contract in Contract.all:
            if self == contract.author:
                temp_list.append(contract.book)
        return temp_list
    
    def sign_contract(self, book, date, royalties):
        if isinstance(self, Contract):
            raise Exception
        contract = Contract(self, book, date, royalties)
        return contract
            
    
    def total_royalties(self):
        num = 0
        for contract in Contract.all:
            if self == contract.author:
                num += contract.royalties
        return num

class Book:
    def __init__(self, title):
        self.title = title
    
    def contracts(self):
        temp_list = []
        for contract in Contract.all:
            if self == contract.book:
                temp_list.append(contract)
        return temp_list
    
    def authors(self):
        temp_list = []
        for contract in Contract.all:
            if self == contract.book:
                temp_list.append(contract.author)
        return temp_list

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
       if not isinstance(author, Author) or not isinstance(book, Book) or type(date) != str or type(royalties) != int:
           raise Exception
       
       self.author = author
       self.book = book
       self.date = date
       self.royalties = royalties

       Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        beans = []
        for contract in Contract.all:
            if date == contract.date:
                beans.append(contract)      
        return beans