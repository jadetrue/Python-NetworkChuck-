#Let's start a coffee shop togeth!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot barista

print("Hello, weclome to NetworkChuck coffee!!!")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today.")

menu = "Americano,\n Cappuccino,\n Latte,\n Mocha,\n Espresso\n"

order = input("What would you like? Here is our menu: " + menu)

print(order + " coming up for you " + name)

price = 3

number_of_coffees = input("How many coffee's would you like?\n")

total = price * int(number_of_coffees)

print("Thank you, " + number_of_coffees + " " + order + "'s coming up for you." + " That'll be £" + str(total))