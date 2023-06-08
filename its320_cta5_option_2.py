# ------------------------------------------------------------------------
# Program Name: Module 5 Option 2 Critical Thinking
# Author: Michael Masters
# Date:5/21/2023
# ------------------------------------------------------------------------

def add_strings(str_1, str_2):
    """This function adds two strings together. It returns the result"""
    return str_1 + str_2

def reverse_string(str):
    """This function reverses the order of a string. It returns the result"""
    return str[::-1]

# A loop that will have the user enter three strings and store them in a list.
print("Hello! Please enter three strings.")
counter = 1
str_lst = []
while counter <= 3:
    user_input = input("Please enter a string: ")
    str_lst.append(user_input)
    counter = counter + 1

call_1 = add_strings(str_lst[0], str_lst[1])  # Calls add_string function and adds the first two elements of the list.
call_2 = reverse_string(str_lst[2])  # Calls the reverse_string fucntion and reverses the third element of the list.

print("A concatenation of the first two strings is:",call_1,"\n" "Your third string reversed is:", call_2)
