# lambda's are small one-line functions that can take an input and return an output
# this can be used when you need only a single use of a function in your code
add10=lambda x: print(x+10)
# add10(5)

mult=lambda x,y: print(x*y)
# (mult(2,7))

point2D=[(3,4),(1,2),(7,8),(5,-6)]
point2D_sorted=sorted(point2D, key=lambda x:x[1])
print(point2D_sorted)

# map (func,seq)
# transforms each element into a function
a=[1,2,3,4,5,6,7,8,9,10]
b=map(lambda x:x+2,a)
c=[x+2 for x in a] #acheiving the same thing with list comprehension
# print(list(b))
# print(c)

# filter (func,seq)
# returns true /false and returns all true elements

filt1=filter(lambda x:  x%2==0,a)
print(list(filt1))