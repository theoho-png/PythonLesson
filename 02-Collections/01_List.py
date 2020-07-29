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
print(subjectList)

#Deleting List Element
print(subjectList.pop(1)) #Method 1: Pop
print(subjectList)

del subjectList[0] #Method 2: Del
print(subjectList)

subjectList.remove("Music") #Method 3: Remove
print(subjectList)
