# exercise 9
# Dictionary is a collection which is ordered* and changeable. No duplicate members.


Dict_1 = {'name':'Fred','Age':24}
print(Dict_1['name']+' '+str(Dict_1['Age']))
print(Dict_1.get('name'))

Dict_1['Age']=27
print (Dict_1.get('Age'))

#print(Dict_1.pop('name'))
#print(Dict_1)
#print(Dict_1.popitem())
#print(Dict_1)
#Del_1.clear
#del Dict_1

print(Dict_1.items())

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels_muteable = dict.fromkeys( keys , value )
#vowels = { key : list(value) for key in keys }
# you can also use { keys : value[:] for key in keys }
vowels = { key : value[:] for key in keys}
print(vowels)

# updating the value
value.append(2)
value.append(3)
print("muteable dictioany" + str(vowels_muteable))
print("fix dictionary"+ str(vowels))
