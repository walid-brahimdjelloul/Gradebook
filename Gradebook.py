last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# My code below: 
## Create a list called subjects 
subjects = ['physics', "calculus", "poetry", "history"]

## Create a list called grades
grades = [98, 97, 85, 88]

## Manually (without any methods) create a two-dimensional list to combine subjects and grades.
gradebook = [['physics', 98], ['calculus', 97], ["poetry", 85], ["history", 88]]
## print
print(gradebook)

## add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.
gradebook.append(["computer science", 100])

## My grade for "visual arts" just came in! I got a 93!
gradebook.append(['visual arts', 93])

##Our instructor just told us they made a mistake grading and am rewarding an extra 5 points for our visual arts class.
gradebook[-1][-1] = 98
print(gradebook)

## I decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.
gradebook[2].remove(85)
print(gradebook)

## add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append('Pass')
print(gradebook)

##Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
