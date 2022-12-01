### JHL Development Robot Coffee Barista
### Learning In Python Part 1 

Business = "Jacks Coffee House" ## Name Of The Buisness

price = 5 ## Price Of Each Coffee (All Coffees Are The Same Price Currently)

menu = "Black Coffee, Espresso, Light and Sweet,\n" + "Ice Coffee, and Cappucino" ## Items Listed On Menu

print("Hello Welcome To " + Business + "!!!")

print("Thank you so much for coming in today!!!")

name = input("What is your name?\n") ## Persons Name

order = input("Nice to meet you " + name + "!!!" + " What Would You Like To Order?\n" + "This Is What We Have On Our Menu For Today:\n" + menu + "\n") ## What The Person Ordered 

quantity = input("How much " + order + " Would you like?\n")

total = price * int(quantity)

print("Sounds great " + name + " Your total is going to be " + "$" + str(total) + "\n" + "we will get your " + quantity + " " + order + " right up for you!!!" + " we will call you to the register when your \n" + quantity + " " + order + " is ready!!!")

#print("Sounds Great " + name + "!!!\n" + "We will get your " + quantity + " " + order + " right up for you!! \n" + "We will call you up to the register when your \n" + order +" is ready!!!")

print("Hey " + name + " Your " + quantity + " " + order + " is ready at the counter!!!\n" + "Thank you for choosing " + Business + "!!!\n" + "Have a good day, and we hope to see you soon!!!" )







