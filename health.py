import random

health = 50
difficulty = 1
potion_health = int(random.randint(25, 50) / difficulty)
print("Your starting health is {}".format(health))
health = health + potion_health

print("The potion has {} health points.".format(potion_health))

print('After drinking the potion your health is {}'.format(health))