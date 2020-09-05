import random

S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def Typoglicemia(s:str) -> str:
    return s if len(s) <= 4 else s[0] + ''.join(random.sample(s[1:-1], len(s[1:-1]))) + s[-1]

print(' '.join(map(Typoglicemia, S.split(' '))))