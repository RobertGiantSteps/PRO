# ************************
# INTERCAMBIANDO TU NOMBRE
# ************************


def run(name: str, surname: str) -> str:
    names = name
    surnames = surname
    
       
    fullname = f'{surnames}, {names}'

    return fullname


if __name__ == '__main__':
    run('Sergio', 'Delgado Quintero')