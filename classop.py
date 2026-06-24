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


class student:
    school="LNCT"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=student("ashu",460)
s2=student("rohan",238)
s3=student("rahul",340)
s4=student("banty",430)
s5=student("badall",440)
print(s1.school,s1.marks)
print(s2.school,s2.name,s2.marks)
print(s3.name)
print(s4.name,s4.marks)
print(s5.school,s5.name,s5.marks)