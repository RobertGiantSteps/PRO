"""
Ejercicio

Dada la variable:

e = 2.71828

, obtenga los siguientes resultados utilizando «f-strings»:

'2.718'
'2.718280'
'    2.72'  # 4 espacios en blanco
'2.718280e+00'
'00002.7183'
'            2.71828'  # 12 espacios en blanco
"""

e = 2.71828

print(f'{e:.3f}')

print()

print(f'{e:f}')

print()

print(f'{e:8.2f}')

print()

print(f'{e:e}')

print()

print(f'{e:010.4f}')

print()

print(f'{e:19.5f}')

