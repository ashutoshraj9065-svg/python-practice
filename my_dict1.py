d = {
    'name':'python',
    'language':'backend',
    'city':''
    }

d.clear()
print(d)

d1 = d.copy() 
print(d,d1)
print(id(d),id(d1))

fromkeys
s = 'python'
# d1 = dict().fromkeys(s)
d1 = dict().fromkeys(s,100)

print(d1)

s = [1,2,3,4,5,6,7]
d1 = dict().fromkeys(s)
# d1 = dict().fromkeys(s,100)
print(d1)
d1[1] = "python"
d1[2] = "python"
d1[3] = "python"
print(d1)

d.get('key','default')
x = d.get('name') 
x = d.get('name1')
x = d.get('name','Guest')

print("Welcome ",x)

print(d.keys())
print(d.values())
print(d.items())

# d.pop('key')
d.pop('name')
print(d)

d.popitem()
print(d)

print(d.setdefault('city','Bhopal'))
print(d)

d1 = {'x':10,'y':20,'z':30}
d.update(d1)
print(d)
d["name"]="c"
print(d)
