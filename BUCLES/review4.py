"""  
Escriba un programa en Python que acepte una cadena de texto e indique si todos 
sus caracteres son alfabéticos. No usar la función isalpha() 
sino una constante ALPHABET = 'abcdefghijklmnopqrstuvwxyz' (solución)

        Entrada: hello-world

       Salida: Se han encontrado caracteres no alfabéticos
       
EJEM MORSA 
while not (name := input('¿Su nombre? ').istitle())

"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


input_strings = 'hello world'
clean_input = input_strings.replace(' ', '')


for letter in clean_input:
    if letter not in ALPHABET:
        msg = 'Non-alphabetic char found!'
        break
else:
    msg = 'All chars are alphabetic'
        
print(msg)


#SOLUCION:

text = 'hello-world'

for char in text:
    if not char.isalpha():
        print('Non-alphabetic char found!')
        break
else:
    print('All chars are alphabetic')
        
    



