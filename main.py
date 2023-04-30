print('CALCULADORA:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione a tecla s para sair')

op = input('Qual operação deseja realizar?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))

while(op != 's'):
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x,y, res))

    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))

    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))

    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))

    else:
        print('Operação inválida.')

    op = input('Qual operação deseja realizar?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))

print('Encerrando o programa.')


print('CALCULADORA:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione a tecla s para sair')

while True:
    op = input('Qual operação deseja realizar?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))

    if (op == '+'):
        res = x+y
        print('Resultado: {} + {} = {}'.format(x,y, res))
        continue

    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue

    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif(op == 's'):
        break
    else:
        print('Operação inválida.')


print('Encerrando o programa.')




#for i in range (3,13,1):
#    print(i)

#i = 3
#while(i < 13):
#    print(i)
#    i = i +1

#for i in range (0,9,2):
#    print(i)

#x=0
#while(x<9):
#    print(x)
#    x=x+2