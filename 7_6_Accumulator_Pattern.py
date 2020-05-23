#May 23 2020
#Python Basics CourseWork University of Miuchigan

#7.6. The Accumulator Pattern

#1.1 Write code to create a list of integers from 0 through 52 and assign that list to the variable numbers.
#You should use a special Python function – do not type out the whole list yourself. HINT: You can do this in one line of code!

numbers = range(0,53)
#You passed: 100.0% of the tests


#1.2Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."

numbs = 0

for string in str1:
    numbs += 1

print(numbs)
#You passed: 100.0% of the tests


#1.3 Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

numbers = list(range(0,41))
sum1 = 0

for s in numbers:
    sum1 += s

print(sum1)
#You passed: 100.0% of the tests



#7.7. Traversal and the for Loop: By Index

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):
    print(n, fruits[n])

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for fruit in fruits:
    print(fruit)

#moreiter-6-1: How many times is the letter p printed by the following statements?
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])

#D. 3 ✔️ idx % 2 is 0 whenever idx is even

import luther.jpg
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

