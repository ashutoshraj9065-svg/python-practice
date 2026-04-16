t = 10
print(type(t))

t = (10)
print(type(t))

t = (10,)
print(type(t))

t = 10,20,30
print(type(t))

x,y,z = (10,20,30),20,30
print(x,y,z)

t = (1,2,3,4,5,'python','java')
print(t)
print(type(t))
print(id(t))
print(len(t))
# print(max(t)) # '>' not supported between instances of 'str' and 'int' 
# print(min(t)) # '<' not supported between instances of 'str' and 'int'
# print(sum(t)) # unsupported operand type(s) for +: 'int' and 'str'

t1 = (1,2,3,4,5,6)
# print(max(t1))
# print(min(t1))
print(sum(t1))

t2 = ('python','java','php')
print(max(t2))
print(min(t2))
# print(sum(t2)) # unsupported operand type(s) for +: 'int' and 'str'
 
# methods of tuple:-------
t = (1,2,3,'python','java')
print(t.count(10)) # frequency of any element
print(t.index('java')) # findout index position of any element
