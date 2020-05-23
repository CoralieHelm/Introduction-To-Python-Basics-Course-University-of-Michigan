#7.12. 👩‍💻 Keeping Track of Your Iterator Variable and Your Iterable¶

#iter-7-1: What is the type of your iterable?

n = ["word", "phrase", 8, ("beam")]
for item in n:
    print(item)
# B. list  Yes, the iterable is n, and it is a list.


#iter-7-2: What is the type of your iterable?

t = "couch"
for z in t:
    print(z)
#A. String ✔️ Yes, the iterable in this example is a string

#iter-7-3: What is the type of your iterable?
y = 18
#for z in y:
    #print(z)
    

    
#E. error ✔️ Yes, Python is unable to iterate over integers and floats.


#iter-7-4: What is the type of your iterable?
t = ("couch", "chair", "washer", "dryer", "table")
for z in t:
    print(z)
#C. Tuple. ✔️ Yes, the iterable in this situation is a tuple.

#iter-7-5: What is the type of your iterable?
t = "couch"
for z in t:
    print(z)
#A. string ✔️ Correct! The iterable is a string.

#iter-7-6: What’s the type of your iterator variable?

t = ["couch", "chair", "washer", "dryer", "table"]
for z in t:
    print(z)

#A. string ✔️ Correct! Every item in the iterator variable will be a string.

#iter-7-7: What’s the type of your iterator variable in the first iteration?
t = [9, "setter", 3, "wing spiker", 10, "middle blocker"]
for z in t:
    print(z)

#D. integer ✔️ Yes, the first item in t is an integer.

#iter-7-8: What’s the type of your iterator variable in the second iteration?

t = [9, "setter", 3, "wing spiker", 10, "middle blocker"]
for z in t:
    print(z)

#A ✔️ Yes, the second item in t is a string.

#iter-7-9: What’s the type of your iterator variable in the final iteration?

red = "colors"
for blue in red:
    print(blue)
#A. string ✔️ Yes, the last value stored in the iterator variable is a string.

#7.9. 👩‍💻 Printing Intermediate Results¶
w = range(10)

tot = 0
print("***** Before the For Loop ******")
for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)
print("***** End of For Loop *****")
print("Final total:", tot)
