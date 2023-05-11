# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    processed_name = fullname.split()
    name = processed_name[0]
    surname = processed_name[1]
    surname_index = fullname.find(surname)
   
    
    
    
    
    
    
   
    swapname = f'{fullname[surname_index:]} {name}'

    return swapname


if __name__ == '__main__':
    run('John McClane'  )