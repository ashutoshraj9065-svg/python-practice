# class digital:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
# mobile1=digital("motorola",23000)
# mobile2=digital("sumsung",46000)
# print(mobile1.name)
# print(mobile2.price)


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# s1=student("ashu",478)
# s2=student("banty",460)
# print(s1.marks)
# print(s2.name)


# class student:
#     school="LNCT"

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# s1=student("ashu",460)
# s2=student("rohan",238)
# s3=student("rahul",340)
# s4=student("banty",430)
# s5=student("badall",440)
# print(s1.school,s1.marks)
# print(s2.school,s2.name,s2.marks)
# print(s3.name)
# print(s4.name,s4.marks)
# print(s5.school,s5.name,s5.marks)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks>=260:
#             print("pass")
#         else:
#             print("fail")


# s1=student("ashu",138)
# s1.result()


# class showroom:
#     def __init__(self,brand,price,model):
#         self.brand=brand
#         self.price=price
#         self.model=model

#     def deliver(self,name):
#         if self.price>=5000000 and self.price<8800000:
#             print(f"congratulation {name} ,your {self.brand} is ready for deliver")
#         elif self.price>=8800000:
#             print(f"congratulation {name},your primimum {self.brand}")
#         else:
#             print(f"sorry {name},plese sir ap money laiye")
# c1=showroom("audi",5200000,"xxouy")    
# c2=showroom("g-wagan",9300000,"xxuttr")
# c3=showroom("scorpio",40000,"hghgj")

# c1.deliver("ashu")


# class vechile:
#     def __init__(self,start):
#         self.start=start

# class car(vechile):
#     pass

# c1=car("vechile start ho gai")
# print(c1.start)


# class school:
#     def student(self):
#         print("student data")
# class teacher(school):
#     pass
# c2=teacher()
# c2.student()

# class animal:
#     def eat(self):
#         print("eating animal")

# class dog(animal):
#     def lunch(self):
#         print("dog lunch")
# class cat(animal):
#     pass

# d1=dog()
# print(d1.eat())
# print(d1.lunch())
# c1=cat()
# print(c1.eat())

# class bank:
#     def __init__(self):
#          self.balance=10000
   
#     def show_balance(self):
#          print(self.balance)

# b1=bank()
# b1.show_balance()

# #multiple inheritence

# class father:
#      def __init__(self,name):
#           self.name=name


# class child(father):
#      def __init__(self,name,age):
#           super().__init__(name)
#           self.age=age

# b1=child("bhpendrakumar",52)
# print(b1.name)
# print(b1.age)

print("hello")


    
        