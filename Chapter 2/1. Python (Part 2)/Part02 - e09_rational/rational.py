class Rational(object):
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Rational(num, den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __repr__(self):
        return f"{self.num}/{self.den}"


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
