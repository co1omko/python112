class Book:
    name = "name"
    year = "0000"
    publisher = "publisher"
    genre = "genre"
    author = "author"
    price = "price"

    def print_info(self):
        print("Информация о книге".center(40, "*"))
        print(f"Название книги: {self.name}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, first_name, year, publisher, genre, author, price):
        self.name = first_name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

b1 = Book()
b1.input_info("Элемент крови", "2012", "АСТ", "Фантастический детектив", "Зотов Г.А.", "350р.")
b1.print_info()
b1.set_name("Печать луны")
print(b1.get_name())