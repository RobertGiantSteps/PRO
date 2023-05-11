""" 
Escriba un programa en Python que acepte un número entero 𝑛

    y realice el siguiente cálculo de productos sucesivos (solución):

∏𝑖=1𝑛𝑖^2=1^2⋅2^2⋅3^2⋅⋯⋅𝑛^2


"""

n = 5
a = 0
b = 1 ** 2

for i in range(1 ,n + 1):
    a = i ** 2
    b *= a
    
print(b)


print()
#SOLUCION:

n = 5

acc = 1
for i in range(1, n + 1):
    acc *= i ** 2

print(acc)
    

    