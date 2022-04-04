# Файлы
# print(f.closed)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)


# f = open(r'C:\Users\Демид\Desktop\python\txt.txt', 'r') # r чтение файла
# print(f.read())
# f.close()

# f = open(r'test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# f.close()
#
# f = open(r'test.txt', 'r')
# print(len(f.readline()))
# for line in f:
#     print(line)
# f.close()

#
# f = open('xyz.txt', 'w') # w создание нового файла
# f.write('Hello\nWorld')
# f.close()

# f = open('xyz.txt', 'a') # a добавляет запись в конце файла
# lines = ['This is line 1', 'This is line 2']
# f.writelines(lines)
# f.close()


# f = open('xyz.txt', 'w')
# lst =[str(i)for i in range(1, 20)]
# for i in lst:
#     f.write(i + "\t")
# f.close()

# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open('text2.txt', 'r')
# rd = f.readlines()
# # print(rd)
# for i in range(len(rd)):
#     if rd[i] == "изменить строку в списке;\n":
#         rd[i] = "Hello World\n"
# # print(rd)
# f.close()
# f = open('text2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('text2.txt', 'r')
# print(f.read())
# f.close()


# f = open('text2.txt', 'r')
# rd = f.readlines()
# print(rd)
# a = int(input("Выберите позицию для удаления: "))
# if 0 <= a <= len(rd):
#     del rd[a]
# else:
#     print("Позиция введена не верно")
# print(rd)
# f.close()


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell()) # возвращает текущую позицию курсора в файле
# print(f.seek(1)) # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# f = open('text.txt', 'w+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

#
# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return '  '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done!')


# file_name = 'res_1.txt'
# with open('res_1.txt', 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = nums.split('  ')
# print(lst)
# print(len(lst))


# def longest_world(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         #print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         #print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_world('test.txt'))

# with open('test.txt', 'r', encoding='utf-8') as text:
#     lst = text.read().split()
#     m = max(len(word)for word in lst)
#     print([i for i in lst if len(i) == m])

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# os
# os.path

# import os


# print("Текущая директория:", os.getcwd())
# print(os.listdir(".idea")) # показыввет содержимое папки
#os.mkdir("folder") # создает дерикторию по указанному пути
#os.makedirs("nested1/nested2/nested3")
# os.remove("xyz.txt") # удаляет файл
# os.rename("nested1", "test") # переименовывает папку
#os.rename("test.txt", "test/test1.txt")
# os.renames("text.txt", "text/text1.txt")
# os.rmdir("folder") #удаление папки

# for root, dirs, files in os.walk('test', topdown=True):
#     print("Root: ", root)
#     print("Subdirs: ", dirs)
#     print("Files: ", files)
#     print()


# for root, dirs, files in os.walk('Work'):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f"Директория", root, "удалена")


import os.path


# print(os.path.split(r"C:\Users\Демид\Desktop\python\Work\F5\1.txt"))
# print(os.path.split(r"C:\Users\Демид\Desktop\python\Work\F5\1.txt")[0])
# print(os.path.split(r"C:\Users\Демид\Desktop\python\Work\F5\1.txt")[1])
#
# print(os.path.dirname(r"C:\Users\Демид\Desktop\python\Work\F5\1.txt"))
# print(os.path.basename(r"C:\Users\Демид\Desktop\python\Work\F5\1.txt"))
#
# print(os.path.join("/python", "Work", "F5", "1.txt"))
#
# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for d, fl in files.items():
#     for file in fl:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()


# file_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
# def print_three(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("*" * 40)
#
#
# print_three('Work', topdown=False)
# print_three('Work', topdown=True)


# print(os.path.exists("")) # проверяет наличие файла

# print(os.path.getsize("one.txt")) # возвращает размер файла в байтах
# print(os.path.getatime("one.txt")) # время последнего доступа к файлу в секундах
# print(os.path.getmtime("one.txt")) # возвращает  время последнего изменения файла
# print(os.path.getctime("one.txt")) # возвращает время создания файла

import time
#
# path = r"C:\Users\Демид\Desktop\python\DZ\HW - 3.py"
# size = os.path.getsize(path)
# ksize = size // 1024
# print(ksize)
#
# c = os.path.getctime(path)
# b = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c))
# print(b)


# a = r"C:\Users\Демид\Desktop\python\Work\F2\F21\f211.txt"
# if os.path.exists(a):
#     d, name = os.path.split(a)
#     a = os.path.getctime(a)
#     print(f"{name} ({d}) - last access time {a} sec")
# else:
#     print(f"Файла {a} не существует!")


print(os.path.isfile(r"C:\Users\Демид\Desktop\python\Work\F2\F21\f211.txt")) # возвращает True если путь является файлом
print(os.path.isdir(r"C:\Users\Демид\Desktop\python\Work\F2\F21")) #возвращает True  если путь является директорией

