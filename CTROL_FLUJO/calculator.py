"""
Ejercicio

Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando (suma, resta, multiplicación, división) y calcule el resultado de la operación, 
usando para ello la sentencia match-case.
Controlar que la operación no sea una de las cuatro predefinidas. 
En este caso dar un mensaje de error y no mostrar resultado final.
Ejemplo

    Entrada: 4, 3, +

    Salida: 4+3=7

"""

first_value = float(input('Enter ther first value: '))
second_value = float(input('Enter the second value: '))
operand = input( 'Enter a operant: ')



match operand:
    case '+':
        result = first_value + second_value
        msg = f'{first_value} {operand} {second_value} = {result}'
        print(msg)
    case '-':
        result = first_value - second_value
        msg = f'{first_value} {operand} {second_value} = {result}'
        print(msg)
    case '*':
        result = first_value * second_value
        msg = f'{first_value} {operand} {second_value} = {result}'
        print(msg)
        
    case '/':
        result = first_value / second_value
        msg = f'{first_value} {operand} {second_value} = {result}'
        print(msg)
    case _:
        msg = 'Operant not found !!'
        print(msg)
        
        
#Solucion:

value1 = int(input('Introduzca el primer valor: '))
value2 = int(input('Introduzca el segundo valor: '))
op = input('Introduzca la operación: ')

match op:
    case '+':
        result = value1 + value2
    case '-':
        result = value1 - value2
    case '*':
        result = value1 * value2
    case '/':
        result = value1 / value2
    case _:
        result = None
        print('Operación inválida')

if result is not None:
    print(f'{value1}{op}{value2} = {result}')
        