# exercise 19
# files handeling

try:    # its good to open files inside try block
    f= open('message.txt', 'r') # 'r' for read file 'w' for write, 'a' for append at the end of file
    #print(f.read())

    print(f.read(6))  # read will print first 6 leters
    print(f.read(6))  # read is a generator Now it will print next 6 leters

finally:
    f.close()   # always close the file after.



#####
##### Better practice is to open files with 'with open'

with open('message.txt','r') as f:
    print(f.read(10))  
    print(f.read(15)) 

    # 'with' will close file automatically at the end


# write will creat new file or overwrite existing file
with open('exercise19.txt','w') as f:
   f.write('Hello World of Python.\n\n')

with open('exercise19.txt','w') as f:
    f.write('Oops accidently deleted old text.\n')


# use 'a' append to avoid overwriting a file content
    # writelines can write a list of texts into the file
with open('exercise19.txt','a') as f:
    lines=['The deleted text was this.','\nHello World of Python.']
    f.writelines (lines)