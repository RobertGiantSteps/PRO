""" 
Ejercicio

Determine si un número dado es un número primo.

No es necesario implementar ningún algoritmo en concreto. 
La idea es probar los números menores al dado e ir viendo si 
las divisiones tienen resto cero o no.
¿Podría optimizar su código? ¿Realmente es necesario probar con tantos divisores?
Ejemplo

        Entrada: 11

        Salida: Es primo

"""

number = 10

for value in range(2,number // 2):
    if number % value == 0:
        print('Not prime')
        break
else:
    print('Yeah! We have a prime number')
        
       

print('SOLUCION')        
#Solicion 
n = 10

for i in range(2, n // 2):
    if n % i == 0:
        print("It's not prime")
        break
else:
    print('Yeah! We have a prime number')
