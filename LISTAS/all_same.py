# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    
    all_same = False
    new_list = []
    new_list.append(items[0])
    for i in range(1,len(items)):
        if items[i] == items[i - 1]:
            all_same = True
        else:
            all_same = False
        
        
    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])