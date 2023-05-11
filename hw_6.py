class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

class Subscriber:
    def __init__(self, full_name):
        self.full_name = full_name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.subscribers = []
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return True
        return False

    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            return True
        return False

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_subscriber(self, full_name):
        for subscriber in self.subscribers:
            if subscriber.full_name == full_name:
                return subscriber
        return None

    def lend_book(self, subscriber, book):
        if subscriber and book:
            if book not in subscriber.borrowed_books:
                subscriber.borrowed_books.append(book)
                return True
        return False

    def return_book(self, subscriber, book):
        if subscriber and book:
            if book in subscriber.borrowed_books:
                subscriber.borrowed_books.remove(book)
                return True
        return False

def main():
    library = Library()

    while True:
        print("Select action:")
        action = int(input())

        if action == 1:
            book_info = input().split(", ")
            book = Book(book_info[0], book_info[1])
            if library.add_book(book):
                print("success")
            else:
                print("book already exists")

        elif action == 2:
            full_name = input()
            subscriber = Subscriber(full_name)
            if library.add_subscriber(subscriber):
                print("success")
            else:
                print("subscriber exists")

        elif action == 3:
            full_name, book_title = input().split(", ")
            subscriber = library.find_subscriber(full_name)
            book = library.find_book(book_title)

            if not subscriber:
                print("subscriber does not exist")
            elif not book:
                print("book does not exist")
            else:
                if library.lend_book(subscriber, book):
                    print("success")
                else:
                    print("the copy of the book is already taken")

        elif action == 4:
            full_name, book_title = input().split(", ")
            subscriber = library.find_subscriber(full_name)
            book = library.find_book(book_title)

            if not subscriber:
                print("subscriber does not exist")
            elif not book:
                print("book does not exist")
            else:
                if library.return_book(subscriber, book):
                    print("success")
                else:
                    print("A book can be returned only by the subscriber who took it")

        elif action == 5:
            full_name = input()
            subscriber = library.find_subscriber(full_name)
            if not subscriber:
                print("subscriber does not exist")
            else:
                print(f"{subscriber.full_name}, {len(subscriber.borrowed_books)}")

     


   elif action == 6:
            print("goodbye")
            break

if __name__ == "__main__":
    main()
