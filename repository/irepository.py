from abc import ABC, abstractmethod

class Irepository:
    
    @abstractmethod
    def read_books():
        pass
    
    @abstractmethod
    def create_book():
        pass

    @abstractmethod
    def delete_book():
        pass

    @abstractmethod
    def read_books_APIS():
        pass