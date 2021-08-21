# exercise 14
# class inheritance

class Food:
    def price(self,price=0):
        self.price=price
        
    def weight(self,weight=0):
        self.weight=weight
    
    def RawOrCooked(self,condition):
        self.condition = condition
    
class Vegan(Food):
    
    def __init__(self,name):
        self.name=name
    def vegitable(self,vegitable):
        self.vegitable=vegitable
        
    def color(self,color):
        self.color=color
   
    def MadeOf(self,material):
        self.material=material
        
class NonVeg(Food):
    
    def __init__(self,name):
        self.name=name
    
    def meat(self,meat):
        self.meat=meat
        
        
pasta =   Vegan('pasta')
pasta.vegitable='Bell pepper'
pasta.color='Green'
pasta.weight=2
pasta.price=3.5
pasta.RawOrCooked='Cooked'
pasta.MadeOf='wheat'

pizza = NonVeg('Pizza')
pizza.meat('Tona fish')
pizza.price(5)
pizza.weight(250)
pizza.RawOrCooked('Raw')

print (pasta.name)
print(pasta.color,pasta.vegitable,pasta.name)
print(pasta.weight,'kg')
print(pasta.RawOrCooked)
print(pasta.price,'euro')

print(pizza.name)
print(pizza.meat,pizza.name)
print(pizza.weight,'grams')
print(pizza.price,'euro')