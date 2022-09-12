# exercise 11
# A tuple is a collection which is ordered and unchangeable.

myTupil=(1,2,'One','Two')
print(myTupil)

#Access
print(myTupil[2])
print(myTupil[-1])

if 'One' in myTupil:
    print('Yes')
    
# Convert tuple to list in order to change any item in it, then convert back to tuple
y=list(myTupil)
y[0]=2
myTupil=tuple(y)
print(myTupil)

# unpacking

x=('apple','banana','cherry')
(green)=x
print(green,yellow,red)
