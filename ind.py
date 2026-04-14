# s="ashutosh"
# print(s.index("s"))
# print(s.index("s",s.index("s")+1))
# print(s.index("s",2,7))
# print(s.index("s",))

# s="programmging"
# print(s.index("g",2,-7,5))
# print(s.index("g"))
# print(s.index("g",4,9))
# print(s.index("i",3))
# # print(s.index("r",2,8))
# list = [1, 2, 3, 4, 50, 40, 30, 50, 9, 10]
# element = 50
# print(list.index(element,5))



# lst= list(map(int,input("enter a list number").split()))
# user=int(input("enter a number"))
# if(user in lst):
#     print(lst.index(user))
# else:
#     print("not found")


# lst2=[10,20,30,40,60,50]
# user=int(input("enter a number"))
# if(user in lst2):
#     print(lst2.index(user))
# else:
#     print("not valid")


user=input("enter a slice")
ashu=user[-3:-7:-1]
print(ashu)