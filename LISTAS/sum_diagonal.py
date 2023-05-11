# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    sum_diagonal = 0
    for i in range(len(matrix)):
    # AQUI ES IMPORTANTE SABER QUE EN LA DIAGONAL EL INDICE DE LA FILA COINCIDE CON EL DE LA COLUMNA POR ESO[i][i]
        sum_diagonal += matrix[i][i]
    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])