""" 
Escriba un programa en Python que acepte dos valores enteros (𝑥 e 𝑦) 
que representarán un punto (objetivo) en el plano. El programa simulará 
el movimiento de un «caballo» de ajedrez moviéndose de forma alterna: 
2 posiciones en 𝑥 + 1 posición en 𝑦. 
El siguiente movimiento que toque sería para moverse 1 posición 
en 𝑥 + 2 posiciones en 𝑦
.El programa deberá ir mostrando los puntos por los que va pasando 
el «caballo» hasta llegar al punto objetivo (solución).

        Entrada: objetivo_x=7; objetivo_y=8;

        Salida: (0, 0) (1, 2) (3, 3) (4, 5) (6, 6) (7, 8)
"""

OBJECTIVE_X = 7
OBJECTIVE_Y = 8

horse_x = 0
horse_y = 0

print(f'({horse_x},{horse_y})',end=' ')

move = True
while horse_x != OBJECTIVE_X and horse_y != OBJECTIVE_Y:
    if move:
        horse_x += 1
        horse_y += 2
    else:
        horse_x += 2
        horse_y += 1
    print(f'({horse_x},{horse_y})',end=' ')
    move = not move

        
    

print()

#Solucion 

# =================================================
# OPCIÓN A
# =================================================
TARGET_X = 7
TARGET_Y = 8

horse_x = 0
horse_y = 0
print(f'({horse_x}, {horse_y})', end=' ')

flow = True
while horse_x != TARGET_X and horse_y != TARGET_Y:
    if flow:
        horse_x += 1
        horse_y += 2
    else:
        horse_x += 2
        horse_y += 1
    print(f'({horse_x}, {horse_y})', end=' ')
    flow = not flow
print()
# =================================================
# OPCIÓN B
# =================================================
TARGET_X = 7
TARGET_Y = 8

horse_x = 0
horse_y = 0

flow = True
while horse_x <= TARGET_X and horse_y <= TARGET_Y:
    print(f'({horse_x},{horse_y})')
    horse_x += 2 - flow
    horse_y += 1 + flow
    flow = not flow
            
            
        
        
    


    
    
        
        
    
    
        

        