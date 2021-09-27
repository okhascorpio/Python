def add_info(func):
    
        print('Function',func.__name__,'is running')
        return func
    
@add_info
def disp():
    print('Greetings')

disp()




def smart_devide(func):
    def inner(a,b):
        if b==0:
            print('Can not devide by zero')
            return
        return func(a,b)
    return inner



# Chain decorators
@smart_devide
@add_info
def devide(a,b):
    print(a/b)

devide(10,2)
devide(2,0)