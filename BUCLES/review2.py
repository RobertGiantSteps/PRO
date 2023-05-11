""" 
    Escriba un programa que pida nombre y apellidos de una persona 
    (usando un solo input) y repita la pregunta mientras el nombre 
    no esté en formato título (solución).

¿Su nombre? ana torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana Torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana Torres Blanco


"""

correct_format = False

while correct_format == False:
    name = input('¿Su nombre? ')
    if name == name.title():
        print('Formato Correcto !!')
        correct_format = True
    else:
        continue
    
#Solucion:

# OPCIÓN A
while True:
    name = input('¿Su nombre? ')
    if name.istitle():
        break
    print('Error. Debe escribirlo correctamente')

# OPCIÓN B
while not (name := input('¿Su nombre? ').istitle()):
    print('Error. Debe escribirlo correctamente')
    
