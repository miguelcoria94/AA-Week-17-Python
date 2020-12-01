# Write your function, here.
# Parameters are in this order: chickens, cows, pigs

def how_many_legs(chicken, cows, pigs):
    total = 0

    chicken_legs = chicken * 2
    cows_legs = cows * 4
    pig_legs = pigs * 4
    return chicken_legs + cows_legs + pig_legs


print(how_many_legs(2, 3, 5))  # > 36
print(how_many_legs(1, 2, 3))  # > 22
print(how_many_legs(5, 2, 8))  # > 50
