# s = {1,3,2,5,3,6,7}
# print(s)

# s = {'python','java','php'}
# print(s)

# s = {1,2,3,'python','java','php'}
# s.add(100)
# s.add("c")
# print(s)


# s = {1,2,3,'python','java','php'}
# # # s.update(100,200,300) # TypeError: 'int' object is not iterable
# s.update('python')
# # s.update('python','java')
# print(s)

# s = {1,2,3,'python','java','php'}
# # s.remove() # set.remove() takes exactly one argument (0 given)  
# # s.remove('python')
# # s.remove(100) # KeyError: 100
# s.discard(30)
# print(s)

# s = {1,2,3,'python','java','php'}
# s1 = s.copy() 
# print(s,s1)
# print(id(s),id(s1))

# s = {1,2,3,'python','java','php'}
# s.clear()
# print(s)

# s={1,2,3,4,5}
# s1={4,5}
# s.intersection(s1)
# print(s)
# print(s1)
# print(s.difference(s1))
# print(s)

# s.difference_update(s1)
# print(s)
# print(s1)

# s.symmetric_difference_update(s1)
# print(s)
# print(s1)

# print(s.isdisjoint(s1))

# print(s.issuperset(s1)
# print(s1.issubset(s))

# homework set and forezen set

s1={10,20,30,"java","python","c++"}
f=frozenset(s1)
# print(type(f))
s2={10,20,30,"java"}
f1=frozenset(s2)
print(f.intersection(f1))
print(f.difference(f1))
print(f.union(f1))
print(f.symmetric_difference(f1))
print(f.isdisjoint(f1))
print(f.issuperset(f1))
print(f1.issuperset(f))
print(f1.issubset(f))
print(f.issubset(f1))



