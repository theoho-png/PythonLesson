#Lesson 02 - Part 01
#List

#Declaring a List
numberList = [2, 4, 6, 8]
nameList = ["Michelle", "Nate"]
theoList = ["Theo", 2000, "October", True]
print(numberList)

#Accessing List Element
print(nameList[0])

#Changing List Element
nameList[0] = "Theo"
print(nameList)

#Adding List Element
nameList.append("Michelle")
print(nameList)

#-------------------------------------#

subjectList = ["English", "Math", "Science", "IT", "Music"]

#Deleting List Element
print(subjectList.pop(1)) #Method 1: Pop
print(subjectList)

subjectList.remove("Science") #Method 2: Remove
print(subjectList)

del subjectList[0] #Method 3: Del
print(subjectList)
