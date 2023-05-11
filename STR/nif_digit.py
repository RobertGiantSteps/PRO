# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************

ID_LETTER = 'T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'
ALGORIT_NUMBER = 23
def run(nif: str) -> str:
    nif_number = int(nif)
    control_digit = nif_number % ALGORIT_NUMBER
    index_letter = ID_LETTER.split(',') 
    wnif = str(nif_number) + index_letter[control_digit]

    return wnif


if __name__ == '__main__':
    run('78654355')