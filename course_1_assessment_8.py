#May 25 2020
#course_1_assessment_8

#Questions
#seqmut-1-5: Could aliasing cause potential confusion in this problem?

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
#A. Yes ✔Yes, b and z reference the same list and changes are made using both aliases.


#seqmut-1-6: Could aliasing cause potential confusion in this problem?
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"


#B. No ✔️ Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.

#seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?

lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
#A. 1 ✔️ Yes, when we are using the remove method, we are just editing the existing list, not making a new copy.


#seqmut-1-7: Which of these is a correct reference diagram following the execution of the following code?

x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']

#d. IV ✔️ Yes, the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first version makes a new object entirely and reassigns to obj. The second version changes the original object so that the contents of object_two are added to the end of the first.

#seqmut-1-8: Which of these is a correct reference diagram following the execution of the following code?

sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)

#A. I ✔️ Yes, when we make our own diagrams we want to keep the old information because sometimes other variables depend on them. It can get cluttered though if there is a lot of information.
