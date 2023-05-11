"""
Ejercicio

Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:

    ¿Puede volar?              

    ¿Es humano?

    ¿Tiene máscara?
Ejemplo

        Entrada: can_fly = True, is_human = True y has_mask = True

        Salida: Ironman
fire_risk = 'LOW' if temperature < 30 else 'HIGH'

fire_risk
'HIGH'
"""
can_fly = False
is_human = True
has_mask = True

if can_fly and is_human and has_mask:
    hero = 'Ironman'
elif can_fly and is_human  and not has_mask:
    hero = 'Captain Marvel'
elif can_fly and not is_human and has_mask:
    hero = 'Ronan Accuser'
elif can_fly and not is_human and not has_mask:
    hero = 'Vision'
elif not can_fly and is_human and has_mask:
    hero = 'Spiderman'
elif not can_fly and is_human and not has_mask:
    hero = 'Hulk'
elif not can_fly and not is_human and has_mask:
    hero = 'Black Bolt'
else:
    hero = 'Thanos'
    
print(hero)

#SOLUCION:

can_fly = True
is_human = False
has_mask = False

if can_fly:
    if is_human:
        if has_mask:
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if has_mask:
            print('Ronan Accuser')
        else:
            print('Vision')
else:
    if is_human:
        if has_mask:
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if has_mask:
            print('Black Bolt')
        else:
            print('Thanos')


