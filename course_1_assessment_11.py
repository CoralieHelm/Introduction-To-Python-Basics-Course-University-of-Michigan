#May 26 2020
#course_1_assessment_11

#seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?

lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]


#I. ✔️ Yes, when we are using the remove method, we are just editing the existing list, not making a new copy.


#seqmut-1-4: What will be the value of a after the following code has executed?

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")


# ['holiday', 'celebrate!', 'company'] Good work!

#seqmut-1-5: Could aliasing cause potential confusion in this problem?

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

#seqmut-1-13: Given that we want to accumulate the total sum of a list of numbers, which of the following accumulator patterns would be appropriate?

nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n


#C. III.✔️ Yes, this will solve the problem.


#seqmut-1-14: Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?

lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1

#D. ✔️ Yes, this will solve the problem.

#seqmut-1-15: Which of these are good names for an accumulator variable? Select as many as apply.




# c, d✔️Correct. Yes, total is a good name for accumulating numbers.


#seqmut-1-16: Which of these are good names for an iterator (loop) variable? Select as many as apply.
# A, C, D ✔️Correct.


#seqmut-1-17: Which of these are good names for a sequence variable? Select as many as apply.

#A,C, D ✔️Correct.


#seqmut-1-18: Given the following scenario, what are good names for the accumulator variable, iterator variable, and sequence variable? You are writing code that uses a list of sentences and accumulates the total number of sentences that have the word ‘happy’ in them.

#D. accumulator variable: total | iterator variable: sentence |sequence variable: sentence_lst ✔️ Yes, this combination of variable names is the clearest.

#Task 1. For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app = []

for char in ael:
    app.append(char)

#You passed: 100.0% of the tests


#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for word in wrds:
    past_wrds.append(word + "ed")
#You passed: 100.0% of the tests
