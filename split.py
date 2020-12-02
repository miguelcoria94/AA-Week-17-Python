# Write your function, here.
# Write your function, here.
def cap_space(s):
  result = ""
  i = 0
  while i < len(s):
    if s[i].isupper():
      result += " "
    result += s[i]
    i += 1
  return result.lower()



print(cap_space("helloWorld"))  # > "hello world"
print(cap_space("iLoveMyTeapot"))  # > "i love my teapot"
print(cap_space("stayIndoors"))  # > "stay indoors"
