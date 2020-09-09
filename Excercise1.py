#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Give me your name: ")
age = int(input("Give me your age: "))
remaining_years = 100 - age
Year100 = 2020 + remaining_years              #The year in which age 100 is reached
Number = int(input("Give number of times to print msg: "))
print(("Your name is "+name+" and you will turn 100 in the year:"+str(Year100)+"\n")*Number)
