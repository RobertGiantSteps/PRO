# ************
# VALOR MÁXIMO
# ************
""" 
Dada una lista de valores numéricos enteros, obtenga su máximo valor.                                  │
│                                                                                                        │
│ Prohibido utilizar:                                                                                    │
│                                                                                                        │
│  • La función "built-in" max().                                                                        │
│  • La función "built-in" sorted().

"""

def run(values: list) -> int:
    greatest_number = values[0]
    max_value = 0
    for value in range(len(values)):
        if values[value] > greatest_number:
            greatest_number = values[value]
    max_value = greatest_number
     
            
        

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])