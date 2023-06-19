import time

rowNum = 5

def Pyramid123(rowNum):
    for i in range(1, rowNum + 1, 1):
        print("🍦" * i)
        time.sleep(0.5)

    # Reverse the triangle
    for i in range(rowNum - 1, 0, -1):
        print("🍦" * i)
        time.sleep(0.5)


def Pyramid246(rowNum):
    for i in range(2, (rowNum * 2) + 1, 2):
        print("🇸🇬" * i)
        time.sleep(0.5)



"""
e.g. rowNum = 5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# 1. Identify the pattern
# 2. Spot the changing factor, replace it with a variable
# 3. Loop it
def NumberPyramid1(rowNum):
    for i in range(1, rowNum + 1, 1):
        print((str(i) + " ") * i)



"""
Question 4: 
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

# 1. Identify the pattern
# 2. Spot the changing factor, replace it with a variable
# 3. Loop it
"""
def NumberPyramid2(rowNum):
    for j in range(2, rowNum + 2, 1):
        for i in range(1, j, 1):
            print(i, end=" ")

        print("\r")














