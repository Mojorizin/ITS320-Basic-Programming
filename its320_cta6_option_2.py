# ------------------------------------------------------------------------
# Program Name: Module 6 Option 2 Critical Thinking
# Author: Michael Masters
# Date:5/28/2023
# ------------------------------------------------------------------------


def make_list():
    """ Create a list from user input until 'done' is entered. It returns the first 10 elements of each list. """
    user_list = []
    while True:
        element = input("Enter a number or type 'done' to quit: ")
        if element == 'done':
            break
        user_list.append(int(element))
    return (user_list[0:10])

def cartesian_product(A, B):
    """ Computes the Cartesian Product of two lists and prints the result. """
    AxB = [(a, b) for a in A for b in B]
    print (AxB)

# Tells the user what this program does and what they need to enter.    
print ( "Hello."
        "\nThis program will ask you to enter two lists."
        "\nOnly the first 10 elements of each list will be kept."
        "\nIt will then show you the cartesian product of the two lists."
    )
    
list_A = make_list() # Create the first list by calling make_list.
list_B = make_list() # Create the second list by calling make_list.
print ("Your first list is: ", list_A)  # Print the first list.
print ("Your second list is: ", list_B)  # Print the second list.
cartesian_product (list_A, list_B) # Compute the cartesian prodcut by calling cartesian_product and print the new list.