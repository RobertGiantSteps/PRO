""" 
Dado su tamaño, muestre por pantalla un mosaico donde la diagonal 
principal esté representada por X, 
la parte inferior por D y la parte superior por U.

Ejemplo

        Entrada: 5

        Salida:

        X U U U U
        D X U U U
        D D X U U
        D D D X U
        D D D D X
"""

size = 5

for row in range(size):
    for col in range(size):
        if row < col:
            symbol = 'U'
        elif row > col:
            symbol = 'D'
        else:
            symbol = 'X'
        print(symbol, end=' ')
    print()
    
