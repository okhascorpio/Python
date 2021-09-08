# exercise 18
# exception handeling try except

#Any type of exception

A= 10
B= 0
C= [2,4,6]
try:
    C=A/B   #devide by zero
    D=C[4]   #index error
   
    

except ZeroDivisionError:
    
    print('Cannot devide by zero.')

except IndexError:
    print ('Index is incorrect.')

except:
   print('Some exception has occured.')

finally:
    print('Program ends.')