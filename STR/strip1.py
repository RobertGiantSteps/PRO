# *************************
# QUITANDO PRIMERO Y ÚLTIMO
# *************************


def run(text: str) -> str:
    text_processed = text[1:-1]
    stext = text_processed

    return stext


if __name__ == '__main__':
    run('What can I do')