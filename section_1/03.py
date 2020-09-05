import collections
from pprint import pprint
S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
T = list(map(lambda x: x.strip(',.') ,S.split(' ')))
alphas = list(map(lambda t: {t: dict(collections.Counter(t))}, T))
pprint(alphas)
