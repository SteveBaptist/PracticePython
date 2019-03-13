'''
Created on Mar 12, 2019

@author: Steve Baptist
'''

if __name__ == '__main__':
    pass

"""
Exercise 4
Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. (If you don't know what a divisor is, 
it is a number that divides evenly into another number. For example, 13 is 
a divisor of 26 because 26 / 13 has no remainder.)
"""

def isDiv(num):
    divisors = []
    for chk in range(1, num + 1):
        if num % chk == 0:
            divisors.append(chk)
    print(divisors)
        
test = 192



isDiv(test)

