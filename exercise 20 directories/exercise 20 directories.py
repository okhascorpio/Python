# exercise 20
# directories with os module


import os
os.system('cls')
# current working directory
print(os.getcwd())
os.rename('exercise 20','exercise 20 directories')
#os.chdir('C:/Users/fani/Python_exercises/exercise 20/')

with open('new document.txt', 'w') as f:
    f.writelines('Hello Python')

print(os.getcwd())
try: # try and ignore file exists error
    os.mkdir('New Folder')  # will not make new if already exists
    print ('1st: ',os.listdir())
except FileExistsError:
    print ('2nd: ',os.listdir())   

try:
    os.rename('new document.txt', 'renamed doc.txt')
except FileExistsError:
    print ('3rd: ',os.listdir())

try:
    os.rename('New Folder','Renamed Folder')
except FileExistsError:
    print ('4th: ',os.listdir())


os.rmdir('Renamed Folder')
print ('4th: ',os.listdir())
