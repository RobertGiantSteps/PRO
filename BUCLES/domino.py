"""   
Escriba un programa que muestre por pantalla todas las fichas del dominó. 
La ficha «en blanco» se puede representar con un 0 


0|0 0|1 0|2 0|3 0|4 0|5 0|6
1|1 1|2 1|3 1|4 1|5 1|6
2|2 2|3 2|4 2|5 2|6
3|3 3|4 3|5 3|6
4|4 4|5 4|6
5|5 5|6
6|6
"""
MAX_VALUE = 9

for blue in range(MAX_VALUE + 1):
    for red in range(blue,MAX_VALUE + 1 ):
        domino = f'{blue}|{red}'
        print(domino,end=' ')
    print()
   


#SOLUCION 
MAX_DOMINO = 6

for up_part in range(MAX_DOMINO + 1):
    for down_part in range(up_part, MAX_DOMINO + 1):
        domino = f'{up_part}|{down_part}'
        print(domino, end=' ')
    print()    