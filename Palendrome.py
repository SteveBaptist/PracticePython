'''
Created on Mar 12, 2019

@author: Steve Baptist
'''



if __name__ == '__main__':
    pass

"""
Exercise 6
Ask the user for a string and print out whether this string is a palindrome 
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

def isPal(wrd):
    same = True
    for ltr in range(len(wrd)):
        #print(wrd[ltr], wrd[-ltr - 1], same)
        if wrd[ltr] != wrd[-ltr -1]:
            same = False
            
    if same:
        print(wrd + " is a palendrome.")
    else:
        print(wrd + " is not a palendrome")

word = "hatah"

isPal(word)