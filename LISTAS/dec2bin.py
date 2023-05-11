# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    num_bin = bin(num)
    str_bin = str(num_bin)
    code_part = str_bin.split('b')
    number_part = code_part[1]   
    to_bin = str(number_part)
    return to_bin


if __name__ == '__main__':
    run(1)