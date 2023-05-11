"""

Escriba un programa en Python que acepte la opción de dos jugadoras en 
Piedra-Papel-Tijera y decida el resultado (solución).

        Entrada: person1=piedra; person2=papel

        Salida: Gana persona2: El papel envuelve a la piedra

"""


SCISSORS= 'scissors'
ROCK = 'rock'
PAPER = 'paper'
person_1 = ROCK
person_2 = PAPER

if person_1 == person_2:
         print('MATCH')

        
if person_1 == ROCK: 
    if person_2 == PAPER:
        print('Win person_2: The paper wraps the stone ')
        
if person_2 == ROCK:
    if person_1 == PAPER:
        print('Win person_1: The paper wraps the stone ')

if person_1 == ROCK:
    if person_2 == SCISSORS:
        print('Win person_1: The rock broke the scissors')
        
if person_2 == ROCK:
    if person_1 == SCISSORS:
        print('Win person_2: The rock broke the scissors')
        
if person_1 == SCISSORS:
    if person_2 == PAPER:
        print('Win person_1: The scissors cut the paper')
        
if person_2 == SCISSORS:
    if person_1 == PAPER:
        print('Win person_2: The scissors cut the paper')
        
        
#SOLUCION:

choose1 = 'piedra'
choose2 = 'papel'

if choose1 == choose2:
    msg = 'Empate'
    winner = 0
elif choose1 == 'piedra' and choose2 == 'tijera':
    msg = 'La piedra aplasta la tijera'
    winner = 1
elif choose1 == 'tijera' and choose2 == 'piedra':
    msg = 'La piedra aplasta la tijera'
    winner = 2
elif choose1 == 'tijera' and choose2 == 'papel':
    msg = 'La tijera corta el papel'
    winner = 1
elif choose1 == 'papel' and choose2 == 'tijera':
    msg = 'La tijera corta el papel'
    winner = 2
elif choose1 == 'papel' and choose2 == 'piedra':
    msg = 'El papel envuelve la piedra'
    winner = 1
elif choose1 == 'piedra' and choose2 == 'papel':
    msg = 'El papel envuelve la piedra'
    winner = 2

if winner == 0:
    msg = 'Empate'
else:
    msg = f'Gana persona{winner}: {msg}'

print(msg)
        
        
        
        
        
            
        

