# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n

    return n

# Fraction class
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
