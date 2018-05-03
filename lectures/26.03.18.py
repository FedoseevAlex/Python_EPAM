# Task 1 из лекции
#def intersect(*args):
#    res = []
#    for x in args[0]:
#        if x in res:
#            continue
#        for y in args[1:]:
#            if x not in y:
#                break
#            else:
#                res.append(x)
#    print(res)
#    return res
#intersect(['s','c','a','m'], ['s','r','a','m'])
#intersect(('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])

#def union(*args):
#    res = []
#    for x in args:
#        for y in x:
#            if y not in res:
#                res.append(y)
#    print(res)
#    return res
#union(['s','c','a','m'], ['s','r','a','m'])
#union(('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])


# Task 2 из лекции
#def strtoint(string):
#  res = 0
#  for i in string:
#    if ord(i) < 10:
#      res *= 10
#    elif ord(i) < 100:
#      res *= 100
#    elif ord(i) < 1000:
#      res *= 1000
#    res += ord(i)
#  print(res)
#  return res
#
#strtoint('abcd')

# Вариант без свитча
#def strtoint(string):
#    res = 0
#    pow = 0
#    for i in string:
#        while(ord(i) // 10**pow):
#            pow += 1
#        res *= 10**pow
#        res += ord(i)
#        print('pow is: {}'.format(pow))
#    print(res)
#    return res
#
#strtoint('abcd')


# Task 3 из лекции
#def wrapper(func):
#    def inner(*args, **kwargs):
#        print('Function name {}'.format(func.__name__))
#        func(*args, **kwargs)
#    return inner
#
#wr = wrapper(print)
#wr('Hello')
