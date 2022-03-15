import re

# Задание 1
# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимум ежемесячных осадков"
# reg = r"\d+/\d+/\d+"
# print(re.findall(reg, s))

# Задание 2
def password(pas):
    return re.findall(r'[\wа-я-@]{6,18}', pas, re.I)


print(password('my-p@ssw0rd'))
