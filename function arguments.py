def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


print(about("Ben", 57, "Dragons"))


def about(name, age, likes = "Python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence


print(about("Ben", 57))


# unPack and Pack

# Unpack
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)


# Pack
def new_add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print(new_add(1, 2, 3, 4, 5, 6, 7, 8, 9))

dictionary = {"name": "ben", "age": 26, "likes": "school"}
print(about(**dictionary))


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


foo(ben="Male", thomas="Girl")
