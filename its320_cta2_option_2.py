#------------------------------------------------------------------------
# Program Name: Module 2 Option 2 Critical Thinking
# Author: Michael Masters
# Date:4/23/2023
#------------------------------------------------------------------------

# Get the user input and store in variables.
car_make = input("Please enter car brand:")  # store as string.
car_model = input("Please enter car model:")  # store as string.
avg_mpg = float(input("Please enter the estimated miles per gallon:"))  # store as a float.
car_year = int(input("Please enter the model year:"))  # store as an integer. I don't think the user would actually spell out the year. They should write 2017 not twenty-seventeen or sometinng like that...
odometer_start = int(input("Please enter the starting odometer reading:"))  # store as int. I don't think the user would enter a decimal for this....
odometer_end = int(input("Please enter the ending odometer reading:"))  # store as int. I don't think the user would enter a decimal for this...

# Store the variables in a dictionary.
user_car_dictionary = {
    "make": car_make,
    "model": car_model,
    "year": car_year,
    "beginning odometer": odometer_start,
    "ending odometer": odometer_end,
    "estimated mpg": avg_mpg,
}

# Calculate total miles.
total_miles = (user_car_dictionary["ending odometer"] - user_car_dictionary["beginning odometer"])

# Print the dictionary.
print(user_car_dictionary)
