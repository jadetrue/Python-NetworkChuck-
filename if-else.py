name = input("What is your name?\n")


if name == "Ben": 
  print("You're not welcome here.")
else: 
  print("Hello " + name + ", thank you so much for coming in today.")

if 4 < 3:
  print("Yup it's true")
  print("It's true")
else:
  print("Nope not true")

###Nested if / else statements

name = input("What is your name?\n")

if name != "Ben": 
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes":
    print("You're not welcome here.")
    exit()
  else:
    print("Hello Ben, you're special here")
else:
  print("Hello " + name + ", thank you so much for coming in today.")

# if 4 < 3:
#   print("Yup it's true")
#   print("It's true")
# else:
#   print("Nope not true")

## Nested if's //MESSY WAY
  
# if order == "Americano":
#   price = 2
# if order == "Cappuccino":
#   price = 4
# if order == "Latte":
#   price = 3
# if order == "Mocha":
#   price = 8
# if order == "Espresso":
#   price = 9


## Elif

# if order == "Cappuccino":
#   price = 12
# elif order == "Mocha":
#   price = 2
# elif order == "Espresso":
#   price = 9
# elif order == "Latte":
#   price = 5
# else:
#   print("We don't have that here")