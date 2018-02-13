# Ask user for email address
email = input("What is your email address? : ").strip()
# Slice out the user name
user = email[:email.index('@')]
# Slice out the domain name
domain = email[email.index('@')+1:]
# Format the message
output = "Your user name is {} and your domain is {}".format(user, domain)
# Display the output of the message
# print(email)
# print(user)
# print(domain)
print(output)
