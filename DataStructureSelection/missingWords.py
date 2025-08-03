from ref import invisible_path, words_path
from fileHistogram import proccessFile

# caso fosse tratar as palavras com dicionários, essa seria a forma de subtrair
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def load_dictionary(path):
    """Lê o arquivo words.txt e retorna um set com todas as palavras"""
    with open(path, encoding='utf-8') as fin:
        return set(word.strip().lower() for word in fin if word.strip())

if __name__ == '__main__':
    print('Lendo palavras do livro...')
    book_words = set(proccessFile(invisible_path))

    print('Lendo dicionário...')
    dictionary_words = load_dictionary(words_path)

    print('Comparando...')
    missing_words = sorted(book_words - dictionary_words)

    print(f'\nPalavras no livro que não estão no dicionário: {len(missing_words)}')
    print('=' * 50)
    for word in missing_words:
        print(word)
    print(f'Existe um total de {len(missing_words)} palavras presentes no livro que não estão no dicionário')