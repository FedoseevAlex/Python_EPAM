def union(*args):
    res = []
    for x in args:
        for y in x:
            if y not in res:
                res.append(y)
    print(res)
    return res

print("Result of union(['s','c','a','m'], ['s','r','a','m'])")
union(['s','c','a','m'], ['s','r','a','m'])
print("Result of union(['s','c','a','m'], ['s','r','a','m'])")
union(('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])
