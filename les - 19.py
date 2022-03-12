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