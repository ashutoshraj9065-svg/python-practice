# append():- add single element at last position in given list
l = [10,20,30,40,'python','java']
# l.append(100)
l.append((1,2,3,4,5,6,7,8))

print(l)

# extend():- add multiple elements at last position in given list
l = [10,20,30,40,'python','java']
# l.extend(100) # 'int' object is not iterable
# l.extend((1,2,3,4,5,6,7,8))
l.extend('python')

print(l)


# insert():- add element in targeted posion of given list.
l = [10,20,30,40,'python','java']
# l.insert(0,"PHP")
# l.insert(4,"PHP")
l.insert(4,[1,2,3,4,5,6,7,])
print(l)


# copy():- Create new objects with same elements.
l1 = [1,2,3,4,5,6,"python"]
l2 = l1.copy()
print(l1,l2,sep=' , ')
print(id(l1),id(l2),sep=',')

# pop():- remove element through targeted index. By-default it remove -1 index element. (i.e last element)
l = [1,2,3,4,5,6,"python"]
# l.pop() # default last position[-1] is targeted
l.pop()
print(l)

# remove():- remove element from given list.
l = [1,2,3,4,5,6,"python"]
# l.remove() # list.remove() takes exactly one argument (0 given)
# l.remove(100) #  list.remove(x): x not in list
l.remove(6)

print(l)

# clear(): remove all elements from given list.
l = [1,2,3,4,5,6,"python"]
l.clear()
print(l)
# del :- remove object from system memory
del l
print(l) # name 'l' is not defined

# index():- findout index position of any element.
l = [1,2,3,4,5,6,"python"]
pos = l.index(5) # l.index(element,start,stop)
print(pos)

# count():- frequency of any element.
l = [1,2,3,4,5,6,5,5,5,"python"]
# pos = l.count(5)
pos = l.count(100)
print(pos)

# sort(): arrenge in assending order.
l = [2,5,3,41,5,6,7]
l.sort()
print(l)
l.sort(reverse=True) # desending order
print(l)


# reverse(): arrenge in reverse order.
l = [2,5,3,41,5,6,7]
l.reverse()
print(l)