# ********************************
# OBTENIENDO EL NÚMERO DE PALABRAS
# ********************************


def run(text: str) -> int:
    separate_text = text.split()
    num_words = len(separate_text)

    return num_words


if __name__ == '__main__':
    run('Before software can be reusable it first has to be usable')