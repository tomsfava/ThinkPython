def ngrams(words, order):
    """Returns a list of n-grams(tuples) of 
    size order given the list words"""
    return [tuple(words[i:i+order]) for i in range(len(words) - order + 1)]


def markov_analysis_text(text, order=2):
    """From a given text, returns a dictionary
    that maps from prefixes with given order, to 
    a collection of possible suffixes"""

    words = text.split()

    ngrams_list = ngrams(words, order)

    markov_dict = {}

    for ngram in ngrams_list:
        prefix = ngram[:-1] # todos os elementos menos o último
        suffix = ngram[-1] # último elemento

        if prefix not in markov_dict:
            markov_dict[prefix] = []
        markov_dict[prefix].append(suffix)
    
    return markov_dict

def markov_analysis_list(t, order=2):
    ngrams_list = ngrams(t, order)

    markov_dict = {}

    for ngram in ngrams_list:
        prefix = ngram[:-1]
        suffix = ngram[-1]

        if prefix not in markov_dict:
            markov_dict[prefix] = []
        markov_dict[prefix].append(suffix)
    
    return markov_dict


if __name__ == '__main__':
    text = "Half a bee, philosophically, Must, ipso facto, half not be. But half the bee has got to be Vis a vis, its entity. D'you see? But can a bee be said to be Or not to be an entire bee When half the bee is not a bee Due to some ancient injury?"

    markov_dict = markov_analysis(text)
    for prefix, suffixes in markov_dict.items():
        if len(suffixes) > 1:
            print(f'{prefix}: {suffixes}')
    

