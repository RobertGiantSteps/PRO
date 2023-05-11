""" 

Escriba un programa en Python que acepte dos cadenas de texto y 
compute el producto cartesiano letra a letra entre ellas (solución).

        Entrada: str1=abc; str2=123

        Salida: a1 a2 a3 b1 b2 b3 c1 c2 c3

"""
str1='abc'

str2='123'

for i in str1[:]:
    for z in str2[:]:
        print(f'{i}{z}',end=' ')
        
print()

#SOLUCION 

str1 = 'abc'
str2 = '123'

for char1 in str1:
    for char2 in str2:
        print(f'{char1}{char2}', end=' ')
    