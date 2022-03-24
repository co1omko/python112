import re


# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print("Выпрямленный список: ", union(names))


s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78,"
reg = r'\+*7\s*[(]*\w{3}[)]*\s*\w{3}\s*-*\w{2}\s*-*\w{2}'
print(re.findall(reg, s))

