import random

questions = ['Why is the sky blue',
             'How old are you',
             'Why is a tree',
             'Where are all the dinosaurs']

choice = random.choice(questions)
answer = input(choice + "?: ").strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()
print("Oh, ok then.")