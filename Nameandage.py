'''
Created on Mar 1, 2019

@author: Steve Baptist
'''
from time import time, gmtime
if __name__ == '__main__':
    pass

"""
Exercise 1
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. (Hint: order of 
operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""

def centenial():
    curdte = gmtime(time())
    curdte = curdte[0]
    name = input("What is your name?")
    age = int(input("How old are you?"))
    happy = str.lower(input("Have you had your birthday yet? Type yes or no"))
    byear = curdte - age
    if happy in "no":
        byear = byear - 1
    cyear = byear + 100
    print(f"Hi {name}, you were born in {byear}.\
          \nyour centenial birthday will be in {cyear}.")

centenial()