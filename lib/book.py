#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Constructor to initialize the Book object with title and page count
        self.title = title
        self._page_count = page_count  # Using an underscore to indicate it's a "private" attribute

    @property
    def page_count(self):
        return self._page_count  # Getter method for page count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value  # Setter method for page count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book = Book("And Then There Were None", 272)
print(book.page_count)  # Output: 272
print(book.title)  # Output: "And Then There Were None"
book.page_count = 300  # Setting new page count
book.page_count = "not an integer"  # This will print an error message
book.turn_page()  # Output: "Flipping the page...wow, you read fast!"
