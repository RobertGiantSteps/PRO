# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    all_item = []
    for item in texts:
        if item == '':
            all_item = []
        else: 
            all_item.extend(item)
               
    chars = all_item

    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])