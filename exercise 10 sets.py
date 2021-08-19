# exercise 10
# Set is a collection which is unordered and unindexed. No duplicate members.


set1= {'text',False,1,2,3}
set2= {4,5,6}
set3= {"monkey"}
print(type(set1))


set1.add(4)
print('add to a set')
print(set1)

print('\nupdate a set')
set1.update(set3,{8,9})
print(set1)


print('\nunion of sets')
union= set1 | set2
print(union)



print('\nintersection')
intersection= set1&set2
print(intersection)

print('\nis subset')
print(set2.issubset(union))
#print(set1.difference_update(set2))

print('\nremove from a set')
set1.remove(4) #remove throws erroe if not found
print(set1)


print('\ndiscard from a set')
set1.discard("cat") #discard throws no error but returns 'none' 
print(set1)



print('\nfind in set')
print (10 in set1)

print('\nfor loop in set')
for number in set1:
    print(number)

print('\nclear set')
set1.clear()
print(set1)



