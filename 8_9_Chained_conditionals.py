#May 24 2020
#8.9. Chained conditionals

#Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False. You aren’t you?”.
#Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output. If neither are in str1, assign “Neither true nor false!” to output.

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren’t you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false!"
#You passed: 100.0% of the tests

#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass,
#then check that you’ve matched up the strings exactly.

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []



for rain in percent_rain:
    if rain > 90:
        resps.append("Bring an umbrella.")
    elif rain > 80:
        resps.append("Good for the flowers?")
    elif rain  > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")
            
