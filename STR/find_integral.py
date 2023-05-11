# *********************
# ENCUENTRA LA INTEGRAL
# *********************

EXP = 'x^'
def run(symbol: str) -> str:
    cut_numbers = symbol.split(',')
    coefficient = cut_numbers[0]
    exponent = cut_numbers[1]
    add_exponent = int(exponent) + 1
    operation = int(coefficient) // add_exponent
    str_integral = str(operation) + EXP + str(add_exponent)
    integral = str_integral

    return integral


if __name__ == '__main__':
    run('3,2')