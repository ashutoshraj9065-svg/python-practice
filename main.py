# file handling 

# f=open("student.csv")
# # data=f.read()
# # print(data)
# # print(f.readline())
# # print(f.readlines())
# print(type(f.readlines()))

#with open function use in by default close function
# with open("student.csv")as f:
#     print(f.read())

# with open("student.csv","w")as data:
#     print(data.write("rahul\n32"))
# with open("student.csv","r")as data:
#     print(data.read())


# name="ashu"
# age=23
# with open("india.csv","w")as ashu:
#     print(ashu.write(f"{name} {age}"))

# with open("india.csv")as ashu:
#     print(ashu.read())


# append use 
name="banty"
age=28
with open("india.csv","a")as f:
    print(f.write(f"{name} {age}"))

with open("india.csv")as f:
    print(f.read())
print("hello")