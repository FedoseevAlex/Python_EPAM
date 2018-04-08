#!/usr/bin/env/ python3.6
# HW #L5.1 Matrix


class Matrix:
    import random
    from functools import reduce
    
    def __init__(self, *args) -> None:
        if len(args) == 1:
            matrix = args[0]
            # Check matrix consistency
            # If all rows have equal length -> True
            if len(set([len(row) for row in matrix])) == 1:
                self.matrix = matrix
                self.rows = len(self.matrix)
                self.columns = len(self.matrix[0])
            else:
                raise ValueError('Inconsistent matrix. Inequality of row lengths.')
        elif len(args) == 2:
            self.rows = args[0]
            self.columns = args[1]
            self.matrix = [self.random.sample(range(101), self.columns) for usless_var in range(self.rows)]
        else:
            raise ValueError('Wrong number of arguments.')
            
    def __str__(self):
        self.__string = str(self.matrix)
        return self.__string
    
    def __getitem__(self, pos):
        row, column = pos
        return self.matrix[row][column]
    
    def __setitem__(self, pos, value):
        row, column = pos
        self.matrix[row][column] = value
    
    def __repr__(self):
        self.__rstring = '\n'.join([str(row) for row in self.matrix])
        return self.__rstring
    
    def __add__(self, other):
        if other.rows == self.rows and other.columns == self.columns:
            return Matrix([list(map(lambda x, y: x + y,
                                    self.matrix[row],
                                    other.matrix[row])) for row in range(self.rows)])
        else:
            raise ValueError('Matrix sizes are not equal.')
            
    def __sub__(self, other):
        if other.rows == self.rows and other.columns == self.columns:
            return Matrix([list(map(lambda x, y: x - y,
                                    self.matrix[row],
                                    other.matrix[row])) for row in range(self.rows)])
        else:
            print('Make exception here')
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                other = other.transpose()
                result = list()
                for row in range(self.rows):
                    raw = list()
                    for column in range(other.rows):
                        res = list(map(lambda x, y: x * y, self.matrix[row], other.matrix[column]))
                        res = self.reduce(lambda a, i: a + i, res, 0)
                        raw.append(res)
                    result.append(raw)
                return Matrix(result)
            else:
                raise ValueError('Unsuitable dimensions of operands.')
        elif isinstance(other, int):
            res = list()
            for row in range(self.rows):
                res.append([item * other for item in self.matrix[row]])
            return Matrix(res)
        else:
            raise ValueError('Wrong operand type. Must be int or Matrix.')
            
    def __eq__(self, other):
        if other.rows == self.rows and other.columns == self.columns:
            result = True
            for row in range(self.rows):
                for col in range(self.columns):
                    result = result and self.matrix[row][col] == other.matrix[row][col]
        else:
            raise ValueError('Unsuitable dimensions of operands.')
        return result
    
    def is_square(self):
        """
        Check if matrix is square.
        >>> a = Matrix([[1, 2], [3, 4]])
        >>> a.is_square()
        True
        >>> b = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> b.is_square()
        False
        :return: bool True or False.
        """
        return self.rows == self.columns
        
    def transpose(self):
        """
        Transpose matrix.
        >>> a = Matrix([[1, 2], [3, 4]])
        >>> a
        [1, 2]
        [3, 4]
        >>> b = a.transpose()
        >>> b
        [1, 3]
        [2, 4]
        :return: Matrix object
        """
        res = list()
        for col in range(self.columns):
            res.append([self.matrix[row][col] for row in range(self.rows)])
        return Matrix(res)
        
    def is_symmetric(self, diag='main'):
        """
        Check if matrix is symmetrical with respect to the main or anti diagonal.
        By default checking by main diagonal.
        >>> a = Matrix([[1, 1, 3], [1, 1, 2], [3, 2, 1]])
        >>> a
        [1, 1, 3]
        [1, 1, 2]
        [3, 2, 1]
        >>> a.is_symmetric()
        True
        >>> b = Matrix([[5, 4, 1], [6, 2, 4], [3, 6, 5]])
        >>> b
        [5, 4, 1]
        [6, 2, 4]
        [3, 6, 5]
        >>> b.is_symmetric(diag='anti')
        True
        >>>
        :param diag: could be 'main' or 'anti'. Specify diagonal for symmetric check.
        :type diag: str.
        :return: None.
        """
        if self.is_square():
            if diag == 'main':
                return self == self.transpose()
            elif diag == 'anti':
                to_compare = []
                for row in range(self.rows):
                    to_compare.append(self.matrix[row][::-1])
                to_compare = Matrix(to_compare[::-1])
                return self == to_compare.transpose()
            else:
                raise ValueError("Wrong diag. Could be 'main' or 'anti")
        else:
            raise ValueError("Non square matrix.")
    

# Tests
b = Matrix([[1, 2], [3, 4]])
c = Matrix([[1, 2, 3, 4, 5, 6, 7]])
v = Matrix(2, 2)
try:
    t = Matrix([[1, 2, 3], [4, 5, 6, 43]])
except ValueError:
    print('Error during matrix creation!')

k = b * 3
print(k)
k = b + v
print(k)
k = b - v
print(b.transpose())
print(v.transpose())

