#course_1_assessment_5
#Due: 2020-05-25 
#Description: Assessment for Lists and Strings lesson.

#Questions

#sequences-10-1: What will the output be for the following code?

let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)
A. zpzpzpzpzp
B. zzzzzppppp
C. pzpzpzpzpz
D. pppppzzzzz
E. None of the above, an error will occur.

#✔️C. Yes, because let_two was put before let, c has "pz" and then that is repeated five times.


#Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.

rts = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

last = sports[-3:]


#You passed: 100.0% of the tests

#Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy.

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = by + " " + az + "" + io + ", " + qy 



#You passed: 100% of the tests


#sequences-10-2: What will the output be for the following code?

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)
A. ['travel', 'lights', 'moon']
B. ['world', 'travel', 'lights']
C. ['travel', 'lights']
D. ['world', 'travel']

#✔️C.  Yes, python is a zero-index based language and slices are inclusive of the first index and exclusive of the second.


#sequences-10-3: What is the type of m?

l = ['w', '7', 0, 9]
m = l[1:2]
A. string
B. integer
C. float
D. list

#✔️D) Yes, a slice returns a list no matter how large the slice.

#sequences-10-4: What is the type of m?

l = ['w', '7', 0, 9]
m = l[1]
A. string
B. integer
C. float
D. list

#✔ A)️ Yes, the quotes around the number mean that this is a string.

#sequences-10-5: What is the type of x?

b = "My, what a lovely day"
x = b.split(',')
A. string
B. integer
C. float
D. list

#✔️D. Yes, the .split() method returns a list.

#sequences-10-6: What is the type of a?

b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
A. string
B. integer
C. float
D. list

#✔️A.  Yes, the string is split into a list, then joined back into a string, then split again, and finally joined back into a string.
