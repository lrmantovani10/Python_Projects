##Building program that tells you if you have prime
#numbers or  not
##Use the Fermat method correctly
import random
number = int(input("Insert a number ahead:"))

def checkone():
    print("Please insert a number greater than one")
    
   
while number<=1:
    checkone()
    number = int(input("Insert a number ahead:"))
def checkprime(self):
    var1 = 2
    if (var1**(number-1))%(number) ==1 or number==2:
        print("Number is prime")
    
    else:
        print("number is not prime")

    
while number >1:
    checkprime(number)
    print("To check for the primality of another number,")
    number = int(input("Insert a number ahead:"))
