n1 = float (input('First number: '))
signal = input('Chose the signal(+, -, *, or /): ')
n2 = float (input('Second number: '))
if signal == '-':
  m = n1 - n2
  print('SUB: ', m)
  
elif signal == '+': 
  s = n1 + n2
  print('SUM: ', s)

elif signal == '*': 
  m = n1 * n2
  print('MUL: ', m)

elif signal == '/': 
  d = n1 / n2
  print('DIV: ', d)

else:
  print('ERROR')