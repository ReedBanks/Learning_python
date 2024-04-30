import random

def roll(num):
    return random.randint(1, num)

# itertools
#is a collection of tools for handling iterators
from itertools import product

a=[1,2,3,4]
b=[3,4]

# print(list(product(a,b,repeat=2))) #returns an object 

from itertools import permutations
# shows the number of ways the list can be permuted/arrangged

# print(list(permutations(a)))


from itertools import combinations
import operator

# shows the number of ways the list can be combined
print(list(combinations(a,2)))

from itertools import accumulate
# makes an iterator that returns an accumalated sum
accm=accumulate(a,func=operator.mul)
print(list(accm))

from itertools import groupby
# makes an iterator that returns keys and groups
def smaller_than_3(x):
    return x<3

group_obj=groupby(a,key=smaller_than_3)

for key,value in group_obj:
    print(f"GroupBy : {key , list(value)}")



