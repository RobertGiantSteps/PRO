# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************

""" 
Dada una lista, genere otra lista eliminando   │
│ los elementos duplicados consecutivos.  
"""

def run(items: list) -> list:

    no_repeted = []
    # Agregar el primer elemento a la nueva lista
    no_repeted.append(items[0])
    
    # Recorrer la lista y comparar elementos consecutivos
    for i in range(1, len(items)):
        if items[i] != items[i-1]:
            no_repeted.append(items[i])

          
    result = no_repeted

    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])