def cipher(s:str):
    return ''.join(map(lambda t: chr(219 - ord(t)) if ord('a') <= ord(t) <= ord('z') else t, s))

print(cipher("I am a pen."))
