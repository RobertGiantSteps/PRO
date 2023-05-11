# ****************
# EL CUADRADO ROJO
# ****************


"""
Lado = √(Área)

Lado = (Diagonal) / √2

"""
def run(arc_A: float) -> float:
    pi = 3.14 
    square_area = (arc_A ** 2) / (8 * pi)
    area = square_area

    return area


if __name__ == '__main__':
    run(1)