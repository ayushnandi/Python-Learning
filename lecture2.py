# x = int(input())
# y = int(input())
# if x==y:
#     print("both the no. are equals")
# else:
#     if x>y:
#         print("x is grater")

#     else:
#         print("x is smaller")




# if x<40:
#     print("fail")
# elif x<55:
#     print("third")
# elif x<75:
#     print("second")
# else:
#     print("first")





# print("Enter the data")
# data = []
# for n in range(0,4):
#     data.append(int(input()))

# print(data)




print("Enter your data")
x = int(input())
r = int(x/2)
for n in range(2,r+1):
    if x%n == 0:
        print("its not prime",n)
        break
else:
    print("its prime")





# sum = 0 
# for x in range(10):
#     n = int(input("ENTER no."))
#     if n%2!=0:
#         print(n, " is not even")
#         break
#     sum += n
# print("sum = ",sum )