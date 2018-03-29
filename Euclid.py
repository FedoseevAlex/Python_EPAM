a = ''
b = ''
while not a.isdecimal():
  a = input('Enter first number >> ')

while not b.isdecimal():
  b = input('Enter second number >> ')

a = int(a)
b = int(b)

while a and b:
  if a >= b:
    a %= b
  else:
    b %= a
res = a | b
print('Greatest common divisor: {}'.format(res))
