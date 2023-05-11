# *************
# SUMA REPETIDA
# *************

FIRST_MULTIPLE = 11
SECOND_MULTIPLE = 111
def run(n: int) -> int:
    first_mult = n * FIRST_MULTIPLE 
    second_mult = n * SECOND_MULTIPLE
    
    
    
    result = n + first_mult + second_mult

    return result


if __name__ == '__main__':
    run(3)