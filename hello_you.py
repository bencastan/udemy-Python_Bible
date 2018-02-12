# Ask user for name
name = input('What is you name?: ')
# Ask user for age
age = input("What is your age in years?: ")
# Ask user for city
city = input("What city do you live in?: ")
# Ask user what they enjoy
hobby = input("What are your hobbies?: ")
# Create output text
output = "Hello {}. You are {} years old.".format(name, age)
output = output + " You live in {} and you like {}.".format(city, hobby)
# Print output to screen
print(output)