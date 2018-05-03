# Task #L7.1
# Написать генератор, сходный по функционалу с zip
"""
def myzip(*args):
    iargs = [iter(arg) for arg in args]
    while iargs:
        for iarg in iargs.copy():
            try:
                yield next(iarg)
            except StopIteration:
                iargs.remove(iarg)

print(list(myzip(['a', 'b', 'c', 'd'], (1, 2, 3))))
print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3))))
"""

