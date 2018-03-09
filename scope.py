a = 1000


def f1():
    ab = a + 10
    print(ab)


def f2():
    a = 50
    print(a)


def f3():
    # Overwrite the global variable 'a' with the global keyword to force the change
    # Has to be done on two lines as below
    global a
    a = 101


f1()
f2()
print(a)
f3()
print(a)
