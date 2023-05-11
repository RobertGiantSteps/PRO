"""

Escriba un programa en Python que acepte 3 códigos de teclas y 
muestre por pantalla la acción que se lleva a cabo en sistemas 
Ubuntu Linux (solución).

        Entrada: tecla1=Ctrl; tecla2=Alt; tecla3=Del;

        Salida: Log out

"""

key_1 = 'Alt'

key_2 = 'Tab'

key_3 = 'Tab'

if key_1 == 'Ctrl' and key_2 == 'Alt' and key_3 == 'Del':
    msg = f'{key_1} + {key_2} + {key_3} : Log out'
elif key_1 == 'Ctrl' and key_2 == 'Alt' and key_3 == 'T':
    msg = f'{key_1} + {key_2} + {key_3} : New Terminal'
elif key_1 == 'Alt' and key_2 == 'Shift' and key_3 == 'Tab':
    msg = f'{key_1} + {key_2} + {key_3} : Quick move betwen files'
else:
    msg = 'Combination not foud'
print(msg)


#SOLUCION:
first_key = 'Super'
second_key = 'L'
third_key = ''

if first_key == 'Super':
    if second_key == 'L':
        action = 'Locks the screen'
    elif second_key == 'D':
        action = 'Show desktop'
    elif second_key == 'A':
        action = 'Shows the application menu'
    elif second_key == 'M':
        action = 'Toggle notification tray'
    elif second_key == 'Tab':
        action = 'Switch between running applications'
    elif second_key == 'Space':
        action = 'Change input keyboard'
    elif second_key == '<arrow>':
        action = 'Snap windows'
elif first_key == 'Alt':
    if second_key == 'F2':
        action = 'Run console'
    if second_key == 'Tab':
        action = 'Switch between running applications'
elif first_key == 'Ctrl':
    if second_key == 'Q':
        action = 'Close an application window'
    elif second_key == 'Alt':
        if third_key == '<arrow>':
            action = 'Move between workspaces'
        elif third_key == 'Del':
            action = 'Log out'
        elif third_key == 'T':
            action = 'Ubuntu terminal shortcut'
        elif third_key == 'L':
            action = 'Locks the screen'
        elif third_key == 'D':
            action = 'Show desktop'

print(action)
    
    
    

