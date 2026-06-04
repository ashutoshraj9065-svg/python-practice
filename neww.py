# print("hello")
# def sq_fun(n):
    
#         sa=n**2
#         return sa
# n=int(input("enter a number"))
# print(sq_fun(n))
# # print(sq_fun())

# def even_as(n):
#         if n%2==0:
#             return "even number"
#         else:
#              return "odd number"
# n=int(input("enter a value"))
# rs=even_as(n)
# print(rs)

# def ashu(n):
#       if n>1:
#             for i in range(2,n):
#                   if n%i==0:
#                         return "not prime"
#             else:
#                 return "prime number"
#       else:
#             return "not prime"
# n=int(input("enter a number"))
# a=ashu(n)
# print(a)

# n= int(input("enter a number"))
# x=0
# y=1
# print("fabonicc series")
# for i in range(1,n+1):
#     print(x,end=" ")
#     z=x+y
#     x=y
#     y=z


# n=int(input("enter a number"))

# temp=n
# sum=0
# while temp>0:
#     d=temp%10
#     sum=sum+d**3
#     temp=temp//10
    
# if sum==n:
#     print("armsstrong")
# else:
#     print("not armsstrong")

# def large():
#     largestt=[10,30,2,40,50,20]
#     largestt.sort(reverse=True)
#     return largestt[0]
# a=large()
# print("largest number",a)
# print("largest number")
# print("same number")

# # qno 1 
# n=int(input("enter a number"))
# original=n
# reverse=0

# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# if original==reverse:
#     print("planidrom ")
# else:
#     print("not planidrom")

# l1=[1,2,3,4,5,6,7]
# count=0
# for i in l1:
#     if i%2==0:
#         count=count+1
# print(count)       

# def fact(n):
#     fact1=1
#     for i in range(1,n+1):
#         fact1=fact1*i
#     return fact1
# n=int(input("enter a number "))
# a=fact(n)
# print(a)

# n=input("enter a string")
# rev=""
# for i in n:
#     rev=i+rev
# print(rev)

# n=int(input("enter a number"))
# for i in range (1,n+1):
#     if i==5:
#         continue
#     print("print i",i)

# n=input("enter a string ")
# vo="a","e","i","o","u"
# count=0
# for i in n:
#     if i in vo:
#         count=count+1
# print("count is ",count)

# l1=[10,20,40,2,40,80,22]
# largest=l1[0]

# for i in l1:
#     if i>largest:
#         largest=i
# print("largest number is ",largest)

# s="programming"
# s1=""
# for i in s:
#     if i not in s1:
#         s1=s1+i
# print(s1)

# # # set slove question
# # a=set(s)
# # print("-".join(a))

# l2=[10,20,30,40,5,50,]
# largest=l2[0]
# sec_largest=l2[0]
# for i in l2:
#     if i >largest:
#         largest=i
# for j in l2:
#     if j > sec_largest and j<largest:
#         sec_largest=j
# print("second largest",sec_largest)

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if i==7:
#         break
#     print(i)

# s4="i love python"
# rev=s4[::-1]
# # print(rev)

# l3=[1,2,3,2,3,4,4,5,78,7,8,7]
# # new=[]
# # for i in l3:
# #     if i not in new:
# #         new.append(i)
# # print(new)
# a=list(set(l3))
# print(a)
# print(type(a))

# ss2="i love python"
# rev="".join(ss2.split()[::-1])
# print(rev)
# print("update")

# user=int(input("enter a number"))
# for i in range(2,user+1):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#         print(i, end=" ")
# n=int(input("enter a number"))
# count=0
# while n>0:
#     n=n//10
#     count=count+1
# print(count)


# l1=[1,2,2,3,1,4,2]
# ch=[]
# for i in l1:
#     if i not in ch:
#         count=0
#         for j in l1:
#          if i==j:
#             count=count+1
#         print(i,"=",count)
#         ch.append(i)

a=10
b=20
c=a*b
print(c)
    
