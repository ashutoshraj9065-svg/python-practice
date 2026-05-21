# print("hello")
def sq_fun(n):
    
        sa=n**2
        return sa
n=int(input("enter a number"))
print(sq_fun(n))
# print(sq_fun())

def even_as(n):
        if n%2==0:
            return "even number"
        else:
             return "odd number"
n=int(input("enter a value"))
rs=even_as(n)
print(rs)

def ashu(n):
      if n>1:
            for i in range(2,n):
                  if n%i==0:
                        return "not prime"
            else:
                return "prime number"
      else:
            return "not prime"
n=int(input("enter a number"))
a=ashu(n)
print(a)