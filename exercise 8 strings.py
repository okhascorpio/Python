#exercise 8
#strings and its functions / methods


text1='hello world'
print ("single qouts: "+text1)

text2="Hello World"
print ("Double qouts"+text2)

text3='''Hello
World
of
Nerds'''
print("String with tripple qouts, multiple lines "+text3)

print("Concatination: "+text1+" "+text2)

print("Index of w in string 1: " + str(text1.index('w')))
print(text1.isspace())

txt = "     banana     "
x = txt.lstrip()
x = x.rstrip()
print("of all fruits", x, "is my favorite")
