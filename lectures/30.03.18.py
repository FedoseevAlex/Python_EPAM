# Task 1
# написать факториал с reduce
#import functools
#
#functools.reduce(lambda a, x: a*x if x else 1, list(range(3)), 1)


# Task 2
# Переписать в функциональном стиле
#names = ['Alexey', 'Ivan', 'Petr']
#
# Заменить имена на хэш
#map(hash, names)

# Task 3
# Переписать в функциональном стиле

#sentences = ['test string', 'with two test words: test and test',
#             'and some without ** string']
# Считаем количество символов во всех строках
#functools.reduce(lambda a, s: a + len(s), sentences, 0)
# Считаем количество вхождений слова 'test'
#functools.reduce(lambda a, s: a + s.count('test'), sentences, 0)
