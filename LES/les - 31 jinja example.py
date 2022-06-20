from jinja2 import Template


# per = {'name': "Igor", 'age': 28}
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# per = Person("Igor", 28)
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# data = "{% raw %}Строка, с назвваниеи {{ name }}. Со значением {% endraw %}"
# tm = Template(data)
# msg = tm.render(name="Igor")
# print(msg)


# link = "<a href='#'>Ссылка<\a>"
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
# print(msg)git 