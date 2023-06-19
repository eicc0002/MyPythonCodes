""" Question - 20%
numList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numList2 = []
Find all odd numbers in the numList1 and add them to numList2
print numList2
Output: [1, 3, 5, 7, 9]
"""

def Odd_Number_Filter(someWeirdList):
    numList2 = []
    for eachNum in someWeirdList:
        if eachNum % 2 == 1:
            numList2.append(eachNum)
    print(numList2)


# Odd_Number_Filter([*range(1, 101, 1)])


# Given any list, find the largest number in the list
def our_max_function(someList):
    curr_max = someList[0]
    for eachNum in someList:
        if eachNum > curr_max:
            curr_max = eachNum
    return curr_max

print(our_max_function([8, 1000, -100, 1000.1]))



# Given any list, find the smallest number in the list - 20%
def our_min_function(someList):
    curr_min = someList[0]
    for eachNum in someList:
        if eachNum < curr_min:
            curr_min = eachNum
    return curr_min


print(our_min_function([8, 1000, -100, 1000.1]))


# Create a function that returns the sum of all numbers in a someList - 20%
# anyList = [1, 2, 3]
# output: 6
def Sum(someList):
    pocket = 0
    for eachNum in someList:
        pocket = pocket + eachNum # Change pocket by +eachNUm
    return pocket


# Some average - 10%
def SumAvg(someList):
    pocket = 0
    for eachNum in someList:
        pocket = pocket + eachNum # Change pocket by +eachNUm
    return pocket


print(Sum([]))
print(SumAvg([]))

"""
LEADERBOARD:
Trevan - 160
Menaja - 148
Zac - 110
HJ - 101
"""