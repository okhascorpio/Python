# exercise 7
# List is a collection which is ordered and changeable. Allows duplicate members.


list_1 = ["a","b","e","c","d","e"]
print("List_1 is:",list_1)

list_1.insert(1,"e")
print("Inserted \"e\" at index 1 of List_1:",list_1)

print ("count of e in list_1 is: ",list_1.count("e"))

list_1.remove("d")
print("Removed first \"d\" from List_1:",list_1)

list_2 = [1,2,3,4,5]
print("list_2 is:", list_2)

list_3=[6,7,8]
print("list_3 is:", list_3)

list_2.append(4)
print("Appended 4 at the end of list_2:",list_2)

list_4=list_1.copy()
print("list_4 is copy of list 1:",list_4)

list_2.extend(list_3)
print("Extended list2 is: ",list_2)
