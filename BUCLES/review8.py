""" 

Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud (solución).

        Entrada: 0001010011101 y 0000110010001

        Salida: 4
    La distancia Hamming entre 1011101 y 1001001 es 2.
    La distancia Hamming entre 2143896 y 2233796 es 3.
    La distancia Hamming entre "tener" y "reses" es 3.

"""

str_1 = '2143896'
str_2 = '2233796'
hamming = 0

for value in range(len(str_1)):
    if str_1[value] != str_2[value]:
        hamming += 1
    else:
        continue
print(hamming)


#SOLUCION

str1 = '0001010011101'
str2 = '0000110010001'

distance = 0

# Suponemos que ambas cadenas tienen la misma longitud
for i in range(len(str1)):
    if str1[i] != str2[i]:
        distance += 1
print(distance)




        
    





    
            
        
          




