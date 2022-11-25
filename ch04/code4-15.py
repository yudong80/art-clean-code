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
    
    def next_page(self):
        self.current_page += 1
        return self.current_page

    def print_page(self):
        print(f"... Page Content {self.current_page} ...")


python_one_liners = Book()

print(python_one_liners.get_publisher())
# 출판사 이름 출력

python_one_liners.print_page()
# ... 0 페이지 내용
python_one_liners.next_page()
python_one_liners.print_page()
# ... 1 페이지 내용