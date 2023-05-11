"""

Escriba un programa en Python que acepte edad, peso, pulso y plaquetas, 
y determine si una persona cumple con estos requisitos para donar sangre.

        Entrada: edad=34; peso=81; heartbeat=70; plaquetas=150000
        Salida: Apto para donar sangre

"""

age = 34

weigh = 81

heart_beat = 80

platelets = 149000

if 18 <= age <= 65 and weigh >= 50 and 50 <= heart_beat <= 110 and platelets >= 150000:
    msg = 'Ready to donate'
else:
    msg = 'forgot about it '
    
print(msg) 
