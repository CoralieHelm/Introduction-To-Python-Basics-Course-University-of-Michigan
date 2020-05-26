#May 26 2020
#9.11. The Accumulator Pattern with Strings¶

#seqmut-10-1: What is printed by the following statements:

s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

#Tasks 2. For each character in the string already saved in the variable str1, add each character to a list called chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for string in str1:
    chars.append(string)
#You passed: 100.0% of the tests

#Tasks 3. Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
    
output = ""
for out in range(35):
    output = output + "a"
#You passed: 100.0% of the tests
