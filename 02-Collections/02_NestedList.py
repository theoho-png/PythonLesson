#Lesson 02 - Part 02
#Neseted List

#Declaring a List
subjectList = ["English", "Math", "IT", ["Biology", "Chemistry", "Physics"]]
print(subjectList)

#Accessing Nested List Element
print(subjectList[3][2])

#Changing List Element
subjectList[3][2] = "Psychology" #Replaced Physics with Psychology
print(subjectList)

#Adding Nested List Element
subjectList[3].append("PE") #Method 1: append

subjectList[3].insert(2,"Physics") #Method 1: insert
print(subjectList)

#-------------------------------------#

#Adding a List into a List
languageStudy = ["English", "Math"]
print(languageStudy)
languageSubject = ["Chinese", "Japanese", "French", "Spanish"]
languageStudy.insert(2, languageSubject)
print(languageStudy)

#-------------------------------------#

#Deleting List Element
print(subjectList[3].pop(3)) #Method 1: Pop
print(subjectList)

del subjectList[3][3] #Method 2: Del
print(subjectList)

subjectList[3].remove("Physics") #Method 3: Remove
print(subjectList)
