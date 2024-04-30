# collection module implements special container data types and provides
# alternatives for things like dictionaries and tuples
# counter,namedtuple,ordereddict,defaultdict,deque

from collections import Counter
# couner is a container that stores elements as dictionary keys and
# their count as dictionary values 

a="abbccc"
myCounter=Counter(a)
print(myCounter.most_common())

from collections import namedtuple
# similar to a struct 
# 

Point=namedtuple("Point",'x,y') #this creates a point class with field x and y
pt1=Point(1,-2)

print(pt1)

from collections import OrderedDict
# this is just like a normal dictionary but it remembers the order in which values were inserted in the dictionary

order=OrderedDict()
order['a']=1 
order['b']=2
order['c']=3

print(order)

from collections import defaultdict

#allows a default value if a key has no value
d=defaultdict(float)
d['a']=-1
d['b']=-2
d['c']=-3
print(d[''])


from collections import deque
# doubles ended queues
# can be used to add and remove from both the top and bottom of the queue
queue = deque()
queue.append(23)
queue.append(44)
queue.append(423)
queue.append(42)

queue.appendleft(1)
queue.pop()
queue.popleft()
print (queue)
