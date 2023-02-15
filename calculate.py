def arithmetic(a, b, c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
    else: 
        print('incorrectly')
        
        
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = input('Enter operator:')

arithmetic(a, b, c)
