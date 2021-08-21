# exercise 5 break and continue
# print all except few

languages = [ "Python" , "Java" , "Swift" , "C" , "C++"] 
for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print (language)