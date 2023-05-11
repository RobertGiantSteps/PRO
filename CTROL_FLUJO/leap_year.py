"""
Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es.
ℹ️ Un año es bisiesto en el calendario Gregoriano, 
si es divisible entre 4 y no divisible entre 100, 
o bien si es divisible entre 400. 
Puedes hacer la comprobación en esta lista de años bisiestos.
Ejemplo

        Entrada: 2008

        Salida: Es un año bisiesto
"""

year = 2028

leap_year = 'its leap year' if year % 4 == 0 else 'not leap year'

print(leap_year)