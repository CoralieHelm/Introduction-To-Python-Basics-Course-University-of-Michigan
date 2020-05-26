#May 25 2020
#9.8. Append versus Concatenate

#Task 1. We can use append or concatenate repeatedly to create new objects. If we had a string and wanted to make a new list, where each element in the list is a character in the string, where do you think you should start?
#In both cases, you’ll need to first create a variable to store the new object.

st = "Warmth"
a = []
for s in st:
    a.append(s)
print(a)
