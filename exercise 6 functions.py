# exercise 6 functions
# add and multiply function

def add_numbers(n1,n2):
    return (n1+n2)

def multiply_numbers(n1,n2):
    return (n1*n2)

number_1= int(input("Enter number 1: "))
number_2= int(input("Enter number 2: "))

sum= add_numbers(number_1,number_2)
print ("The sum is:",sum)

product= multiply_numbers(number_1,number_2)
print ("The product is:",product)