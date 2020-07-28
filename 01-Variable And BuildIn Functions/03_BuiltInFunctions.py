#Lesson 01 - Part 03
#Built-in Functions

#Print Statement
print("This print statment is working.")

#Input Statement
print("Please enter your name.")
name = input()

#Changing data type
age = int(input("Please enter your age."))
#!!!The deafult data type for input is String.
#Therefore, we need to convert the age to int 

#Checking variable data type
#type(myVar)
print("The age you just enter is a " + str(type(age)))

#-------------------------------------#

currentYear = 2020
birthYear = currentYear - age

#Summary

print("Hello " + name +  "\n" + 
"You are born in " + str(birthYear))
