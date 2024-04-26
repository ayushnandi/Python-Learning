


def validate_password(password):
   
    has_lower = False
    has_upper = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
    if not (has_lower and has_upper):
        return False
    
   
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False
    special_chars = {'$', '#', '@'}
    has_special = any(char in special_chars for char in password)
    if not has_special:
        return False
    
    # Minimum length 6 characters and maximum length 16 characters
    if len(password) < 6 or len(password) > 16:
        return False
    
    return True

# driver code
password = input("Enter a password: ")
print("password entered = ",password)
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password.")