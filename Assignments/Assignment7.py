from typing import List, Dict, Union
#import books.txt, users.txt
import os

# Base User Class
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @staticmethod
    def validate_email(email: str) -> bool:
        return "@" in email and "." in email

# Librarian Class
class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

# Member Class
class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self.borrowed_books: List[int] = []

# class Book:
class Book:
    def __init__(self, book_id: int, title: str, author: str, availability: bool):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability

    @property
    def book_id(self) -> int:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        self._title = new_title

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    @property
    def availability(self) -> bool:
        return self._availability

    @availability.setter
    def availability(self, available: bool) -> None:
        self._availability = available

    def display_info(self) -> None:
        print(f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Available: {self._availability}")

# LibraryManager Class
class LibraryManager:
    books_file = 'books.txt'
    users_file = 'users.txt'

    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.users: Dict[int, Union[Librarian, Member]] = {}

    # File Handling Methods
    def load_data(self) -> None:
        # Load books
        try:
            with open(self.books_file, 'r') as bf:
                for line in bf:
                    book_data = line.strip().split(',')
                    book_id, title, author, availability = int(book_data[0]), book_data[1], book_data[2], book_data[3] == 'True'
                    self.books[book_id] = Book(book_id, title, author, availability)
        except FileNotFoundError:
            print(f"{self.books_file} not found.")
        except Exception as e:
            print(f"An error occurred while loading books: {e}")

        # Load users
        try:
            with open(self.users_file, 'r') as uf:
                for line in uf:
                    user_data = line.strip().split(',')
                    user_id, name, email, role = int(user_data[0]), user_data[1], user_data[2], user_data[3]
                    if role == 'Librarian':
                        self.users[user_id] = Librarian(user_id, name, email)
                    elif role == 'Member':
                        self.users[user_id] = Member(user_id, name, email)
        except FileNotFoundError:
            print(f"{self.users_file} not found.")
        except Exception as e:
            print(f"An error occurred while loading users: {e}")

    def save_data(self) -> None:
        # Save books
        try:
            with open(self.books_file, 'w') as bf:
                for book in self.books.values():
                    bf.write(f"{book.book_id},{book.title},{book.author},{book.availability}\n")
        except IOError as e:
            print(f"Error writing to {self.books_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving books: {e}")

        # Save users
        try:
            with open(self.users_file, 'w') as uf:
                for user in self.users.values():
                    role = 'Librarian' if isinstance(user, Librarian) else 'Member'
                    uf.write(f"{user.user_id},{user.name},{user.email},{role}\n")
        except IOError as e:
            print(f"Error writing to {self.users_file}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving users: {e}")

    # Book Management Methods
    def add_book(self, book_id: int, title: str, author: str) -> None:
        if book_id in self.books:
            print("Book already exists.")
        else:
            self.books[book_id] = Book(book_id, title, author, True)
            self.save_data()

    def update_book(self, book_id: int, title: str, author: str) -> None:
        if book_id in self.books:
            self.books[book_id].title = title
            self.books[book_id].author = author
            self.save_data()
        else:
            print("Book not found.")

    def delete_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]
            self.save_data()
        else:
            print("Book not found.")

    # User Management Methods
    def register_user(self, user_id: int, name: str, email: str, role: str) -> None:
        if user_id in self.users:
            print("User already exists.")
        elif not User.validate_email(email):
            print("Invalid email format.")
        else:
            if role == 'Librarian':
                self.users[user_id] = Librarian(user_id, name, email)
            elif role == 'Member':
                self.users[user_id] = Member(user_id, name, email)
            self.save_data()

# Borrow and Return Books
    def borrow_book(self, user_id: int, book_id: int) -> None:
        if user_id not in self.users:
            print("User not found.")
        elif not isinstance(self.users[user_id], Member):
            print("Only members can borrow books.")
        elif book_id not in self.books:
            print("Book not found.")
        elif not self.books[book_id].availability:
            print("Book not available.")
        else:
            # Only proceed if user is a Member
            self.books[book_id].availability = False
            member = self.users[user_id]  # Safely cast the user to Member
            if isinstance(member, Member):  # Double-check for clarity
                member.borrowed_books.append(book_id)
                self.save_data()
                print(f"Book {book_id} has been borrowed by Member {user_id}.")

    def return_book(self, user_id: int, book_id: int) -> None:
        if user_id not in self.users:
            print("User not found.")
        elif not isinstance(self.users[user_id], Member):
            print("Only members can return books.")
        elif book_id not in self.books:
            print("Book not found.")
        else:
            # Safely cast the user to Member
            member = self.users[user_id]
            if isinstance(member, Member):
                if book_id not in member.borrowed_books:
                    print("This book is not borrowed by the user.")
                else:
                    self.books[book_id].availability = True
                    member.borrowed_books.remove(book_id)
                    self.save_data()
                    print(f"Book {book_id} has been returned by Member {user_id}.")
# Example Usage
if __name__ == "__main__":
    manager = LibraryManager()
    manager.load_data()

    # Add a new book
    manager.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")

    # Register a user
    manager.register_user(101, "Alice", "alice@example.com", "Member")

    # Borrow a book
    manager.borrow_book(101, 1)

    # Return a book
    manager.return_book(101, 1)
