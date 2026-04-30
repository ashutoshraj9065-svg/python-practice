
# # import string
# # import keyword

# # print(len(keyword.kwlist))
# # print(keyword.kwlist)
# # print(len(keyword.softkwlist))

# # print(string.punctuation)
# # print(len(string.punctuation))

# # x=10
# # y=5
# # print(x/y)
# # print(x//y)
# # print(x%y)

# # print(x:="python")

# # x=20
# # y=10
# # z=30
# # print(x==y)
# # print(x>y)

# # print(x>y or y>z)
# # x=[10,20]
# # y=[10,20]
# # print(x is y)




# s="i am a good boy"
# print("am" in s)

# n=int(input("enter a number"))
# i=1
# while i<n:
#     print(i)
#     i=i+1

# l=[2,4,6,8,10]
# add=0
# for num in l:
#     add=add+num
# print("sum is ",add)
#qno 1
# n=int(input("enter a number"))
# if n%2==0:
#     print("even number",n)
# else:
#     print("odd number",n)
# # qno 2
n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))

if n1>=n2 and n1>=n3:
    print("n1 number is a greater then n2 and n3",n1)
elif n2>=n1 and n2>=n3:
    print(f"n2 number is {n2} greater then n1 and n3")

else:
    print("n3 is a greater then n1 and n2",n3)

# qno 3
user=int(input("enter a value"))
if user==0:
    print("number is a zero")
elif user>0:
    print("number is a positive number")
else:
    print("number is a negative number")


