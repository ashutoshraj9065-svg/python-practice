# # numbers = [10, 20, 30, 40, 50]
# # count=0
# # sum=0
# # largest=numbers[0]

# # for i in numbers:
# #     count=count+1
# # print(count)

# # for i in numbers:
# #     sum=sum+i
# # print(sum)
 
# # for i in numbers:
# #     if i>largest:
# #         largest=i

# # print(largest)


# # numbers = [18, 7, 25, 3, 12]
# # smallest=numbers[0]

# # for i in numbers:
# #     if smallest>i:
# #         smallest=i
# # print(smallest)

# # numbers = [10, 20, 30, 40, 50]
# # largest=numbers[0]
# # secondlargest=numbers[0]

# # for i in numbers:
# #     if i>largest:
# #          secondlargest=largest
# #          largest=i
      
# # print(secondlargest)
# # print("error")


# # numbers = [12, 45, 7, 89, 23,50]
# # largest=numbers[0]
# # second=numbers[0]
# # third=numbers[0]

# # for i in numbers:
# #     if i > largest:
# #         third=second
# #         second=largest
# #         largest=i
# #     elif i >second:
# #         third=second
# #         second=i
# #     elif i > third:
# #         third=i
# # print(third)
# # print(second)
# # print(largest)
        


# # numbers = [10, 20, 10, 30, 20, 40, 10]
# # count =0
# # for i in numbers:
# #     if i==10:
# #         count=count+1
# # print(count)

# # numbers = [12, 7, 19, 25, 8, 30, 15]
# # count=0


# # for i in numbers:
# #     if i>15:
# #         count=count+1

# # print(count)

# # numbers = [12, 45, 18, 7, 33, 50, 21]
# # min2=numbers[0]

# # for i in numbers:
# #     if min2>i:
# #         min2=i

# # print(min2)

# numbers = [10,20,10,30,20,40,10]

# visited = []

# for i in numbers:

#     if i in visited:
#         continue

#     count = 0

#     for j in numbers:

#         if i == j:
#             count = count + 1

#     print(i, "->", count)

#     visited.append(i)
# a=10
# b=10
# c=a+b
# print(c)
def birthdayCakeCandles(candles):
    largest = candles[0]
    count = 0

    for i in candles:
        if i > largest:
            largest = i
            count = 1
        elif i == largest:
            count += 1

    return count


n = int(input())
candles = list(map(int, input().split()))

answer = birthdayCakeCandles(candles)

print(answer)

    