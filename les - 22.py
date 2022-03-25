# Файлы
# print(f.closed)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)


# f = open(r'C:\Users\Демид\Desktop\python\txt.txt', 'r') # r чтение файла
# print(f.read())
# f.close()

f = open(r'test.txt', 'r')
print(f.readline())
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

