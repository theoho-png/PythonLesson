#Lesson 01 - Part 02
#String Variable

#Declaring Variable
myText = "Hello "
myName = 'T'

myName = 'Theo' #Changing value in a variable
print(myName)

#-------------------------------------#

#Use of Quotations
singleQuotes = 'This is a String!'
doubleQuotes = "But I can't use quotation marks."

tripleQuotes= '''Triple Quotes can be used
- As a comment
- Or as a String
(Triple Quotes also reduces the need for a newline character)
'''

#Triple Quotes as a comment
'''Remove the bullet point and replaces the whole section with a single paragraph.'''
print(tripleQuotes)

#-------------------------------------#

#String Concatenation
print(myText + myName)
print(myName * 5)

#Error in String Concatenation
#print(myName + 5)
print(myName + "5")