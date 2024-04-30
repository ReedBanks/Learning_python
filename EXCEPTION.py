# try to ecept specific files

try:
    number=67
    # number = int(input("Enter a number : "))
    print(number)
    # value = 10/0
except ZeroDivisionError as err:
    print("divided by 0")
    print(err)
except ValueError as err:
    print("invalid input!!")
    print(err)

x=6
# if x<10:
    # raise Exception("x must be between 10 and 20")

# assert throws assertion exception if the assertion fails/ not true
assert (x<10),"x must be between 10 and 20"

# we can define our own exception by subclassing the main exception class

class ValueError(Exception):
    pass

def value(x):
    if x > 100:
        raise ValueError("value too large")
    
try:
    value(200)
except ValueError as err:
    print(err)