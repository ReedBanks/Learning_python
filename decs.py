# decorators => is a function that takes another function as an argument and extends its functionality
#              1. function decorators =>
#              2.class decorators =>

import functools

def repeat(num_times):
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decoration
    
    

@repeat(num_times=3)
def greeting(name):
    print(f"Hello {name}")
    
# greeting("Reed")

# class decorators
# used often when we want to maintain and handle a state
class CountCalls:
    
    def __init__(self,func):
        self.func = func
        self.num_count=0 #state variable to count class calls
        
    def __call__(self,*args, **kwargs):
        # allows to execute an obj of the class as a function
        self.num_count += 1
        print(f"Current calls : {self.num_count}")
        

    
@CountCalls
def hello():
    print("Hello")
    
user1=hello()
user2=hello()
user3=hello()

# uses
# time comparison
# debugging
# caching
