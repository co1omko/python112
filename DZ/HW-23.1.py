# f = open("file3.txt", 'w').write(open("file1.txt", 'r').read() + open("file2.txt", 'r').read())


# text = "первая строка\nстрока номер два\nтретья строка\n4 строка"
# with open("string.txt", 'w') as f:
#     f.write(text)

f = open('string.txt', 'r')
for line in f.readlines():
    print(len(line), 'символов')
f = open('string.txt', 'r')
print(len(f.readline().split()))
with open('string.txt', 'r') as f:
    print(len(f.readlines()), 'str')
