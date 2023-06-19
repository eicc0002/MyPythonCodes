# Python List []
# Empty List - []
foodList = ["MilkTea", "ChiliCrab", "Sushi", "Steamboat"]
print(foodList)


# Print each item in the list using the for i in range approach (10%)
for i in range(0, len(foodList), 1):
    print(foodList[i], end=" ** ")

print("\r")

# Print each item in the list using the for each loop approach (10%)
for eachItem in foodList:
    print(eachItem, end=" ** ")

print("\r")

# Reverse print the list (20%) - Slicing technique - just one line of code
# Output:
# ['Steamboat', 'Sushi', 'ChiliCrab', 'MilkTea']
# Steamboat Sushi ChiliCrab MilkTea
for i in range(len(foodList) - 1, -1, -1):
    print(foodList[i], end=" ")

print("\r")

print(foodList[::-1])


"""
LEADERBOARD:
Nemesis Prime - 45
PottyTrooper - 43
MidnightAutumn - 42
Failure Management - 26
"""