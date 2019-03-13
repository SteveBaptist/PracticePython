'''
Created on Mar 1, 2019

@author: Steve Baptist
'''

if __name__ == '__main__':
    pass

"""
Exercise 2
Ask the user for a number. Depending on whether the number is even or 
odd, print out an appropriate message to the user. Hint: how does an 
even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one 
number to divide by (check). If check divides evenly into num, tell that 
to the user. If not, print a different appropriate message.
The % sign is exactly the modulus operator.
"""

def remain():
    simple = str.lower(input("Do you want to check odd or even, or \
    \nsomething more complex? Type simple or complex"))
    num = int(input("What is your dividend?"))    
    
    if simple in "simple":
        check = 2
        if num % check == 0:
            print(f"{num} is even.")
            if num % 4 == 0:
                print(f"{num} is a multiple of 4")
        else:
            print(f"{num} is odd.")
        
                
    else:
        check = int(input("What number do you want to devide by?"))
    
    if num % check == 0:
        print(f"{check} goes into {num} evenly {int(num / check)} times.")
    else:
        print(f"{check} does not go into {num} evenly.")
keep = True
while keep:
    remain()
    goin = str.lower(input("Do you want to test new numbers? Yes or No?"))
    if goin in "no":
        keep = False
