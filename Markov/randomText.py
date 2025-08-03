import random
from .analysis import markov_analysis_list
from DataStructureSelection.ref import invisible_path
from DataStructureSelection.fileHistogram import proccessFile

def generate_text(markov_dict, order, length=50):
    # Começa com um prefixo aleatório do dicionário
    prefix =  random.choice(list(markov_dict.keys()))
    output_words = list(prefix) # inicializa com o prefixo

    for _ in range(length - (order - 1)):
        suffixes = markov_dict.get(prefix, None)
        if not suffixes:
            prefix = random.choice(list(markov_dict.keys()))
            output_words.extend(prefix)
            continue

        next_word = random.choice(suffixes)
        output_words.append(next_word)
        prefix = tuple(output_words[-(order - 1):])
    return ' '.join(output_words)

if __name__ == '__main__':
    word_list = proccessFile(invisible_path)

    markov_dict = markov_analysis_list(word_list, 8)

    generated = generate_text(markov_dict, 8, 250)
    print(generated)