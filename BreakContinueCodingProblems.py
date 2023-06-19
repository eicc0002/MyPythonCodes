testString = "GetWellSooooooOOOOOOooooooOOOOOOOOOOOonHJ"

# for loop with the range() function
for i in range(0, len(testString), 1):
    print(testString[i], end="🍎 ")

print("\r")

# for-each loop in python
# eachChar represents the character in the current iteration
# as we iterate through the string
for eachChar in testString:
    print(eachChar, end="🍎 ")

print("\r")


# Question 1 - Print every character in the testString except for letter "O" "o"
#               USING THE FOR-EACH LOOP APPROACH AND CONTINUE STATEMENT
for eachLetter in testString:
    if eachLetter == "O" or eachLetter == "o":
        continue # It starts a new iteration immediately
    print(eachLetter, end=" ")


print("\r")


# Question 2 - To count the occurances of letter "O" "o" in the testString
# Use for-each loop

count = 0
for eachChar in testString:
    if eachChar == "o" or eachChar == "O":
        count += 1

print(count)



# Question 3 - To print every character before the second letter "O" or "o"
# Cut off at the second letter "O" or "o"
# for each loop, break, count variable
count = 0
for eachChar in testString:
    if eachChar == "o" or eachChar == "O":
        count += 1

    if count > 2:
        break

    print(eachChar, end=" ")











