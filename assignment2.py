# Intro to Programming Using Python - Assignment #2
# Completed by: 


# 1. Create three dictionaries:
#   - Each one will contain information about a particular student: Steve, Alice and Tyler
#   - Give each dictionary the keys 'name', 'homework', 'quizzes', and 'tests'
#   - Set the value of the 'name' key to the name of the student (e.g. Steve's name should be "Steve")
#   - The other keys should be empty lists (we'll fill them in next)
#   - Make sure to assign each dictionary to a variable so you can refer to them individually later (eg. steve, alice and tyler)


# 2. Now fill in the dictionaries above with the following scores:
# Steve
#   Homework: 90, 97, 75, 92
#   Quizzes: 88, 40, 94
#   Tests: 75, 90
# Alice
#   Homework: 100, 92, 98, 100
#   Quizzes: 82, 83, 91
#   Tests: 89, 97
# Tyler
#   Homework: 0, 87, 75, 22
#   Quizzes: 0, 75, 78
#   Tests: 100, 100


# 3. Create a list called students that contains your three students


# 4. For each student in your students list, print out that student's data as follows:
#   - print out the student's name
#   - print out the student's homework
#   - print out the student's quizzes
#   - print out the student's tests 


# 5. Write a function to calculate the average of a list
#   a. Define a function called average() that has one argument, numbers (which will be a list)
#   b. Inside the function, use the built-in Python function sum() to add up the numbers variable, store the result in a variable called total
#   c. Divide total by the length of the numbers list (use the built-in Python len() function)
#   d. Return the result 


# 6. Write a function to calculate the weighted average score for a student
#   a. Define a function called get_weighted_average() that takes one argument: student (a dictionary)
#   b. Inside the function create a variable (homework) that stores the average of the student's homework 
#      (Remember you can get this out of the dictionary with student['homework'] and then use your average() function)
#   c. Repeat step 2 for "quizzes" and "tests"
#   d. Homework is 10%, quizzes are 30%, and tests are 60% . Multiply the three averages by their weights and return the sum. 


# 7. Write a function to convert a grade into a letter grade
#   a. Define a function called get_letter_grade() that has one argument called score. score will be a number.
#   b. Inside your function, test score using a chain of if / elif /else statements like this:
#       - If score is 90 or above: return “A"
#       - If score is 80 or above: return “B"
#       - If score is 70 or above: return “C"
#       - If score is 60 or above: return “D"
#       - Otherwise: return “F"
#   c. Test your function by calling your get_letter_grade function with the result of get_weighted_average(steve). Print the resulting letter grade.


# 8. Write a function to calculate the class average
#   a. Create a function called get_class_average() that has one argument, students. You can expect students to be a list containing students.
#   b. Make an empty list called results inside the function
#   c. For each student in students, calculate get_weighted_average(student) and then call results.append() with that result
#   d. Finally, return the average of the results


# 9. Test it all out
#   - Print out the result of calling get_class_average with your students list.
#   - Then print out the results of get_letter_grade with the class's average
