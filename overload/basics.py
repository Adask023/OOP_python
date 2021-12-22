print('hi')


class F:
    a: int

    def __init__(self, a: int) -> None:
        self.a = a

    def __repr__(self) -> str:
        return f'F(a={self.a})'

    # potrzebne do a<b oraz .sort()
    def __lt__(self, other):
        return self.a < other.a

    # potrzebne do set(), dict()
    def __hash__(self) -> int:
        return self.a.__hash__()

    def __eq__(self, other):
        return self.a == other.a

    def __add__(self, other):
        return F(self.a + other.a)

    def __mul__(self, other):
        return F(self.a * other.a)




a = F(10)
b = F(20)
c = F(10)

w = [b, a, c]

s = set(w)
print(s)

print(a.__hash__())
print(b.__hash__())
print(c.__hash__())

# print(a, b.__hash__(), id(b))

print(a == b)

d = dict()
d[a] = 90
d[b] = 50
d[c] = 100
print(a + b)
