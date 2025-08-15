#Basic Functions
def greet(): #Define Functions
    print("Hello Everyone")

greet() #call Functions

#Parameters Functions
def greet_name(name):
    print("Hello",name)

greet_name("Pei")

#Without Functions
User = "Pei"
print("Hello",User,"I hope you will enjoy my website.")

User = "Priew"
print("Hello",User,"I hope you will enjoy my website.")

User = "Tag"
print("Hello",User,"I hope you will enjoy my website.")

#With Functions
def greet_user(user):
    print("Hello",User,"I hope you will enjoy my website.")

greet_user("Pei")
greet_user("Priew")
greet_user("Tag")

#Return Functions
def power (base,exponent):
    return base * exponent

print(power(2,2))