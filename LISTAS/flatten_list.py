# ***************
# APLANA LA LISTA
# ***************
""" 
Dada una lista - que puede contener sublistas 
(con sólo en 1 nivel de anidamiento) - │
│genere otra lista "aplanada".

"""

def run(elements: list) -> list:
    flat_list = []
    nested_elements = []
    for element in elements:
        if isinstance(element,list):
            nested_elements = [v for v in element]
            flat_list.extend(nested_elements)
        else:
            flat_list.append(element)
        
    flatten_elements = flat_list

    return flatten_elements


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])