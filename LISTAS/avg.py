""" 
Lea desde línea de comandos una serie de números 
y obtenga la media de dichos valores 
(muestre el resultado con 2 decimales).

La llamada se haría de la siguiente manera:

$ python avg.py 32 56 21 99 12 17

Plantilla de código para el programa:


Ejemplo

        Entrada: 32 56 21 99 12 17

        Salida: 39.50

"""



import sys

values = sys.argv[1:]
values = [int(v) for v in values]

sum_ = sum(values)
avg = sum_ / len(values)

print(f'La media es {avg:.2f}')

