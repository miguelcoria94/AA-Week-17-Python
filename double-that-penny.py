print("** Doubling Penny **")

# How many times would a penny need to double to generate a million dollars?
count = 0
total = 0

# STEP 2: Write the while loop

while total < 100000000:
    if total == 0:
        total = 0.01
    else:
        total *=2
    count += 1


print('Double', count, 'times')

# How much money has been generated at that point?
print('${:,}'.format(total))
