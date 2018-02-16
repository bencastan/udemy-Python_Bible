known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

# print(len(known_users))
while True:
    print("Hi! my name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}, how are you today? ".format(name))
        remove = input("would you like to be removed from the system?: (y/n) ").strip().lower()
        if remove == 'y':
            known_users.remove(name)
        elif remove == "n":
            print("I did not want you to leave anyway.")
        print()
    else:
        print("Sorry I don't know you {}.".format(name))
        add = input("Would you like to be added to the system?: (y/n)").strip().lower()
        if add == 'y':
            known_users.append(name)
        if add == 'n':
            print("Ok, see you later.")
        print()