#------------------------------------------------------------------------
# Program Name: Vehicle Inventory Program.
# Author: Michael Masters
# Date:6/11/2023
#------------------------------------------------------------------------

inventory_dict = {} # A dictionary that stores the car objects. The item number is the key, the car object is the value.

class Car:

    """ This Class can be called to create new car objects. 
        It has methods to return the car object info as a string. 
        It also has a method to add the Car object to the vehicle inventory dictionary with an item number. """

    def __init__ (self):

        """ Gets the needed input from the user about the car and creates an instance of the Car class. """

        self.__make = str (input ("Please enter car make: "))
        self.__model = str (input ("Please enter car model: "))
        self.__color = str (input ("Please enter car color: "))
        self.__year = int (input ("Please enter the year the car was made: "))
        self.__mileage = int (input ("Please enter the car's avg miles per gallon: "))
    
    def info (self):

        """ Returns a string of the attributes associated with the class instance. """
        
        return str ("Make: {} | Model: {} | Year: {} | Color: {} | Mileage: {} mpg" .format (self.__make, self.__model, self.__year, self.__color, self.__mileage))
        
    def add (self):

        """ Assigns an inventory number to the class instance. 
            The inventory number + str info returned from the "info" method is added to the dictionary as a key/value. 
            A success message is printed to the terminal so the user knows something happened. """

        inventory_num = len (inventory_dict) + 1

        inventory_dict [inventory_num] = new_car

        print ("\n Item number: {} | {} | added to the inventory." .format (inventory_num, new_car.info()))

def view_inventory ():

    """ Displays the current inventory to the user. 
        If there is nothing in the inventory, a message is displayed and the user is returned to the menu. """

    if len (inventory_dict) == 0:

        print ("\n The inventory is empty.")
    
    else:
         
        for (inventory_num, car) in inventory_dict.items ():

            print ("\n Item number: {} | {}" .format (inventory_num, car.info()))

def remove_car ():

    """ Shows the user the current inventory. 
        If there is nothing, displays error message and user is returned to menu. 
        Asks the user to choose which item to remove. That item is then deleted from the dictionary. 
        A message is printed to the terminal so the user knows something happened. """

    if len (inventory_dict) == 0:
        
        print ("\n There is nothing to delete because the inventory is empty.")

    elif len (inventory_dict) >= 1:
            
            view_inventory ()
            
            item_select = int (input ("\n Which item do you want to remove? "))

            if item_select in inventory_dict:

                del inventory_dict [item_select]

                print ("\n Item number {} was removed from the inventory." .format (item_select))
            
            elif item_select not in inventory_dict:

                    print ("\n That item is not in the inventory.")

def update_car ():

    """ Shows the user the current inventory. 
        If there is nothing, displays error message and user is returned to menu. 
        Asks the user to choose which item to update. That item is then deleted from the dictionary.
        A new instance of the Car class is created and added to the dictionary with the original inventory number. 
        A message is printed to the terminal so the user knows something happened. """
    
    if len (inventory_dict) == 0:
        
        print ("\n There is nothing to update because the inventory is empty.")

    elif len (inventory_dict) >= 1:
        
        view_inventory ()
            
        item_select = int (input ("\n Which item do you want to update? "))

        if item_select in inventory_dict:

            print ()
            new_car = Car ()
            inventory_num = item_select
            inventory_dict [inventory_num] = new_car

            print ("\n Item number {} was updated." .format (item_select))
            
        elif item_select not in inventory_dict:

            print ("\n That item is not in the inventory.")

def inventory_file ():

    """ Writes the inventory to a .txt file named vehicle_inventory and exits the program. """
    
    with open ("vehicle_inventory.txt", "w") as file:
        
        for inventory_num, car in inventory_dict.items ():

            file.write ("Item number: {} | {} \n" .format (inventory_num, car.info()))



# ------------------------------ Begin Program ------------------------------ #


menu_choice = '' # A variable to control the menu choice from the user. Set to an initial value to start the loop.

while menu_choice != 6: # Runs the program until the user enters 5 or 6.

        # Menu for the user to select actions from.
        # Has exception handling if the user enters something other than an integer or an integer that is not a menu choice.
    try:
        print()
        print ("**************************************************************")
        print ("* 1. View current inventory.                                 *")
        print ("* 2. Add a new car to the inventory.                         *")
        print ("* 3. Remove a car from the inventory.                        *")
        print ("* 4. Update an existing car in the inventory.                *")
        print ("* 5. Print the inventory to vehicle_inventory.txt and exit.  *")      
        print ("* 6. Exit.                                                   *")
        print ("**************************************************************")
        print()

        menu_choice = int (input ("Please make a selection: ")) # Asks the user what they want to do, and updates the menu_choice variable with the integer selection.

        if (menu_choice <= 0) or (menu_choice >= 7):
            
            raise ValueError ("That is not a valid entry. Please enter a number between 1-6. \n")
           
    except ValueError: print ("That is not a valid entry. Please enter a number between 1-6. \n")

    if menu_choice == 1: # Show the inventory by calling the view_inventory function.

        view_inventory ()
    
    elif menu_choice == 2: # Add a new car to the inventory by printing a fresh line, creating an instance of the Car class with user input, adding that instance to the vehicle inventory dictionary by calling the "add method."
        
        print ()
        new_car = Car ()
        new_car.add ()
        
    elif menu_choice == 3: # Remove a car from the inventory by calling the remove_car function.
        
        remove_car ()

    elif menu_choice == 4: # Update an existing car attributes by calling the update_car function.
        
        update_car ()

    elif menu_choice == 5: # Print the inventory to a list by calling the inventory_file function. Exit the program.
        
        inventory_file ()
        break
        
    elif menu_choice == 6: # Exit the program.
        break