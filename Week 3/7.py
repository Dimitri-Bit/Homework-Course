class Book:

    def __init__(self, title, author, year_of_publish, num_of_copies):
        self.title = title
        self.author = author
        self.year_of_publish = year_of_publish
        self.num_of_copies = num_of_copies

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_year_of_publish(self):
        return self.year_of_publish
    
    def set_year_of_publish(self, year):
        self.year_of_publish = year

    def get_num_of_copies(self):
        return self.num_of_copies

    def set_num_of_copies(self, num):
        self.num_of_copies = num

class Library:

    def __init__(self, book_list):
        self.book_list = book_list

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book_title):
        for i in self.book_list:
            if i.title == book_title:
                self.book_list.remove(i)
                return
            
    def show_books(self):
        for i in self.book_list:
            print(f"Title: {i.title} Author: {i.author} Year of publish: {i.year_of_publish} Number of copies: {i.num_of_copies}")
            
    def find_book_title(self, title):
        for i in self.book_list:
            if i.title == title:
                return i

    def find_book_author(self, author):
        for i in self.book_list:
            if i.author == author:
                return i

book1 = Book("title1", "author1", 1999, 35)
book2 = Book("title2", "author2", 2005, 20)
book3 = Book("title3", "author3", 1996, 50)

library = Library([book1, book2, book3])
library.show_books()
print("------")
library.remove_book("title2")
library.show_books()