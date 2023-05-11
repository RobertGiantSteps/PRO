""" 
Ejercicio

Imprima los 100 primeros números de la sucesión de Fibonacci: 
0,1,1,2,3,5,8,13,21,34,55,89,…

"""

a = 0
print(a)
b = 1
print(b)

for _ in range(20):
    r = a + b
    a = b
    b = r
    print(r)