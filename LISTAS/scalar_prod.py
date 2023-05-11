""" 
Dados dos vectores (listas) de la misma dimensión, 
utilice la función zip() para calcular su producto escalar.
Ejemplo

        Entrada:

        v1 = [4, 3, 8, 1]
        v2 = [9, 2, 7, 3]

        Salida: 101

    𝑣1⋅𝑣2=[4⋅9+3⋅2+8⋅7+1⋅3]=101

"""

vector1 = [4, 3, 8, 1]
vector2 = [9, 2, 7, 3]
scalar_prod = 0

for v1,v2 in zip(vector1,vector2):
    scalar_prod += (v1 * v2)
print(scalar_prod)


#Solucion:

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

result = 0
for value1, value2 in zip(v1, v2):
    result += value1 * value2

print(result)