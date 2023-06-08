# ------------------------------------------------------------------------
# Program Name: Module 4 Option 2 Critical Thinking
# Author: Michael Masters
# Date:5/14/2023
# ------------------------------------------------------------------------

# Write a program that will provide important statistics for the grades in a class.
# The program will utilize a loop to read five floating-point grades from user input.
# Ask the user to enter the values, then print the following data:
# Average
# Maximum
# Minimum

# Create a loop that asks the user to enter a grade 5 times and store each answer in a list.
counter = 0  # a variable to control the loop.
grade_book = []  # A blank list that will store each grade entered.
while (counter >= 0 and counter < 5):  # runs the loop 5 times, asks for a grade each time, adds each grade to the grade book list.
    grade = float(input("Please enter a grade: "))
    grade_book.append(grade)
    counter = counter + 1

print("You entered:", grade_book)  # Print all of the entered grades

average_score = sum(grade_book) / 5  # Find the average of the scores.
max_score = max(grade_book)  # Find the highest score
low_score = min(grade_book)  # Find the lowest score

# Print it all out
print("The average of your scores is ", average_score,"\n The Lowest score is ",low_score,"\n The highest score is ", max_score,)
