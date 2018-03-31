def intersect(*args):
    res = []
    if args:
        for x in args[0]:
            if x in res:
                continue
            for y in args[1:]:
                if x not in y:
                    break
            else:
                res.append(x)
        print(res)
        return res

#print("Result of intersect(['s','c','a','m'], ['s','r','a','m'])")
#intersect(['s','c','a','m'], ['s','r','a','m'])
#print("Result of intersect(('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])")
#intersect(('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])
intersect([1,2,3,4], [4,5,3,5], [6,7,8])
intersect([1,2,3,4], [4,5,3,5], [6,7,8], ('a','b','c',1,2,3,4,'am'),['sp','am','a',1,2])
intersect('1212143')
intersect()
