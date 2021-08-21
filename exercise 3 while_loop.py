#exercise_3 while loop
#10 to 1 multiplication table  

user_input=int(input("Enter a number:"))
loop_value=10
while loop_value >0:
    print(user_input , "X" , loop_value , "=" , (user_input*loop_value))
    loop_value-=1
