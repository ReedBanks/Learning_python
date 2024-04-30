class Student:

    # initialize func(self , attributes)
    def __init__(self, name, major, gpa, is_in_1st_class):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.first_class = is_in_1st_class

# randoms
import random

a=random.randrange(0,20)
random.normalvariate(1,20)
random.shuffle(list("abcdef"))
random.seed(2)
random.randint(1,10)

# since the random can be predicted we use the secret module 

import secrets
# has only 3 functions for pwds,security tokens and auth keys

a=secrets.randbelow(10)
b=secrets.randbits(8)#returns an integer with a certain number of bits

secrets.choice([a,b])

import numpy as np

rand=np.random.rand(3)
print(rand)