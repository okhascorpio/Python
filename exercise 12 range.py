# exercise 12
# Range function

# creat range

myRange = range(1,5)
print(myRange.start)
print(myRange.stop)
print(myRange.step)
print(myRange.index(3))

print (list(myRange))

myRange2 = range(5) # same as range(0,5)
print (list(myRange2))

myRange3 = range (0,11,2) # range with step
print (list(myRange3))

for value in range(5):
    print (value,'loop using range')
    
# Programming task

myRange4 = range(3,31,3)
print (list(myRange4))
print ("Jenkins automationTest")


