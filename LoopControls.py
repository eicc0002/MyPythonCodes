# For loop
# It is used when we know specifically the number of repetitions
for i in range(0, 5, 1):
    print("🍪")

# while loop
# It is used when we're uncertain about the number of repetitions
# But we know the condition for which the loop has to remain active
# Loop manipulation techniques:
# 1. To alter the execution speed/frequency of a loop
# 2. break - Terminate the loop immediately
# 3. continue - The continue statement exits the current iteration
#               and starts a new iteration immediately!

import time

monkeyCount = 0
while True:
    monkeyCount = monkeyCount + 1
    print("🐵" + " - " + str(monkeyCount))

    if monkeyCount > 99:
        print("You have reached the Singapore Zoo!")
        break

    if monkeyCount < 50:
        continue

    print("You are getting close to the Singapore Zoo!")
    time.sleep(0.1)

print("END OF LOOP")

















