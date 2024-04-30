# generators => functions that return objs that can be iterated over
# items are generated lazily(once per iteration)

def my_generator():
    yield 1
    yield 2
    yield 3
    
g=my_generator()

# for i in g:
    # print (i)

# getting values one at a time
# val=next(g)
# print(val)

# val=next(g)
# print(val)

# val=next(g)
# print(val)

# print(sum(g))

def count(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = count(4)        
value=next(cd)
# print(value)

value=next(cd)
# print(value)

def firstN(n):
    num=0
    while num<n:
        yield num
        num += 1
        
arr=firstN(10)
print(sum(arr))
        


# advantages
# memory efficiency

def fibo(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b 
        
fib=fibo(10)
for i in fib:
    print(i,end=" ")
    

# generator expressions
mygen={i for i in range(20) if i % 2==0}
for i in mygen:
    print(i,end=" ")