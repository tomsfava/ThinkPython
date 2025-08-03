import string
import time
from ref import invisible_path

def fileLineBreakerA(txt):
    all_words = []
    with open(txt, encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            for char in string.punctuation:
                line = line.replace(char, ' ')
            words = line.lower().split()
            all_words.extend(words)
    return all_words

def fileLineBreakerB(txt):
    all_words = []
    with open(txt, encoding='utf-8') as fin:
        trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        for line in fin:
            line = line.strip()
            line = line.translate(trans)
            words = line.lower().split()
            all_words.extend(words)
    return all_words

if __name__ == '__main__':
    start = time.time()
    words_a = fileLineBreakerA(invisible_path)
    time_a = time.time() - start
    start = time.time()
    words_b = fileLineBreakerB(invisible_path)
    time_b = time.time() - start

    print(f'Função A: {time_a:.4f} segundos - {len(words_a)} palavras')
    print(f'Função B: {time_b:.4f} segundos - {len(words_b)} palavras')
    print(f'Função B é {time_a/time_b:.2f}x mais rápida' if time_b < time_a else f'Função A é {time_b/time_a:.2f}x mais rápida')



