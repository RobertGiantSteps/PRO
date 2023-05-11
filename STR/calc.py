"""
Ejercicio
Escriba un programa en Python que lea por teclado dos números enteros y 
muestre por pantalla el resultado de realizar las operaciones básicas entre ellos.
Ejemplo
        Valores de entrada 7 y 4.

        Salida esperada:

        7+4=11
        7-4=3
        7*4=28
        7/4=1.75

Consejo
Aproveche todo el potencial que ofrece print() para conseguir la salida esperada.

"""

first_value = int(input('Please insert the first value: '))

second_value = int(input('Please insert the second value: '))


#Operations:

addition = first_value + second_value
print(f'{first_value} + {second_value} = {addition}')

subtraction = first_value - second_value
print(f'{first_value} - {second_value} = {subtraction}')

multiplication = first_value * second_value
print(f'{first_value} * {second_value} = {multiplication}')

division = first_value / second_value
print(f'{first_value} / {second_value} = {division}')