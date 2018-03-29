for i in range(1,101):
  ToPrint = ''
  if i % 3 == 0:
    ToPrint += 'Fizz'
  if i % 5 == 0:
    ToPrint += 'Buzz'
  if ToPrint == "":
    ToPrint = str(i)
  print(ToPrint)
