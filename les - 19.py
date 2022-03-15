# s = "I am learning Python. hello, WORLD!"
# start = s.find("h")
# end = s.rfind("h")
# print(start, end)
# s1 = s[0:start]
# s2 = s[end + 1:]
# s_new = s1 + s2
# print(s_new)
#
#
# c = 'I am learning Python. hello, World!'
# c = c[:c.find('h')] + c[c.rfind('h') + 1:]
# print(c)

# s = 'hello, World! I am learning Python.'
# print(s.endswith("lo", 0, 5))
# print(s.startswith("I am", 14))

# print('abc123'.isalnum()) #  если строка состоит из букв и цыфр возвращает True
# print('abc$123'.isalnum())
# print(''.isalnum())

# print("ABCabc".isalpha()) # строка состоит только из букв
#
# print("123".isdigit()) # строка состоить из цыфр


# print("abc".isidentifier()) # валидный идентефикатор
# print("1abc".isidentifier())

# print('abc$123'.islower()) # гижний регистр + любые символы и цыфры

# print(" \t \n ". isspace()) # строка состоит из пробельных символов

# print("The Apple".istitle()) # каждый первый символ должен быть в верхнем регистре

# print("ABC".isupper()) # все буквы в верхнем регистре + символы и цыфры


# print('py'.center(10, '-'))
# print('py'.center(2))
# print('py'.center(9, '-'))

# print('     py'.lstrip()) # удаление пробелов слева
# print('py     '.rstrip()) # удаление пробелов справа
# print('http://www.python.org'.lstrip('/:pths')) # удаляет символы слева
# print('py.$$$;'.rstrip(';$.'))
# print('http://www.python.org'.lstrip('/:pths').rstrip('org.'))
# print("    py   ".strip()) # удаляет пробелы слева и справа


# s = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык програмирования.'
# print(s.replace("Nuthon", "Python", 2))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# print(":".join("Hello"))

# print("Строка разделенная пробелами".split())
# print('www.pythin.org'.split("."))
# print('www.pythin.org.ru'.split(".", 1))

# a = input("-> ", ).split()
# print(a)

# a = input("Введите ФИО: ").split()
# print(a)
# print(a[0], a[1][:1] + '.', a[2][:1] + '.')

# a = input("Введите строку: ").split()
# print('*'.join(a))

import re

# s = "Я ищу совпадения в 2021 году. И я их обязательно найуд."
# reg = r'\.'
# print(s)
# print(re.findall(reg, s)) # возвращает список со всеми совпаниями
# print(re.search(reg, s)) # возвращает первое найденное совпадение и останавливает поиск
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# reg = 'Я'
# print(re.match(reg, s)) # в начале строки

# print(re.split(reg, s, 1))

# print(re.sub(reg, "!", s))

# \d любая цифра
# \w любая цифра, буква, _
# \s пробельный символ
# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg = r'ния\b'
# print(re.findall(reg, s))

# s = "Еда, беду, победа"
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s))


# s = "Ели[-ели]"
# reg = r'[А-Яа-яё.\[\]-]'
# print(re.findall(reg, s))

# s = "Час ы 24-часвом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т20:09"
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# повторения
# +  от 1 до бесконечности
# *  от 0 до бесконечности
# ?  от 0 до 1

# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546"
# # reg = r'20?'
# # print(s)
# # print(re.findall(reg, s))
# #
# # d = "Цифры: 7, +17, -42, 0013, 0.3"
# # print(re.findall(r'[-+]?[\d.]+', d))

# s = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"#.*", "", s)))

# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))


# s1 = "МИ Д - Министерство иностранных дел, ГЭС - Гидроэлектро станция, ФСБ - Федеральная служба безопасности"
# reg1 = r"[А-ЯЁ]{2,}\s*[А-ЯЁ]*"
# print(re.findall(reg1, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r'\+*\d{11}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# print(re.findall(r"\w+", "12, + й"))
# print(re.findall(r"\w+", "12, + й", flags=re.A))

# s = 'hello world'
# print(re.findall(r"\w\+", s, flags=re.DEBUG))

# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546"
# reg = r'я'
# print(re.findall(reg, s, flags=re.I))

# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, flags=re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, flags=re.MULTILINE))

# text = """
# {
# "one": 1,
# "two": 2,
# "three": 3
# }
# """
# print(re.findall(r'^["\w+]+', text))
# print(re.findall(r'^["\w+]+', text, flags=re.MULTILINE))


# print(re.findall("""
# [a-z.-]+ # part 1
# @
# [a-z.-]+ # part 2
# """, 'test@mail.ru', flags=re.VERBOSE))


# text = """Python
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
# print(validate_name('Python_master'))


# s = "123456@i.ru, 123456@i.ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@.name.ru"
# reg = r"[\w.-]+@[\w.-]+"
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений<./body>"
# print(re.search('<.*?>', text).group())
# s = "<p>Изображение <img alt='картинка' scr='bg.jpg'> - фон страницы"
# reg = r"<img\s+[^>]*?src\s*=\s*[^>]+>"
# print(re.findall(reg, s))


# text = "Python (в русском языке распространено название пито́н[16] или пайтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической типизацией и автоматическим управление памятью[18][19]."
# print(re.findall(r"\[[\d]+]", text))
# print(re.findall(r"\[.*?]", text))


# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"(int|float)\s*=\s*(\d[.\w+]*)"
# print(re.findall(reg, s))


# (?:) - группирующая скобка не является сохраняющей
