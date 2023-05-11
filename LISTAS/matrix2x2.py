""" 
jercicio

Escriba un programa que permita multiplicar únicamente matrices de 2 filas por 2 columnas. Veamos un ejemplo concreto:

A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

El producto ℙ=𝐴×𝐵

se calcula siguiendo la multiplicación de matrices tal y como se indica a continuación:
ℙ=(6[00]8[10]4[01]9[11])×(3[00]1[10]2[01]7[11])=(6⋅3+4⋅18⋅3+9⋅16⋅2+4⋅78⋅2+9⋅7)=(22334079)
"""

matrix_a = [[6, 4], [8, 9]]

matrix_b = [[3, 2], [1, 7]]

for a,b in zip(matrix_a,matrix_b):
    first_mult = matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0]
    second_mult = matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]
    third_mult = matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0]
    fourth_mult = matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]
print(f'({first_mult} {second_mult})')
print(f'({third_mult} {fourth_mult})',end=' ')


print()
#SOLUCION:

A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

element00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
element01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
element10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
element11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

result = [[element00, element01], [element10, element11]]

print(result)


#SOLUCION (solucion generalizada para matrices de cualquier dimensión)

A = [[6, 4, 2], [8, 9, 1]]
B = [[3, 2], [1, 7], [9, 6]]

output_num_rows = len(A)
intermatrix_count = len(B)  # = len(A[0])
output_num_cols = len(B[0])

P = []
for i in range(output_num_rows):
    row = []
    for j in range(output_num_cols):
        result = 0
        for k in range(intermatrix_count):
            result += A[i][k] * B[k][j]
        row.append(result)
    P.append(row)

print(P)