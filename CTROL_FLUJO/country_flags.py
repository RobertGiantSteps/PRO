"""
Escriba un programa en Python que acepte un país (como «string») y muestre por pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de países (solución).

        Entrada: Italia

        Salida: 🇮🇹
"""



country = 'Japon'

match country:
    case  'Argentina':
        flag = '🇦🇷'
    case 'Italy':
        flag = '🇮🇹'
    case 'Cuba':
        flag = '🇨🇺'
    case 'France':
        flag = '🇫🇷'
    case _:
        flag = f'No flag found'
print(flag)


#SOLUCION:

country = 'Italia'

if country == 'Italia':
    flag = '🇮🇹'
elif country == 'Rusia':
    flag = '🇷🇺'
elif country == 'Taliandia':
    flag = '🇹🇭'
elif country == 'Suecia':
    flag = '🇸🇪'
else:
    flag = '🏳'

print(flag)


