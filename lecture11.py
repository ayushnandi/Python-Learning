# def get_int(n):
#     try:
#         value = int(input(n))
#         return value
#     except ValueError:
#         print('Invalid Input')

# num = get_int('Input an Integer: ')
# print('Input:', num)






def get_num(p):
    while True:
        try:
            value = float(input(p))
            return value
        except ValueError:
            print('invalid, please put valid i/p')

n1 = get_num("Enter the dividend:")
n2 = get_num("Enter the divisor:")
result = n1 / n2
print(result)






# n = 3
# m = n
# n2 = 0
# for i in range(n):
#     for j in range(m,):
#         if n2 >= n :
#             print(' ')
#         else: 
#             print('*')
        
# print()





# n =  '3'
# print(n.isdigit())