# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************

VOWELS = 'aeiou'
def run(text: str) -> int:
    word_length = len(text)
    a = VOWELS[0]
    total = text.count(a) 
    e = VOWELS[1]
    total += text.count(e)
    i = VOWELS[2]
    total += text.count(i)
    o = VOWELS[3]
    total += text.count(o)
    u = VOWELS[4]
    total += text.count(u)
    
    
    
    metric = word_length * total 

    return metric


if __name__ == '__main__':
    run('ordenador')