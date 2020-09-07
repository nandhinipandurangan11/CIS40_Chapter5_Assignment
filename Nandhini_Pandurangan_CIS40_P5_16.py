# CIS40: Summer 2020: Chapter 5 Problem 16: Nandhini Pandurangan
# This program uses recursion to evaluate whether a string is a palindrome


# isPalindrome() uses recursion to check whether the given string is a palindrome
def isPalindrome(string, char1, char2, index1, index2):
    palindrome = True # sentinel value

    while palindrome and index1 <= index2: # looping while palindrome is true and until the two indexes meet
        index1 += 1
        index2 -= 1

        if char1 == char2: # calling isPalindrome() again if the characters match
            isPalindrome(string, string[index1], string[index2], index1, index2)
        else:
            palindrome = False

    return palindrome


# main() calls isPalindrome() and prints output
def main():
    string = input("Please enter a string: ").split() # storing the string as a list
    string = string[0]  # this is to make sure only the first word of the sentence is stored

    # calling isPalindrome() to determine whether the word is a palindrome
    palindrome = isPalindrome(string, string[0], string[len(string) - 1], 0, len(string) - 1)

    # outputting the results
    if palindrome:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")

# calling main()
main()

'''
Output: 

Please enter a string: deed
deed is a palindrome 
-------------------------------
Please enter a string: facebook
facebook is not a palindrome
--------------------------------
Please enter a string: rotator
rotator is a palindrome
-------------------------------
Please enter a string: She sells seashells by the seashore
She is not a palindrome
'''
