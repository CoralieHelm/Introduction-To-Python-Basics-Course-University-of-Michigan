'''course_1_assessment_6
Due: 2020-05-25 01:19:00
Description: Assessment for Way of Programmer Week 2 lesson.

Questions:'''

#1. Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"
for str in my_str:
    print(str)
​#You passed: 100.0% of the tests


#2. Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.


several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for element in several_things:
    print(element)

for typ in several_things:
    print(type(typ))
#You passed: 100.0% of the tests

#3. Write code that uses iteration to print out the length of each element of the list stored in str_list.


str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for lengths in str_list:
    print(len(lengths))
#You passed: 100.0% of the tests



#4. Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0

for element in original_str:
    num_chars += 1
#You passed: 100.0% of the tests
​




#5. addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"
sum_val = 0

addition_int = addition_str.split("+")

for i in addition_int:
    sum_val += int(i)
#You passed: 100.0% of the tests



#6. week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

​

#7 Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f_split = week_temps_f.split(",")

temps_f = 0

for temp in week_temps_f_split:
    temps_f += float(temp)

avg_temp = temps_f / len(week_temps_f_split)
#You passed: 100.0% of the tests



#8. Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
nums = list(range(0,68))
#You passed: 100.0% of the tests


#9.  original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_str_list = original_str.split(" ")
num_words_list = []

for element in range(len(original_str_list)):
    num_words_list.append(len(original_str_list[element]))
#You passed: 100.0% of the tests




#10. Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett = ""

for let in range(7):
    lett += "b"
#You passed: 100.0% of the tests




#11. Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

import turtle

wn = turtle.Screen()
wn.bgcolor("black")



shape = turtle.Turtle()
shape.speed(5)
shape.pensize(5)
distance = 25


for color_shape in ["Beige","Blue", "Brown", "Coral", "Cyan", "Green", "Grey", "Lavender", "Lime", "Magenta", "Maroon","Navy", "Olive", "Orange", "Pink", "Purple", "Red", "Teal", "White", "Yellow"]:
    shape.color(color_shape)
    shape.right(90)
    shape.forward(distance)
    distance += 15


wn.exitonclick()




