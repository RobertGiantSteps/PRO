# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************

FIX_VALUE = 5
def run(n: int) -> int:
    str_n = str(n)
    length_number = len(str_n)
    operation = n * FIX_VALUE ** length_number
    result = operation 
    

    return result


if __name__ == '__main__':
    run(10)