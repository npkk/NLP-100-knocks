S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
oList = [1, 5, 6, 7, 8, 9, 15, 16, 19]
T = S.strip(',.').split(' ')
M = {}
for idx, t in enumerate(T):
    if idx + 1 in oList:
        t = t[:1]
    else:
        t = t[:2]
    M[t] = idx + 1
print(M)