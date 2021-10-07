# Exercise 23 
# Arrays
from array import array

# i for integer, d for float, 
a= array('i',[1,2,3])
print ('Type ', type(a))
print('Array ',a)
print ('Length ',len(a))

a.append(4)
print('Append ',a)

a.extend([5,6,7])
print('Extend ',a)

# pop returns the value removed
b=a.pop()
print ('poped ',b)
print('Pop ',a)

# Give index of value to remove + or - index works
a.pop(2)
print('Pop 2 ',a) 

# Give value to be removed to remove function
a.remove(5)
print('remove 5',a)

# Concat arrays of same data type  c = a + b
b = array('i',[7,8,9])
c=a+b
print('Concat ',c)
# Slice array, end index not included.

print ('slice ', c[2:4])


