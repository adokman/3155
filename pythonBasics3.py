# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# import regular expression module
import re
def ends_with_consonant(in_str):    #defining the fucntion "ends_with_consonant"
found1 = re.search(r'[AEIOU]\b', in_str)   # using RegEx
found2 = re.search(r'[aeiou]\b', in_str)    # using RegEx
found3 = re.search(r'[bcdfghgklmnpqrstvwxyz]\b', in_str)    # using RegEx
found4 = re.search(r'[BCDFGHJKLMNPQRSTVWXYZ]\b', in_str) # using RegEx
if found1:
print(in_str, 'FALSE')   #if string ends with capital letter vowel,return false

if found2:
print(in_str, 'FALSE') #if string ends with small letter vowel,return false

if found3:
print(in_str, 'TRUE') #if string ends with small letter consonant,return true

if found4:
print(in_str, 'TRUE') # #if string ends with small letter consonant,return true

in_str = input('Enter a string:')    # taking the string from user
ends_with_consonant(in_str)

# Part A. ends_with_consonant(s)
# Define a function ends_with_consonant(s) that takes a string and returns true
# if it ends with a consonant and false otherwise.
# (For our purposes, a consonant is any letter other than A, E, I, O, U.)
# Note: Be sure to use RegEx and it works for both upper and lower case and for nonletters!




 # Part B. ends_with_number
# Define a function ends _with_number(s) that takes a string and returns true
# if it ends with a number and false otherwise.
# (For our purposes, a number is any character that is 0,1,2,3,4,5,6,7,8, or 9.)
# Note: Be sure to use RegEx!
def ends_with_number(in_str): # function
found1 = re.search(r'[0-9]\b', in_str)
  
if found1:
print(in_str, 'TRUE') # if string ends with number then return true
  
else:
print(in_str, 'FALSE')    # if string ends without number then return false

in_str = input('Enter a string:') #taking string from the user
ends_with_number(in_str)



# Part C. binary_multiple_of_6
# define a method binary_multiple_of_4(s) that takes a string and returns true
# if the string represents a binary number that is a multiple of 6.
# Note: Be sure it returns false if the string is not a valid binary number!
# Hint: Use regular expressions to match for the pattern of a binary number that is a multiple of 6.
def binary_multiple_of_6(s):


  return
