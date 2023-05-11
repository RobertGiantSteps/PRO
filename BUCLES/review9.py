""" 
Escriba un programa que calcule el máximo común divisor entre dos números enteros. No utilice ningún algoritmo existente. Hágalo probando divisores (solución).

        Entrada: a=12; b=44

        Salida: 4
"""
a = 12
b = 44

if a < b:
    _min = a
else:
    _min = b

for divisor in range(_min, 0, -1):
    if a % divisor == 0 and b % divisor == 0:
        mcd = divisor
        break
else:
    mcd = 1

print(mcd)
    
        
    
        
        


