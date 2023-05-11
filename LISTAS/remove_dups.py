# *********************
# ELIMINANDO DUPLICADOS
# *********************
"""  
  Dada una lista de números, obtenga otra lista donde se eliminen  │
│ los duplicados. Mantenga el orden de los números en la lista de  │
│ salida tal y como aparecen en la de entrada. 
"""

def run(nums_dups: list) -> list:
    no_repeted_values = []
    for num in nums_dups[:]:
        if num not in no_repeted_values:
            no_repeted_values.append(num)
        
        nums_unique = no_repeted_values

    return nums_unique


if __name__ == '__main__':
    run([0, 9, 0, 9, 0, 9])