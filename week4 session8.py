# def z():
#     x=int(input("number: ", ))
#     y=int(input("number: ", ))
#     print(x*y)
#
# z()
#
# #there is an other type of fuctionsc called lamda functions
#
# x = lambda a : a**2
# print(x(3))
#
# def sumup(x, y):
#     return x**y
# print(sumup(3,9))

#arbitrary arguments, "*args"

def my_function(*car):
    print("My favorite car is:", car[2])

my_function("red", "blue","magenta")