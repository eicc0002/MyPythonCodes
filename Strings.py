# String Duplication
print("+" + "-" * 50 + "+")
print(("|" + " " * 50 + "|\n") * 5, end="")
print("+" + "-" * 50 + "+")

def ProcessAString():
    # String indexing
    str1 = input("Enter a word/sentence: ")
    for i in range(0, len(str1), 1):
        print(str1[i], end="---")

def ReverseAString():
    # Reverses a string
    str1 = input("Enter a word/sentence: ")
    for i in range(len(str1) - 1,-1,-1):
        print(str1[i], end="")

ReverseAString()

