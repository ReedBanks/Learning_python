# no duplicates,mutable,unordered

myset=set()
print(type(myset))
myset.add(1)
myset.add(23)
myset.pop()


# for i in myset:
#     print(i)

odds={1,3,5,7,9}
evens={2,4,6,8}
primes={2,3,5,7}
print(type(odds))
print(odds.union(evens))
print(odds.intersection(primes))
print(primes.intersection_update(evens))
print(odds.difference(evens))#odds-evens``
odds.issuperset(primes)
odds.isdisjoint(evens)