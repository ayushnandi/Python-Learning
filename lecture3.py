# def function()


# # error beacause len(fruit) is not storing data anywhere
# fruit = "banana"
# len(furit)





# index = 0
# while index < len(fruit):
#     letter= fruit[index]
#     print(letter)
#     index = index +1






# # index value notation 
# s = "hello world"
# print(s[0:5:2])





# # list are none mutable, the value of list can not be updated 
# greeting = "hello world"
# greeting[0] = 'j'#error in this line , as it can not be mutated
# print(greeting) 





# # here the value is added in the string there for adding element in list is applicable
# greeting = "hello world"
# greeting = 'j' + greeting[1:]
# print (greeting)






# # this function defines that is there (ch) char is present in st string or not if not return -1 or elif return the index of char present in string 
# def myfind(st, ch):
#     i = 0
#     while i <= len(st)-1:
#         if st[i] == ch:
#             return i
#         i = i+1
#     return -1
# i = myfind("ayushnandi", "d")
# print(i)






# # count the no. of times the char is appearing on the string 
# def cnt(str , ch ):
#     i = 0
#     count = 0
#     while i <= len(str)-1:
#         if str[i] == ch:
#             count = count+1
#         i = i+1
#     return count
# i = cnt("ayushnandi", "a")
# print(i)





# # verify the data and print function
# from string import*
# frt = "banana apple"
# f= "10"
# f1= " "
# print(len(frt))
# print(frt.find('b'))
# print(ascii_lowercase)
# print(ascii_uppercase)
# print(digits)
# print(frt.upper())
# print(frt.lower())   
# print(frt.istitle()) # check if title
# print(f1.isspace())  # check if space
# print(f.isdigit())   # check if no.





print(list(range(1,10,2)))

num =[17,123]
voc = []