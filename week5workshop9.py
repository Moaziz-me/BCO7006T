# class Student:
#     def __init__(self, name, number, age):
#         self._name = name
#         self._scores = []
#         self._age = age
#         for count in range(number):
#             self._scores.append(0)
#     def getAge(self):
#         return self._age
#     def setAge(self, age):
#         self._age=age
#     def getNAme(self):
#         return self._name
#     def setScore(self, i, score):
#         self._scores[i-1]=score
#     def getAverage(self):
#         return sum(self._scores)/len(self._scores)
#     def getHighScore(self):
#         return max(self._scores)
#     def __str__(self):
#         return "name: "+self._name + "\nScores: "+\
#     "".join(map(str, self._scores))
#
# s = Student("Moh", 4, 50)
# s.setScore(1, 74)
# print(s.getAge())
# print(s)

# class MyClass:
#     x = 5
# p1=MyClass()
# print(p1.x)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name, self.age)
#
#
# p1 = Person("John", 36)
# p1.myfunc()
# del p1.age

# parent and child class

# class Person:
#     def __inti__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# x = Person("Ahmad", "Mahmood")
# x.printname()

class Student(Person):
    pass