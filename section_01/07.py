def f(x: int, y: str, z: float) -> str:
    return "{:d}時の{:s}は{:.1f}".format(x, y, z)

print(f(12, "気温", 22.4))
