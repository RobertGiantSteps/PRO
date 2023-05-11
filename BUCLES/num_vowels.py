""" 
Ejercicio

Dada una cadena de lettero, indique el número de vocales que tiene.

Ejemplo

        Entrada: Supercalifragilisticoespialidoso

        Salida: 15

"""

VOWELS = 'aeiou'
num_vowels = 0

input = 'Supercalifragilisticoespialidosoeia'

for letter in input:
    if letter in VOWELS:
        num_vowels += 1
print(num_vowels)
        

print()
#(SOLUCION)

VOWELS = 'aeiou'
input = 'Supercalifragilisticoespialidoso'

num_vowels = 0
for letter in input.lower():
    if letter in VOWELS:
        num_vowels += 1

print(num_vowels)