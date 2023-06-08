# ------------------------------------------------------------------------
# Program Name: Module 3 Option 1 Critical Thinking
# Author: Michael Masters
# Date:5/7/2023
# ------------------------------------------------------------------------

# Implement a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO in that year.
# Use the following table that describes the estimated value of a GTO at different times since 1962.

# 1962-1964	$18,500
# 1965-1968	$6,000
# 1969-1971	$12,000
# 1972-1975	$48,000
# 1976-1980	$200,000
# 1981-1985	$650,000
# 1986-2012	$35,000,000
# 2013-2014	$52,000,000

# ------------------------------------------------------------------------

# Ask the user for a year
year = int(input("Please enter the year your Ferrari 250 GTO was made to display the car's value: "))

# Check the year entered against each set of years and print the corresponding dollar value.
# If a year is entered outside of 1962 - 2014, print "there were no 250 GTO's that year."
if (year >= 1962) and (year <= 1964):
    print("$18,500")
elif (year >= 1965) and (year <= 1968):
    print("$6,000")
elif (year >= 1969) and (year <= 1971):
    print("$12,000")
elif (year >= 1972) and (year <= 1975):
    print("$48,000")
elif (year >= 1976) and (year <= 1980):
    print("$200,000")
elif (year >= 1981) and (year <= 1985):
    print("$650,000")
elif (year >= 1986) and (year <= 2012):
    print("$35,000,000")
elif (year >= 2013) and (year <= 2014):
    print("$52,000,000")
else:
    print("There are no Ferrari 250 GTOs in the year you entered.")
