"""
Zadanie:

utworzenie klasyu Fract, z polami p:int, q:int, implementującą ułamki zwykłe o wartości p/q

A)konstruktor, repr, X
B) operatory potrzebny do .sort() czyli __lt__ X
C) Operator potrzebny do set()... X
D)napisać metody from_float(), to_float()) implementujące zamienę ( jak najdokładniejszą na ułamki dziesiętne...
0.3333333333333 -> Fract(1,3)
E) zaimplementować operatory arytmetyczne:

"""


class Fract:
    p: int
    q: int

    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q

    def __repr__(self) -> str:
        return f'{self.p}/{self.q}'

    def __hash__(self):
        return (self.p, self.q).__hash__()

    def __lt__(self, other):

        sel_p = self.p
        sel_q = self.q
        for i in range(sel_p, 1, -1):
            while sel_q % i == 0 and sel_p % i == 0:
                sel_q = int(sel_q / i)
                sel_p = int(sel_p / i)

        oth_p = other.p
        oth_q = other.q
        for i in range(1, oth_q, -1):
            while oth_q % i == 0 and oth_p % i == 0:
                oth_q = int(oth_q / i)
                oth_p = int(oth_p / i)

        return ((sel_p / sel_q) * 100) > ((oth_p / oth_q) * 100)


if __name__ == '__main__':

    a = Fract(1, 4)
    b = Fract(4, 30)
    g = Fract(4, 3)
    c = Fract(10, 12)
    y = Fract(344, 344 * 1)
    
    print(a.__repr__())
    w = [b, a, c, g, y]

    s = set(w)
    print(s)

    print(w)
    w.sort()
    print(w)
