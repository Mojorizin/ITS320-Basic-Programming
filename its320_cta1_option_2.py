#Read two integers and print three lines. The first line should contain integer division, //, the second line should contain float division, /, and the third line should contain modulo division, %. You do not need to perform any rounding or formatting operations.

#Input Format The first line contains the first integer. The second line contains the second integer.

#Output Format Print the three lines as described above.

#Sample Input43

#Sample Output11.33333333333333331

# Algorithm: 
#   1) Get the inputs from the user:
#       Print text: Input first number
#           -store number in an integer variable "num1"
#       Print text: Input second number
#           - store number in a second integer variable "num 2"
#
#   2) Do the math:
#       Divide num1 by num2 using integer divison, "//", store answer in a variable called answer1.
#       Divide num1 by num2 using float division, "/", store answer in a variable called answer2.
#       Divide num1 by num2 using modulo divison, "%", store answer in a variable called answer 3.
#
#   3) Print the results on separate lines:
#       Print the below text:
#           - Line 1: print answer1
#           - Line 2: print answer2
#           - Line 3: print answer3


print("Please input the first number:")
num1=int(input())
print("Please input second number (do not enter 0):")
num2=int(input())

answer1=num1//num2
answer2=num1/num2
answer3=num1%num2

print('Your first number integer divided by your second number is:', answer1)
print('Your first number float divided by your second number is:', answer2)
print('Your first number modulo divided by your second number is:', answer3)