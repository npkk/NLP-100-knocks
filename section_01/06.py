from itertools import chain

def make_letter_n_gram(n: int, S: str):
    T = S.split(' ')
    return list(chain.from_iterable([[t[i:i+n] for i in range(len(t) - n + 1)] for t in T]))

S = "paraparaparadise"
T = "paragraph"
X = set(make_letter_n_gram(2, S))
Y = set(make_letter_n_gram(2, T))
print(X)
print(Y)
print(X.union(Y))
print(X.intersection(Y))
print(X - Y)
print(Y - X)
print("se" in X)
print("se" in Y)