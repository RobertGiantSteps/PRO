""" 
Escriba un programa que encuentre la mínima secuencia de múltiplos de 3 
(distintos) cuya suma sea igual o superior a un valor dado (solución).

        Entrada: 45

        Salida: 0, 3, 6, 9, 12, 15
"""

value = 45
counter = 0

for i in range(0,value,3):
    counter += i
    print(i,end=' ')
    if counter == value:
        break
    else:
        continue


print()
#SOLUCION:

total_sum = 45
current_sum = 0
current_3mult = 0
print(f'M={current_3mult:2d}: S={current_sum:2d}')

while current_sum < total_sum:
    current_3mult += 3
    current_sum += current_3mult
    print(f'M={current_3mult:2d}: S={current_sum:2d}')