# s = "Замените в этой строке все появления буквы 'о' на букбу 'О', кроме первого и последнего вхождения"
# a = s[:s.find('о')+1]
# b = s[s.rfind('о'):]
# c = (s[s.find('о')+1:s.rfind('о')])
# s = a + c.replace('о', 'О') + b
# print(s)

s = 'I am learning Python. hello, WORLD!'
a = s[:s.find('h')]
b = s[s.rfind('h')+1:]
c = s[s.find('h'):s.rfind('h')+1]
s = a + c[::-1] + b
print(s)