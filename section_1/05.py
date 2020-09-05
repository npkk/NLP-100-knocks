from itertools import chain

S = "I am an NLPer"

def make_word_n_gram(n: int, S: str):
    T = S.split(' ')
    return [T[i:i+n] for i in range(len(T) - n + 1)]

def make_letter_n_gram(n: int, S: str):
    T = S.split(' ')
    return list(chain.from_iterable([[t[i:i+n] for i in range(len(t) - n + 1)] for t in T]))

print(make_word_n_gram(2, S))
print(make_letter_n_gram(2, S))