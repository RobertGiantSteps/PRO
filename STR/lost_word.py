# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    word_index = text.find(target_word)
    target_size = len(target_word)
    first_part = text[:word_index]
    split_part = text[word_index:]
    second_part = split_part[target_size:] 
    
    
    
  
    

    mtext = first_part + replace_word + second_part

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')