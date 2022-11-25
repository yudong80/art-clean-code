class Book:

    def __init__(self):
        self.title = "Python One-Liners"
        self.publisher = "NoStarch"
        self.author = "Mayer"
        self.current_page = 0

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_page(self):
        return self.current_page

    def next_page(self):
        self.current_page += 1

class Printer:
    def print_page(self, book):
        print(f"... Page Content {book.get_page()} ...")


python_one_liners = Book()
printer = Printer()

printer.print_page(python_one_liners)
# ... 0 페이지 내용 ...

python_one_liners.next_page()
printer.print_page(python_one_liners)
# ... 1 페이지 내용 ...