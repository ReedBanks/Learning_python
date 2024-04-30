''' 
Since swicth statements don't exist in python it can be emulated
'''
def gender_check(gender):
    match gender:
        case "M":
            return "male".upper()
        case "G":
            return "female".upper()
        
gender_check('m')


# modifying a global variable
def foo():
    global number
    number=3
    x=number
    print("x is : ", x)

number=0
foo()    
print("number is : ", number)

# callings
def calls(x):
    x=5
    print("value is : ", x)

var=10
calls(var)


# shallow & deep copying
# shallow copying is only for one level deep
# deep copying makes a full independent copy.good for nestted copying

import copy

org=[1,2,3,4,5,6,7,8,9,10]
sh_cpy=org.copy() #shallow copy

deep_org=[[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15]]
dp_cpy=copy.deepcopy(deep_org)
# 

sh_cpy[0]=0 
dp_cpy[1][0]=1

print(sh_cpy)
print(org)

print("\n",dp_cpy)
print("\n",deep_org)
