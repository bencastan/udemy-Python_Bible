x = 1
while x <= 15:
    if x % 2 == 0:
        print(x)
    x = x + 1


L = []
while len(L) < 5:
    name = input("Enter a name: ")
    L.append(name)

print(L)