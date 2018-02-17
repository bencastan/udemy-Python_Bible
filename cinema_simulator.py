# Create dictionary to store data about films
films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}

while True:
    print("Films Available: ")
    for i in films:
        print(i)
    print()
    choice = input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        # Check user age
        if age >= films[choice][0]:
            # Check enough seats
            if films[choice][1] >0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Not enough seats available")
        else:
            print("You are too young to see that film! ")
    else:
        print("We don't have that film!")
    print()