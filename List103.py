gameList = ["Minecraft", "Roblox"]
gameList.insert(1, "Fortnite")
gameList.insert(0, "Bloxd.io")

#print(gameList)
"""
Question 1 + 2 - 20% + 20%
[]
[1]
[2, 1]
[3, 2, 1]
[4, 3, 2, 1]
...
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[10, 9, 8, 7, 6, 5, 4, 3, 2]
[10, 9, 8, 7, 6, 5, 4, 3]
...
[]

"""
numList1 = []
for i in range(10, 0, -1):
    numList1.append(i)
    #print(numList1)

import time

while True:
    numList2 = []
    for i in range(1, 11, 1):
        numList2.insert(0, i)
        print(numList2)
        time.sleep(0.05)


    # Delete the last item in the list repeatedly
    for i in range(len(numList2)):
        del numList2[len(numList2) - 1]
        print(numList2)
        time.sleep(0.05)



"""
numList3 = [1, 2, 3]
del numList3[len(numList3) - 1] 
print(numList3)
"""



"""
LEADERBOARD:
MidnightAutumn - 100
PottyTrooper - 100
FailureManagement - 77
TheOneWhoFail - 68
"""



