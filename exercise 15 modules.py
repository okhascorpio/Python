# exercise 15 
# importing modules
from os import system
system("cls")


import Testcalculator
print('2 + 4 =',Testcalculator.add(2,4))
print('2 - 4 =',Testcalculator.subtract(2,4))
print('2 x 4 =',Testcalculator.multiply(2,4))
print('2 / 4 =',Testcalculator.devide(2,4))

# import math to import everything in math module
# or use 'from math import' to import one part of the module
from math import sqrt 
print('square root of 25 is',sqrt(25))
