# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************

HASHTAG = '#'
def run(html: str) -> str:
    clean_html = html.strip('<h>')
    separeted_html = clean_html.split('>')
    number = int(separeted_html[0])
    tail = str(separeted_html[1])
    text = tail.split('</')
    
    

    
    markdown = f'{HASHTAG * number} {text[0]}'

    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')