# exercise 17
# generators creat results on the go. They do not hold values in memory
# are more efficient 
import os, psutil

def squares_of(list_of_numbers):
    for num in list_of_numbers:
        yield num*num 

print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
print(psutil.Process(os.getpid()).memory_info().vms/ 1024 ** 2)



# Test
list= [1,2,3,4,5,6]   
squares= squares_of(list)
# print (squares.__next__())
# print (squares.__next__())
print (next(squares), ' First Print')
# print (squares.__next__())
# print (squares.__next__())
# print (squares.__next__())
#print (squares.__next__())  # will give Error because gen ran out of iteration

# use for loop to go through generator values

for n in squares:
    print(n, ' 2nd Print')


# Can only go through once. 
# printed first value above, the rest in for loop




## Generator from Generator expression

cubes = (x*x*x for x in list)   ## (  ) instead of '[ ] in list comprehension' make it a generator

for c in cubes: print(c, ' Cubes')

