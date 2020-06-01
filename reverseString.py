# Author: Nguyen L.
# Date:   May 14th, 2020 
# Prompt: Write a program to reverse a text. Example: "Hello" would become "olleH"

# Write code here
def reverseString(str):

    newStr = ""

    #logic
    for i in range(len(str), 0, -1):
        newStr += str[i - 1]

    return newStr

my_input = input("Type in a string here: ")
print(reverseString(my_input))
