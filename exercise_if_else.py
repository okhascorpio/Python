#exercise_2 if else
#check if number is positive, negative or zero 

user_input=int(input("Enter a number:"))
if user_input > 0:
    print ("the number" , user_input , "is Positive")
elif user_input == 0:
    print ("the number" , user_input , "is Zero")
else:
    print ("the number" , user_input , "is Negative")
