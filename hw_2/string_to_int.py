def strtoint(string):
  res = 0
  for i in string:
    if ord(i) < 10:
      res *= 10
    elif ord(i) < 100:
      res *= 100
    elif ord(i) < 1000:
      res *= 1000
    res += ord(i)
  print(res)
  return res

print("Result strtoint('abcd'): ")
strtoint('abcd')

# Вариант без свитча
def strtoint2(string):
    res = 0
    pow = 0
    for i in string:
        while(ord(i) // 10**pow):
            pow += 1
        res *= 10**pow
        res += ord(i)
    print(res)
    return res

print("Result strtoint2('abcd'): ")
strtoint2('abcd')
