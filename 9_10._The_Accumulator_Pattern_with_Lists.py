#Ma7 25 2020
#9.10. The Accumulator Pattern with Lists


#seqmut-9-1: What is printed by the following statements?

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)
A. [4,2,8,6,5]
B. [4,2,8,6,5,5]
C. [9,7,13,11,10]
D. Error, you cannot concatenate inside an append.

# C. ✔️ Yes, the for loop processes each item of the list. 5 is added before it is appended to blist.

#seqmut-9-2: What is printed by the following statements?

lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)
A. [8,5,14,9,6]
B. [8,5,14,9,6,12]
C. [3,0,9,4,1,7,5]
D. Error, you cannot concatenate inside an append.
# B. ✔️ Yes, the for loop processes each item in lst. 5 is added before lst[i] is appended to blist.


#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []

for verb in verbs:
    ing.append(verb + "ing")
#You passed: 100.0% of the tests


#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
    numbs = [5, 10, 15, 20, 25]
newlist = []

for numb in numbs:
    newlist.append(numb + 5)
#You passed: 100.0% of the tests

#Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.
for numb in range(len(numbs)):
    numbs[numb] += 5
    
#You passed: 100.0% of the tests

#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
    lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

larger_nums = []

for num in lst_nums:
    larger_nums.append(num*2)

#You passed: 100.0% of the tests
