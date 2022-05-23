# JSON

import json


# data = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ("running", "sky diving", "singing"),
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bon",
#             "age": 8
#         }
#     ]
# }

# with open("data_file.json", 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", 'r') as fw:
#     data1 = json.load(fw)
#     print(data1)

# json_string = json.dumps(data, sort_keys=True)
#
# data1 = json.loads(json_string)
# print(data1)


# x = {'name': 'Виктор'}
# y = {'name': 'Виктор'}
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))


# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(personal_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(personal_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        s = ''
        for i in self.marks:
            s += str(i) + ', '
        return f"Студент: {self.name}: {s[:-2]}"

    def add_marks(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @classmethod
    def dump_to_json(cls, stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []

        data.append({"name": stud.name, "marks": stud.marks})
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        s = ''
        for i in self.students:
            s += str(i) + '\n'
        return f"Группа: {self.group}\n{s}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @classmethod
    def change_group(cls, group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @classmethod
    def dump_group(cls, file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_lst = []
            for i in group.students:
                stud_lst.append([i.name, i.marks])
            tmp = {"Students": stud_lst}
            data.append(tmp["Students"])
            json.dump(data, f, indent=2)

    @classmethod
    def upload_group(cls, file):
        with open(file, 'r') as f:
            print(json.load(f))


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# print(st1)
# st1.add_marks(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 5)
# print(st1)
# print(st1.average_mark())
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
sts = [st1, st2]
my_group = Group(sts, "ГК Python")
print(my_group)
my_group.add_student(st3)
print(my_group)
my_group.remove_student(1)
print(my_group)

group22 = [st2]
my_group2 = Group(group22, "ГК Web")
print(my_group2)
Group.change_group(my_group, my_group2, 0)
print(my_group)
print(my_group2)

# Student.dump_to_json(st1, 'student.json')
# Student.dump_to_json(st2, 'student.json')
# Student.dump_to_json(st3, 'student.json')
#
# Student.load_from_file('student.json')
Group.dump_group('group.json', my_group2)
Group.dump_group('group.json', my_group)
Group.upload_group("group.json")
