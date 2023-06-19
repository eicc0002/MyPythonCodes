"""
Write a Python program to add 'ing' at the end
of a given string (length should be at least 3).
If the given string already ends with 'ing',
add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged.
"""

# Examples:
# work - working
# doing - doingly
# oh - oh

# A parameterised function (a function that accepts inputs)
def addToString(testString):
    if len(testString) > 2:
        # Process the string here
        if testString[-3::1] == "ing":
            print(testString + "ly")
        else:
            print(testString + "ing")
    else:
        print(testString)


# addToString("sneezing")
# addToString("minecraft")
# addToString("Hi")


# Question 2
# Given any String of odd length greater than 7,
# print out the middle 3 characters line by line
# testString = "SwissCottage1"
# Output: C
#         o
#         t

def mid3(testString):
    # Check if the string is odd length
    # using the modulus operator
    if len(testString) % 2 == 1 and len(testString) > 7:
        middleIndex = int((len(testString) - 1) / 2)
        print(testString[middleIndex - 1]) # mid left
        print(testString[middleIndex]) # mid
        print(testString[middleIndex + 1]) # mid right


# Question 3
# Remove then n-th index character from a nonempty string
# A parameterised function with two parameters
def remove_char(testString, n):
    first_part = testString[0:n:1]
    second_part = testString[n + 1::1]
    print(first_part + second_part)


# Question 4
# Write a Python program to change a given
# string to a new string where the first and last chars
# have been exchanged.
testString = "MINECRAFT"
#print(testString[0]) # Points to the first char of any string
#print(testString[-1]) # Points to the last char of any string
#print(testString[-2]) # Points to the second last char of any string

def swap_first_last(testString):
    print(testString[-1] + testString[1:-1:1] + testString[0])


# Question 5
# prints all odd index characters in any string using a for loop
def filter_odds(testString):
    for i in range(1, len(testString), 2):
        print(testString[i])

def filter_evens(testString):
    for i in range(0, len(testString), 2):
        print(testString[i])

filter_odds("SINGAPORE")
filter_evens("SINGAPORE")







