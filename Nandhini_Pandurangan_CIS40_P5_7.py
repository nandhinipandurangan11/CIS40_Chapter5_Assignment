# CIS40: Summer 2020: Chapter 5 Problem 7: Nandhini Pandurangan
# This program prompts the user for a string
# and prints out the number of words in the string


# countWords(string) return the number of words in the string
def countWords(string):
    sentence_list = string.split(" ")  # creating a list from the words of the sentence

    if len(sentence_list) == 1 and sentence_list[0] == "":  # if the sentence is an empty string
        return 0
    else:
        return len(sentence_list)         # returning the length of the list = number of words in sentence


# main() handles input, calls countWords(), and prints the output
def main():
    string = input("Please enter a sentence: ")
    print(string, "has", countWords(string), "words")


# calling main
main()

''' 
Output: 

Please enter a sentence: Mary had a little lamb
Mary had a little lamb has 5 words
-------------------------------------------------
Please enter a sentence: 
 has 0 words
------------------------------------------------
Please enter a sentence: Ice-cream comes in lots of flavors. Oreo is my favorite.
Ice-cream comes in lots of flavors. Oreo is my favorite. has 10 words

'''
