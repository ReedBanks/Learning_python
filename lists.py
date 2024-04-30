friend = ["bob", "squid", "mao", 2]
newfriend = ["maguire", "tim"]
friend.extend(newfriend)  # add lists
friend.append("bingo")
friend.insert(1, "inso")
friend.remove("bob")
friend.index("squid")
friend.count("mao")
# friend.sort()
friend.reverse()
# friend.clear()
friend.pop()  # removes last element
friend2 = friend.copy()
# new_list=sorted(friend)
#print(friend)
#print(friend2)
#print(friend[1:3])
#intermediate
mylist=[0]*5
# print(mylist)
list2=mylist+mylist
newList=mylist.copy()
newList.append(1)
# print(newList)

# list comprehension
square=[i*i for i in range(20)]
# print(square)


# tuples
countries = list(("UK", "GH", "NIG"))
countries.insert(0, "RUS")
countries.sort()
countries.reverse()
del countries[0]

numbers=[0,1,2,3,4,5,6,7,8,9]
numbers.sort()
numbers.reverse()
numbers.append(20)
numbers.remove(5)

coordinates=(1,2,3)
x,y,z=coordinates #unpacking coordinates

newTuple=tuple(["Max",28,"male"])
le=len(newTuple)
name=newTuple[0]
print(le)
