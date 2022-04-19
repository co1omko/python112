# f = open("file3.txt", 'w').write(open("file1.txt", 'r').read() + open("file2.txt", 'r').read())


# text = "первая строка\nстрока номер два\nтретья строка\n4 строка"
# with open("string.txt", 'w') as f:
#     f.write(text)

f = open('string.txt')
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, len(i), 'симв.', word, 'сл.')
print(line, 'стр.')
f.close()

