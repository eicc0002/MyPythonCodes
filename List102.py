# To add an item into the list
# Append integers from 1 - 100 in numList (10%)
# Output:
"""
[]
[1]
[1, 2]
[1, 2, 3]
...
[1, 2, 3, ..., 100]
"""
import time

numList = []
print(numList)

for i in range(1, 101, 1):
    numList.append(i)
    print(numList)
    time.sleep(1)


"""
LEADERBOARD:
PottyTrooper - 53
Nemesis Prime - 45
MidnightAutumn - 44
Failure Management - 34
"""