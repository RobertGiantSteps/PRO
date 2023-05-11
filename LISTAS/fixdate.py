""" 
Ejercicio

Consiga la siguiente transformación:

12/31/20 ➡️ 31-12-2020

"""

date = '12/31/20'
cut_date = date.split('/')
new_date = []

day = cut_date[1]
month = cut_date[0]
year = cut_date[2] + '20'

new_date.append(day)
new_date.append(month)
new_date.append(year)

fixdate = '-'.join(new_date)

print(fixdate)

#SOLUCION 

print()


input_date = '12/31/20'

splitted_date = input_date.split('/')
day = splitted_date[1]
month = splitted_date[0]
year = '20' + splitted_date[2]

output_date = '-'.join([day, month, year])
print(output_date)



