# Write your function, here.
def is_same_num(num1, num2):
    if(num1 == num2):
        return True
    else:
        return False

print(is_same_num(4, 8))  # >  False
print(is_same_num(2, 2))  # >  True
print(is_same_num(2, "2"))  # >  False
