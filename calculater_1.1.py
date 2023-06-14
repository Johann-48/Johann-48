from math_library import sum, sub, mul, div

n1 = float (input('First number: '))
signal = input('Chose the signal(+, -, *, or /): ')
n2 = float (input('Second number: '))
result = 0.0
if signal == '-':
  result = sub(n1, n2)
  
elif signal == '+': 
  result = sum(n1, n2)

elif signal == '*': 
  result = mul(n1, n2)

elif signal == '/': 
  result = div(n1, n2)

else:
  print('ERROR')
print(result)