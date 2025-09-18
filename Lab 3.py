class Book:
    def __init__(self, title, author, ISBN, remained_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.remained_copies = remained_copies

    def checking(self):
        if self.remained_copies > 0:
            print("You can borrow this book")
        else:
            print("The remained copies count is 0")

        print(f'Title:{self.title}, Author:{self.author}, ISBN:{self.ISBN}, Availability:{self.remained_copies}')

    def borrowing(self):
        self.remained_copies -= 1
        print(f"You borrowed {self.title}. Remained copies count is {self.remained_copies}")

    def returning(self):
        self.remained_copies += 1
        print(f"You returned {self.title}. Remained copies count is {self.remained_copies}")

class Ebook:
    def __init__(self, title, author, ISBN, remained_copies, file_format, ):
        self.title = title
        self.author = author

def main():
    b1 = Book("The Old Man and the Sea", "Ernest Hemingway", "123456", 2)
    b1.checking()
    b1.borrowing()
    b1.returning()


if __name__ == '__main__':
    main()