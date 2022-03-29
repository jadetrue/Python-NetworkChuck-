#Let's start a coffee shop togeth!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot barista

print("Hello, weclome to NetworkChuck coffee!!!")

name = input("What is your name?\n")

if name == "Ben" or  name == "Patricia" or "Loki": 
  evil_status = input("Are you evil?\n")
  good_deeds = int(input("How many good deeds have you done today?\n"))
  if evil_status == "Yes" and good_deeds < 4:
    print("You're not welcome here.")
    exit()
else:
  print("Hello " + name + ", thank you so much for coming in today.")
  
menu = "Americano,\n Cappuccino,\n Latte,\n Mocha,\n Espresso\n"

order = input("What would you like? Here is our menu: " + menu)

price = 3

if order == "Cappuccino":
  price = 12
elif order == "Mocha":
  price = 2
elif order == "Espresso":
  price = 8
elif order == "Latte":
  whipped_cream = input("Would you like whipped cream?\n")
  if(whipped_cream == "Yes"):
    price = 11
  else:
    price = 9
else:
  print("We don't have that here")
  price = 0

print(order + " coming up for you " + name)
number_of_coffees = input("How many coffee's would you like?\n")

total = price * int(number_of_coffees)

if int(number_of_coffees) > 1:
  more_than_one = "'s"
else:
  more_than_one = ""

print("Thank you, " + number_of_coffees + " " + order + more_than_one + " " "coming up for you." + " That'll be £" + str(total))
