#May 24 2020
#8.10. The Accumulator Pattern with Conditionals


#example code
phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)


#example 2
s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)


#example 3
s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)


#example 4
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)


#Tasks1

#For each string in the list words, find the number of characters in the string.
#If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0

for word in words:
    if len(word) > 3:
        num_words += 1

#You passed: 100.0% of the tests

#Tasks 2. Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense.
#Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for word in words:
    if word [-1:] == "e":
        past_tense.append(word +"d")
    else:
        past_tense.append(word + "ed")
#You passed: 100.0% of the tests
        
