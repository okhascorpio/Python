# exercise 13
# class

class Person:
    
    def __init__(self,name='Joe',age=20,height=1.6):# default values set if non entered
        self.name=name
        self.age=age
        self.height=height
        
    def isolder(self,person):
        return( self.age>person.age)
            
    def istaller(self,person):
        return (self.height>person.height)
                
person1 = Person()
person2 = Person('James', 12, 1.8)
print(person1.name,person1.age,person1.height)
print(person2.name,person2.age,person2.height)
print('Is person 1 older? ',person1.isolder(person2))
print('Is person 2 taller? ',person1.istaller(person2))