def char_count(c, s):
    count = 0
    for x in s:
        if c == x:
            count += 1
    return count



print(char_count("a", "App Academy"))         #> 1
print(char_count("c", "Chamber of Secrets"))  #> 1
print(char_count("b", "big fat bubble"))      #> 4