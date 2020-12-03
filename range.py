print('THREE CASES FOR RANGE')
print('A) End Value')

# STEP 1: Change the zero in the range to 10
#         Notice how "10" is not included in the output
for i in range(10):
    print(i)

print('B) Start & End Values')

# STEP 2: Code a `for` loop to print numbers 5 through 9
for i in range(5,10):
    print(i)


print('C) Only Even Values')

# STEP 3: Print 0, 2, 4, 6 and 8 using a for loop
#         Hint - range can take a 3rd parameter for the step distance

for i in range(0,9,2):
    print(i)


# Write your function, here.
def get_sum_of_elements(list):
    total = 0
    for i in list:
        total += i

    return total


print(get_sum_of_elements([2, 7, 4]))  # > 13
print(get_sum_of_elements([45, 3, 0]))  # > 48
print(get_sum_of_elements([-2, 84, 23]))  # > 105


# Write your function, here.

def get_indices(list, val):
    indicies = []
    for i in range(0, len(list)):
        if val == list[i]:
            indicies.append(i)
    return indicies
    
        

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
# Prints [0, 1, 3, 5]

print(get_indices([1, 5, 5, 2, 7], 7))
# Prints [4]

print(get_indices([1, 5, 5, 2, 7], 5))
# Prints [1, 2]

print(get_indices([1, 5, 5, 2, 7], 8))
# Prints []
