import unicodedata
import time
from .ref import invisible_path

def cleanLine(line):
    """Remove pontuação usando unicodedata"""
    return ''.join(
        char if not unicodedata.category(char).startswith('P') else ''
        for char in line
    )

def proccessFile(txt):
    """Proccess a book removing header and footer, returns list of words"""
    all_words = []
    skip_header = True

    with open(txt, encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            if skip_header:
                if '[Illustration]' in line:
                    skip_header = False
                continue
            
            if line.startswith('*** END OF THE'):
                break
            line = cleanLine(line)
            words = line.lower().split()
            all_words.extend(words)
    return all_words

def fileHistogram(words):
    """Counts how many times each word appears on a list"""
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram

def print_stats(words, histogram, top_n=20):
    """Print book statistics"""
    print(f'Total de palavras no livro: {sum(histogram.values())}')
    print(f'Palavras únicas: {len(histogram)}')
    print(f'Média de uso por palavra única: {len(words)/len(histogram):.2f}')
    print('\n' + '=' * 50)
    print(f'Top {top_n} palavras mais frequentes:')
    print('='*50)

    sorted_words = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    # def most_common(hist):
    #   t = []
    #   for key, value in hist.items():
    #       t.append((value, key))
    #   t.sort(reverse=True)
    #   return t

    for i, (word, freq) in enumerate(sorted_words[:top_n], 1):
        percentage = (freq/len(words)) * 100
        print(f'{i:2d}, {word:<15} {freq:>6d} vezes ({percentage:>5.2f}%)')

if __name__ == '__main__':
    print('Processando "The Invisible Man"...')
    print('Removendo cabeçalho e rodapé do Project Gutenberg')

    start = time.perf_counter()
    words = proccessFile(invisible_path)
    time_processing = time.perf_counter() - start

    start = time.perf_counter()
    histogram = fileHistogram(words)
    time_histogram = time.perf_counter() - start

    print(f'\nTempo de processamento: {time_processing:.4f}s')
    print(f'Tempo para criar histograma: {time_histogram:.4f}s')
    print(f'Tempo total: {time_processing + time_histogram:.4f}s')

    print_stats(words, histogram)