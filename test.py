# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#      fact=fact*i
# print("factorial number is",fact)

# qno 2

# a=int(input("enter a number"))

# if a>=0 and a<=12:
#      print("child")

# elif a>=13 and a<=19:
#      print("teeneger")
# elif a>=20 and a<=59:
#      print("adult")
# else :
#      print("senior citizin")

# qno 3
# n=int(input("enter a number"))
# x=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=x+2
#     print()

# n=int(input("enter a number"))
# x="A"
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=chr(ord(x)+1)
#     print()

# q no 4


# prime number is ya not

# n=int(input("enter a number"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
# else:
#     print("not prime")

# qno 5
# sports=["cricket","football","hockey","football","ches"]
# print("football",sports.count("football"),"time")
        

# qno 6
# l1=[8,4,5,12,45,9,3,2]
# l1.sort(reverse=True)
# # l1.sort()
# print("second heighest value",l1[1])

# qno 7
# find commom element
# type casting
list1=[10,20,30,40]
list2=[30,40,50,60]
# s1=set(list1)
# s2=set(list2)
# print(s1.intersection(s2))

# without set 
for i in list1:
    if i in list2:
        print(i)

        
        