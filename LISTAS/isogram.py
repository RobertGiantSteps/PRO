""" 
Ejercicio

Determine si una cadena de texto dada es un isograma, es decir, 
no se repite ninguna letra.

Ejemplos válidos de isogramas:

    lumberjacks

    background

    downstream

    six-year-old

"""

word = 'six-year-old'

is_isogram = []

for letter in word:
    if letter not in is_isogram or letter != letter.isalpha():
        is_isogram.append(letter)
        msg = 'Its a isogram'
    else:
        msg = 'Not a isogram'
        break
print(msg)


#Solucion 

word = 'six-year-old'

seen_letters = []
for letter in word:
    if letter in seen_letters:
        print('â›”ï¸ No es un isograma!')
        break
    if letter.isalpha():
        seen_letters.append(letter)
else:
    print('âœ… SÃ­ es un isograma!')
        