arr = ["apple","banana","mango"]
def longestsubString(wrd):
    max = 0
    for i in wrd:
        if len(i) > max:
          max = len(i)
    return max
print(arr[0].upper())

# string mai upper krne k liye    -----   .upper()    ---   use krna hai
# anad length l liyee     -----------     len("abc")     ------     use krna hai 

print(longestsubString(arr)) 