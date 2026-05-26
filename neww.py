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

# qno 1 
n=int(input("enter a number"))
original=n
reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if original==reverse:
    print("planidrom ")
else:
    print("not planidrom")

l1=[1,2,3,4,5,6,7]
count=0
for i in l1:
    if i%2==0:
        count=count+1
print(count)       

def fact(n):
    fact1=1
    for i in range(n-1):
        fact1=fact1*i
    return fact1
n=int(input("enter a number "))
a=fact(n)
print(a)

