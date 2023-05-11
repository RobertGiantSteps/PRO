""" 
Escriba un programa en Python que realice las siguientes 9 multiplicaciones. 
¿Nota algo raro en el resultado? (solución)


1⋅1
11⋅11
111⋅111
1111·1111
11111·11111 
asi hasta el 9

"""
max_multiple = 10
string_number = '1'

for i in range(1,max_multiple):
    all_numbers = string_number * i
    op = int(all_numbers) * int(all_numbers)
    msg = f'{all_numbers} * {all_numbers} = {op}'
    print(msg)
    
print()   
#SOLUCION 

one = '1'
for i in range(1, 10):
    factor = int(one * i)
    result = factor * factor
    print(f'{factor} · {factor} = {result}')