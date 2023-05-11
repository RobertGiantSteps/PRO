""" 
Ejercicio

Escriba un programa que encuentre todos los múltiplos de 5 menores que un valor dado:
Ejemplo

        Entrada: 36

        Salida: 5 10 15 20 25 30 35

"""
target = 36

five_constant = 5

while five_constant < target:
    print(five_constant,end=' ')
    five_constant += 5
    
print()    
#Solucion

target = 36
num = 5
while num < target:
    print(num, end=' ')
    num += 5